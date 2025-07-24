import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv("api_landscape.csv")

# App config
st.set_page_config(page_title="Infra Product Landscape Viewer", layout="wide")
st.title("🛠️ Infra Product Landscape Viewer")
st.caption("Explore infrastructure tools by category, use case, and product.")

# Sidebar: category selector
with st.sidebar:
    st.header("🔍 Filters")
    category = st.selectbox("Select Infra Category", ["All"] + sorted(df["Infra Category"].dropna().unique()))
    keyword = st.text_input("Search products or notes")

# Filter by category
if category != "All":
    filtered_df = df[df["Infra Category"] == category]
else:
    filtered_df = df.copy()

# Filter by keyword
if keyword:
    keyword = keyword.lower()
    filtered_df = filtered_df[
        filtered_df["Product"].str.lower().str.contains(keyword)
        | filtered_df["Notes"].str.lower().str.contains(keyword)
    ]

# Tabs for chart and table
tab1, tab2 = st.tabs(["📊 Chart", "📋 Table"])

with tab1:
    if not filtered_df.empty:
        chart_data = filtered_df["Infra Category"].value_counts().reset_index()
        chart_data.columns = ["Infra Category", "Count"]
        fig = px.bar(chart_data, x="Infra Category", y="Count", title="Products per Infra Category", color="Infra Category")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data matches your filters.")

with tab2:
    if not filtered_df.empty:
        st.dataframe(filtered_df[["Product", "Notes"]].reset_index(drop=True), use_container_width=True)
    else:
        st.info("No results to display.")


