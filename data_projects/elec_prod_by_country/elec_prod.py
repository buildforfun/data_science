import os
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector

country_input = input("Enter country: ")

# Database connection details
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

# Connect to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Execute a query
query = "SELECT Coal,Natural_gas, Oil, Hydropower,Renewable_sources,Nuclear FROM ElecProdBySource WHERE Country = %s"
cursor.execute(query, (country_input,))
result = cursor.fetchone()
result = list(result)

# Plot the data
column_headings = ['Coal', 'Natural gas', 'Oil', 'Hydropower', 'Renewable_sources', 'Nuclear']

# Adjust the figure size and style
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(column_headings, result, color='steelblue', alpha=0.8, edgecolor='black')

ax.set(xlabel='Fuel source', ylabel='Percentage (%)',
       title=f'Sources of electricity production in {country_input}')

# Customize grid and ticks
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent clipping of labels or title
plt.tight_layout()

fig.savefig("plots/Elec_fuel_source_plot " + str(country_input)+ ".png")