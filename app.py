import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("api_landscape.csv")

# App config
st.set_page_config(page_title="Infra Product Landscape Viewer", layout="wide")
st.title("🛠️ Infra Product Landscape Viewer")
st.caption("Explore infrastructure tools by category, use case, and product.")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    
    # Infra category filter
    category = st.selectbox("Select Infra Category", ["All"] + sorted(df["Infra Category"].dropna().unique()))
    
    # Product name dropdown (type-to-search)
    product_options = sorted(df["Product"].dropna().unique())
    selected_product = st.selectbox("Select Product", ["All"] + product_options)
    
    # Notes/keyword search (optional)
    keyword = st.text_input("Search Notes or Keywords")

# Apply filters
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["Infra Category"] == category]

if selected_product != "All":
    filtered_df = filtered_df[filtered_df["Product"] == selected_product]

if keyword:
    keyword = keyword.lower()
    filtered_df = filtered_df[
        filtered_df["Product"].str.lower().str.contains(keyword)
        | filtered_df["Notes"].str.lower().str.contains(keyword)
    ]

# Tabs
tab1, tab2 = st.tabs(["📊 Chart", "📋 Table"])

with tab1:
    if not filtered_df.empty:
        chart_data = filtered_df["Infra Category"].value_counts().reset_index()
        chart_data.columns = ["Infra Category", "Count"]
        fig = px.bar(chart_data, x="Infra Category", y="Count", color="Infra Category", title="Products per Infra Category")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data matches your filters.")

with tab2:
    if not filtered_df.empty:
        st.dataframe(filtered_df[["Product", "Notes"]].reset_index(drop=True), use_container_width=True)
    else:
        st.info("No results to display.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")



