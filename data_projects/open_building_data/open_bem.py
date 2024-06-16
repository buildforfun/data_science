import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class OpenBEM:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        """Read data from a CSV file."""
        self.df = pd.read_csv(self.file_path, low_memory=False)
    
    def process_data(self):
        """Process the data, including setting energy rating order."""
        energy_rating_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.df['CURRENT_ENERGY_RATING'] = pd.Categorical(self.df['CURRENT_ENERGY_RATING'], \
                                                    categories=energy_rating_order, ordered=True)

    def numberEPCs(self):
        """Print results and statistics."""
        lodgements_by_local_authority = self.df['LOCAL_AUTHORITY'].value_counts()
        local_authority = self.df['LOCAL_AUTHORITY_LABEL'].value_counts()
        local_authority_name = local_authority.idxmax()
        sum_lodgements_count = lodgements_by_local_authority.sum()

        numberEPC = f'In the latest data release, there are {sum_lodgements_count} EPC lodgments in \
        {local_authority_name}'
        return numberEPC, local_authority_name

    def save_plot(self,figure, plot_name):
        """Save a plot to the specified folder."""
        figure.savefig(os.path.join(plot_name))
        plt.close()

    def plot_energyratings_bands(self, authority_name):
        """Generate and save a horizontal bar plot."""
        energy_rating_order_dynamic = self.df['CURRENT_ENERGY_RATING'].cat.categories
        energy_rating_counts = self.df['CURRENT_ENERGY_RATING'].value_counts().reset_index()
        energy_rating_counts.columns = ['CURRENT_ENERGY_RATING', 'Number of Records']

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Number of Records', y='CURRENT_ENERGY_RATING', data=energy_rating_counts, \
                    order=energy_rating_order_dynamic)
        plt.xlabel('Number of Records')
        plt.ylabel('Current Energy Rating')
        plt.title('Distribution of Energy Ratings in '+ str(authority_name))
        plt.tight_layout()
        self.save_plot(plt, 'plots/horizontal_bar_plot_rating_records in '+str(authority_name)+'.png')
    
    def plot_property_type_count(self, authority_name):
        plt.figure(figsize=(12, 6))
        sns.countplot(x='PROPERTY_TYPE', data=self.df)
        plt.xticks(rotation=45)
        plt.xlabel('Property Type')
        plt.ylabel('Count')
        plt.title('Count of Properties by Property Type in '+ str(authority_name))
        plt.tight_layout()
        plt.savefig(os.path.join('plots/bar_chart_count_prop_by_type in '+ str(authority_name)+'.png'))
        plt.close()

    def make_report(self,authority_name, numberEPC):
        # Create a PDF report
        doc = SimpleDocTemplate("reports/open_epc_report_for_"+str(authority_name)+".pdf", pagesize=letter)
        content = []

        # Add title and subtitle to the report
        title = "Open EPC Report for "+str(authority_name)
        content.append(Paragraph(title, getSampleStyleSheet()['Title']))
        content.append(Spacer(1, 12))
        content.append(Paragraph(numberEPC, getSampleStyleSheet()['BodyText']))
        # Add plot to the report using Image class
        content.append(Image('plots/bar_chart_count_prop_by_type in '+ str(authority_name)+'.png', width=400, height=300))
        content.append(Image('plots/horizontal_bar_plot_rating_records in '+str(authority_name)+'.png', width=400, height=300))

        # Build the PDF report
        doc.build(content)


sns.set(style="whitegrid")
sns.set_palette("viridis")
        
file_path = "data/domestic-E09000006-Bromley/certificates.csv"
openepc = OpenBEM(file_path)
openepc.read_data()
openepc.process_data()
numberEPC, local_authority_name = openepc.numberEPCs()
openepc.plot_energyratings_bands(local_authority_name)
openepc.plot_property_type_count(local_authority_name)
openepc.make_report(local_authority_name, numberEPC)

