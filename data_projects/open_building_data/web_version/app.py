import matplotlib
matplotlib.use('Agg')  # Set the backend before importing pyplot


from flask import Flask, render_template, request, after_this_request
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import re


# Set the Agg backend
plt.switch_backend('Agg')

app = Flask(__name__)

# Constants
DATA_FOLDER = "data"
RAW_DATA_FOLDER = "raw"
PROCESSED_DATA_FOLDER = "processed"
PLOT_FOLDER = "static"

def read_data(file_path):
    """Read data from a CSV file."""
    return pd.read_csv(file_path, low_memory=False)

def set_seaborn_style_palette():
    """Set seaborn style and palette."""
    sns.set(style="whitegrid")
    sns.set_palette("viridis")

def save_plot(figure, plot_name, folder):
    """Save a plot to the specified folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    figure.savefig(os.path.join(folder, plot_name))
    plt.close()

def process_data(df):
    """Process the data, including setting energy rating order."""
    energy_rating_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    df['CURRENT_ENERGY_RATING'] = pd.Categorical(df['CURRENT_ENERGY_RATING'], categories=energy_rating_order, ordered=True)

def plot_horizontal_bar(df, area):
    """Generate and save a horizontal bar plot."""
    energy_rating_order_dynamic = df['CURRENT_ENERGY_RATING'].cat.categories
    energy_rating_counts = df['CURRENT_ENERGY_RATING'].value_counts().reset_index()
    energy_rating_counts.columns = ['CURRENT_ENERGY_RATING', 'Number of Records']

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Number of Records', y='CURRENT_ENERGY_RATING', data=energy_rating_counts, order=energy_rating_order_dynamic)
    plt.xlabel('Number of Records')
    plt.ylabel('Current Energy Rating')
    plt.title('Distribution of Energy Ratings of '+ str(area))
    plt.tight_layout()
    save_plot(plt, 'horizontal_bar_plot_rating_records.png', PLOT_FOLDER)

def other_plots(df, plot_type):
    # Bar Chart
    plt.figure(figsize=(12, 6))
    sns.countplot(x='PROPERTY_TYPE', data=df)
    plt.xticks(rotation=45)
    plt.xlabel('Property Type')
    plt.ylabel('Count')
    plt.title('Count of Properties by Property Type')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, 'bar_chart_count_prop_by_type.png'))
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='CURRENT_ENERGY_RATING', y='TOTAL_FLOOR_AREA', data=df)
    plt.xlabel('Current Energy Rating')
    plt.ylabel('Total Floor Area')
    plt.title('Scatter Plot of Current Energy Rating vs. Total Floor Area')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, 'scatter_plot_rating_tfa.png'))
    plt.close()

    # Grouped Bar Chart
    plt.figure(figsize=(12, 6))
    sns.countplot(x='CONSTRUCTION_AGE_BAND', hue='CURRENT_ENERGY_RATING', data=df)
    plt.xticks(rotation=45)
    plt.xlabel('Construction Age Band')
    plt.ylabel('Count')
    plt.title('Count of Energy Ratings by Construction Age Band')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, 'grouped_bar_chart_rating_age_band.png'))
    plt.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    area = request.form['area']

    # Validate the area if needed
    # ...

    # Read data
    folder_name = [name for name in os.listdir(os.path.join(DATA_FOLDER, RAW_DATA_FOLDER, "all-domestic-certificates")) 
                   if re.match(r'domestic-.*', name, re.IGNORECASE) and area.lower() in name.lower()]

    if not folder_name:
        return f"No matching folder found for area: {area}"

    file_path = os.path.join(DATA_FOLDER, RAW_DATA_FOLDER, "all-domestic-certificates", folder_name[0], "certificates.csv")
    df = read_data(file_path)

    # Set seaborn style and palette
    set_seaborn_style_palette()

    # Process data
    process_data(df)
    print(df)
    
    # Create a list to store plot names
    plot_names = []
    
    # Plot based on user input
    plot_horizontal_bar(df, area)
    plot_names.append('horizontal_bar_plot_rating_records.png')
    other_plots(df, area)
    plot_names.append('bar_chart_count_prop_by_type.png')
    plot_names.append('scatter_plot_rating_tfa.png')
    plot_names.append('grouped_bar_chart_rating_age_band.png')

    return render_template('plot.html', plot_names=plot_names)

if __name__ == '__main__':
    app.run(debug=True)
