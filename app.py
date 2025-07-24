import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv("api_landscape.csv")

# App title and layout
st.set_page_config(page_title="Infra Product Viewer", layout="wide")

st.title("🛠️ Infra Product Landscape Viewer")
st.caption("Explore infrastructure tools by category, use case, and product.")

# Sidebar filter
with st.sidebar:
    st.header("🔍 Filters")
    category = st.selectbox("Select Infra Category", ["All"] + sorted(df["Infra Category"].dropna().unique()))

# Filter dataframe
if category != "All":
    filtered_df = df[df["Infra Category"] == category]
else:
    filtered_df = df

# Tabs for switching between views
tab1, tab2 = st.tabs(["📊 Chart", "📋 Table"])

with tab1:
    if not filtered_df.empty:
        chart_data = filtered_df["Infra Category"].value_counts().reset_index()
        chart_data.columns = ["Infra Category", "Count"]
        fig = px.bar(chart_data, x="Infra Category", y="Count", title="Products per Infra Category", color="Infra Category")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data for selected category.")

with tab2:
    st.dataframe(filtered_df[["Product", "Notes"]].reset_index(drop=True), use_container_width=True)



