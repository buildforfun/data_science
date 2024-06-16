
from sqlalchemy import create_engine, Column, String, Float, MetaData, Table, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import csv
from urllib.parse import quote_plus

# Database configuration
db_config = {
    'user': 'root',
    'password': '#L0ngP@ssw0rd!',
    'host': 'localhost',
    'port': 3306,
    'database': 'WorldBankData'
}
# Encode the password
encoded_password = quote_plus(db_config['password'])

# Construct the database URL
DATABASE_URL = f"mysql+pymysql://{db_config['user']}:{encoded_password}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Create the engine for the initial connection (without specifying the database)
initial_engine = create_engine(f"mysql+pymysql://{db_config['user']}:{encoded_password}@{db_config['host']}:{db_config['port']}")

# Create the database if it doesn't exist
with initial_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS WorldBankData"))

# Create the engine for the specific database
engine = create_engine(DATABASE_URL)

# Define the base class for the ORM
Base = declarative_base()

# Define the table schema
class ElecProdBySource(Base):
    __tablename__ = 'ElecProdBySource'
    Country = Column(String(255), primary_key=True)
    Coal = Column(Float)
    Natural_gas = Column(Float)
    Oil = Column(Float)
    Hydropower = Column(Float)
    Renewable_sources = Column(Float)
    Nuclear = Column(Float)
    Access_to_electricity = Column(Float)

# Create the table
Base.metadata.create_all(engine)

# Load data from CSV into the table
csv_file_path = 'data/processed/3.7_Electricity_production_sources_and_access_processed.csv'
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Convert empty strings to None
for row in data:
    for key, value in row.items():
        if value == '':
            row[key] = None

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Convert data to instances of ElecProdBySource
for row in data:
    record = session.query(ElecProdBySource).filter_by(Country=row['Country']).first()
    if record:
        # Update existing record
        for key, value in row.items():
            setattr(record, key, value)
    else:
        # Add new record
        new_record = ElecProdBySource(**row)
        session.add(new_record)

# Commit the session
try:
    session.commit()
except IntegrityError as e:
    session.rollback()
    print(f"Error occurred: {e}")
finally:
    session.close()



from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from urllib.parse import quote_plus

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define the table schema
class ElecProdBySource(db.Model):
    __tablename__ = 'ElecProdBySource'
    Country = db.Column(db.String(255), primary_key=True)
    Coal = db.Column(db.Float)
    Natural_gas = db.Column(db.Float)
    Oil = db.Column(db.Float)
    Hydropower = db.Column(db.Float)
    Renewable_sources = db.Column(db.Float)
    Nuclear = db.Column(db.Float)
    Access_to_electricity = db.Column(db.Float)

# Create the table (if it doesn't exist)
with app.app_context():
    db.create_all()


'''
API endpoint

@app.route('/elec_prod_by_country_API', methods=['GET']) defines an endpoint /users that responds to HTTP GET requests.
The get_users function is called when a GET request is made to /co2_calculator.
Inside the function, a connection to the MySQL database is established using mysql.connector.
A query is executed to retrieve all users from the co2_calculator table.
The fetched users are returned as a JSON response.

'''

@app.route('/elec_prod_by_country_API', methods=['GET'])
def get_co2_data():
    try:
        # Get the user input value from the query parameters
        input_value = request.args.get('inputValue', '')
        
        if not input_value:
            return jsonify({'error': 'InputValue is required'}), 400

        print(f'Received input value: {input_value}')
        
        # Query the database for the specified country
        co2_data = ElecProdBySource.query.filter_by(Country=input_value).first()
        
        if not co2_data:
            print('error')
            return jsonify({'error': f'No data found for {input_value}'}), 404

        # Convert the result to a dictionary
        co2_data_dict = {
            'Coal': co2_data.Coal,
            'Natural_gas': co2_data.Natural_gas,
            'Oil': co2_data.Oil,
            'Hydropower': co2_data.Hydropower,
            'Renewable_sources': co2_data.Renewable_sources,
            'Nuclear': co2_data.Nuclear,
            'Access_to_electricity': co2_data.Access_to_electricity
        }

        print('Sending result:', co2_data_dict)
        return jsonify({input_value: co2_data_dict})

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)