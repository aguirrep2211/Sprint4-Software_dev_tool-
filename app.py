import pandas as pd
import panel as pn
import plotly.express as px

pn.extension('plotly')

# Load data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    # Separate brand and model_01 from 'model'
    df[['brand', 'model_01']] = df['model'].str.split(' ', n=1, expand=True)
    df.drop(columns='model', inplace=True)

    # Reorder columns to place brand and model_01 after 'price'
    cols = list(df.columns)
    insert_index = cols.index('price') + 1
    new_order = cols[:insert_index] + ['brand', 'model_01'] + [col for col in cols[insert_index:] if col not in ['brand', 'model_01']]
    df = df[new_order]

    return df

df = load_data()

# -------- Layout -------- #

# Data preview
data_table = pn.pane.DataFrame(df.head(), width=1000)

# Histogram: Price
fig_price_hist = px.histogram(df, x="price", nbins=100, title="Price Distribution")
plot_price_hist = pn.pane.Plotly(fig_price_hist)

# Histogram: Odometer
fig_odometer_hist = px.histogram(df, x="odometer", nbins=100, title="Odometer Distribution")
plot_odometer_hist = pn.pane.Plotly(fig_odometer_hist)

# Scatter: Price vs Model Year
fig_price_model_year = px.scatter(df, x="model_year", y="price", opacity=0.5, title="Price vs Model Year")
plot_price_model_year = pn.pane.Plotly(fig_price_model_year)

# Scatter: Price vs Odometer
fig_price_odometer = px.scatter(df, x="odometer", y="price", opacity=0.5, title="Price vs Odometer")
plot_price_odometer = pn.pane.Plotly(fig_price_odometer)

# Brand selector and summary
brand_selector = pn.widgets.Select(name="Choose a Brand", options=sorted(df['brand'].dropna().unique()))

@pn.depends(brand_selector)
def brand_summary(brand):
    filtered_df = df[df['brand'] == brand]
    if filtered_df.empty:
        return pn.pane.Markdown("### No data available for this brand.")

    top_model = filtered_df['model_01'].mode().iloc[0]
    model_df = filtered_df[filtered_df['model_01'] == top_model]

    car_type = model_df['type'].mode().iloc[0] if not model_df['type'].isna().all() else 'Unknown'
    avg_days_listed = model_df['days_listed'].mean()

    return pn.pane.Markdown(f"""
    ### Summary for **{brand}**
    - Most sold model: **{top_model}**
    - Type: **{car_type}**
    - Average number of days listed: **{avg_days_listed:.2f}**
    """)

# Panel layout
dashboard = pn.Column(
    "## Used Vehicles Data Analysis",
    "### Data Preview", data_table,
    "### Price Distribution", plot_price_hist,
    "### Odometer Distribution", plot_odometer_hist,
    "### Price vs Model Year", plot_price_model_year,
    "### Price vs Odometer", plot_price_odometer,
    "### Brand Summary",
    brand_selector,
    brand_summary
)

dashboard.servable()
