import pandas as pd

# Load the CSV
df = pd.read_csv('api_landscape.csv')

# Preview the data
df.head()

# Check column names and data types
df.info()

# Check for any nulls
df.isnull().sum()

!pip install plotly
import plotly.express as px

# Bar chart: Number of products per infra category
fig = px.bar(df, x='Infra Category', title='Products per Infra Category')
fig.show()
# Filter for a specific infra category
selected_infra = 'Blockchain'  # <- Try changing this to 'Comms SDK', etc.

filtered_df = df[df['Infra Category'] == selected_infra]

# Show product names and notes
filtered_df[['Product', 'Notes']]

