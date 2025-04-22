import pandas as pd
import panel as pn
import plotly.express as px

pn.extension('plotly')

# Load and prepare data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    df[['brand', 'model_01']] = df['model'].str.split(' ', n=1, expand=True)
    df.drop(columns='model', inplace=True)
    cols = list(df.columns)
    insert_index = cols.index('price') + 1
    new_order = cols[:insert_index] + ['brand', 'model_01'] + [col for col in cols[insert_index:] if col not in ['brand', 'model_01']]
    return df[new_order]

df = load_data()

# Create brand-model dictionary
brand_model_df = df[['brand', 'model_01']].drop_duplicates().sort_values(by='brand').reset_index(drop=True)
brand_model_dict = (
    brand_model_df
    .groupby('brand')['model_01']
    .apply(lambda x: sorted(x.dropna().unique()))
    .to_dict()
)

# Widgets
brand_select = pn.widgets.Select(name="Select a Brand", options=sorted(brand_model_dict.keys()))
model_select = pn.widgets.Select(name="Select a Model", options=[])

# Update model options when brand changes
@pn.depends(brand_select, watch=True)
def update_model_options(brand):
    model_select.options = brand_model_dict.get(brand, [])
    model_select.value = model_select.options[0] if model_select.options else None

# Manually update once at startup
update_model_options(brand_select.value)

# Summary for selected brand and model
@pn.depends(brand_select, model_select)
def summarize_model(brand, model):
    filtered = df[(df['brand'] == brand) & (df['model_01'] == model)]
    if filtered.empty:
        return pn.pane.Markdown("No data for this selection.")

    car_type = filtered['type'].mode().iloc[0] if not filtered['type'].isna().all() else 'Unknown'
    avg_days = filtered['days_listed'].mean()
    avg_price = filtered['price'].mean()

    return pn.pane.Markdown(f"""
    ### Summary for {brand.title()} {model.title()}
    - Type: **{car_type}**
    - Average Price: **${avg_price:,.2f}**
    - Average Days Listed: **{avg_days:.2f}**
    """)

# Dynamic visualizations
@pn.depends(brand_select, model_select)
def plot_price_distribution(brand, model):
    filtered = df[(df['brand'] == brand) & (df['model_01'] == model)]
    fig = px.histogram(filtered, x="price", nbins=50, title="Price Distribution")
    return pn.pane.Plotly(fig)

@pn.depends(brand_select, model_select)
def plot_odometer_distribution(brand, model):
    filtered = df[(df['brand'] == brand) & (df['model_01'] == model)]
    fig = px.histogram(filtered, x="odometer", nbins=50, title="Odometer Distribution")
    return pn.pane.Plotly(fig)

@pn.depends(brand_select, model_select)
def plot_price_vs_model_year(brand, model):
    filtered = df[(df['brand'] == brand) & (df['model_01'] == model)]
    fig = px.scatter(filtered, x="model_year", y="price", title="Price vs Model Year", opacity=0.5)
    return pn.pane.Plotly(fig)

@pn.depends(brand_select, model_select)
def plot_price_vs_odometer(brand, model):
    filtered = df[(df['brand'] == brand) & (df['model_01'] == model)]
    fig = px.scatter(filtered, x="odometer", y="price", title="Price vs Odometer", opacity=0.5)
    return pn.pane.Plotly(fig)

# Introductory markdown text
intro_text = pn.pane.Markdown("""
## Used Vehicles Data Analysis

The dataset contains information on 51,525 used vehicles listed for sale in the United States. The average listed price is approximately $12,132, with a wide range from $1 to $375,000, reflecting a diverse selection of vehicle types and conditions. The model year of the cars spans from 1908 to 2019, with the median vehicle being from 2011, suggesting a strong representation of relatively modern used cars.

There are 100 unique car models in the dataset, with the most common being the Ford F-150, which appears 2,796 times. Vehicles are categorized by condition, with "excellent" being the most frequently reported state, accounting for nearly 24,773 entries. Other condition categories include good, like new, fair, salvage, and new.

Regarding engine specifications, the average number of cylinders is about 6, with most cars having either 4, 6, or 8 cylinders—typical for common sedans, SUVs, and trucks.

Overall, this dataset offers a robust snapshot of the U.S. used vehicle market, suitable for pricing analysis, trend forecasting, and predictive modeling based on attributes like price, condition, year, and model.
""", width=900)

# Dashboard layout
dashboard = pn.Column(
    intro_text,
    "### Select Brand and Model",
    brand_select,
    model_select,
    summarize_model,
    "### Price Distribution", plot_price_distribution,
    "### Odometer Distribution", plot_odometer_distribution,
    "### Price vs Model Year", plot_price_vs_model_year,
    "### Price vs Odometer", plot_price_vs_odometer,
    "### Data Preview",
    pn.pane.DataFrame(df.head(), width=1000)
)

dashboard.servable()
