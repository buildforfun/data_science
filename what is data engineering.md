**What is data engineering?**

Data engineering is the stuff data enginers do, so i will talk about that. Data engineers control the flow of data, in that they build custom data storage systems that transport data through it's various forms into formats needed by the organisations. 

# A typical data engineer flow

1. **Understand problem: to solve this problem, the data engineer must first get clarity on the problem:**
    - Determine frequency in time.
    - Determine whether any filters should be applied to the data
    - Determine the timeframe of the data
    - Determine the data sources of the data
2. **Data extraction and exploration**
    - Determine what joins should be used between the tables and what the relationships are between these tables.
    - Assess the quality of the data: decide if missing or anomalous data may need to be corrected.
3. **Design and create database architecture**
    - Design and create a database that can be used to hold the required data.
4. **Ingest correct data from different sources**
    - Import the data from various sources into the database.
    - Sources of data:
        - Web data
        - Survey data
        - Customer data
        - Financial transactions
		- IoT devices
    - How to access public data?
        - API - where you request data from a company over the internet.
        - Public data records are another great way of gathering data.

5. **Build automated data pipelines**
    - If we are collecting from different sources, it is helpful to have a way of bringing all that data together in one go. That's where a data pipeline comes in! It does exactly that, it moves data from the source into the format needed for analysis in one flow and automates the whole process. This pipeline can then be scheduled to run either manually or automatically.

# Relational database
The relational database is the most common type of database that’s in use today. What is a relational database I hear you ask? Think of a relational database as a group of tables that can be connected to each other without needing to be all in one table.

# How to a design databases
I’ve taken all of the steps from the book Database design for Mere Mortals by Michael J. Hernandez. I’ve simplified the steps, but all the main steps are nearly all the same.

1. **Develop a mission statement and mission objective.**
    1. **Mission statement: purpose of database**
    2. **Mission objectives: what tasks the user should be able to perform with the data.**
2. **Analyse the current database**
    1. **Look at how data is currently collected**
    2. **Review of other similar databases**
    3. **Look at how data is presented**
    4. **Create initial field list**
3. **Create the database structure**
    1. **Use initial list of fields to identify tables within data**
    2. **Compose table descriptions for table**
    3. **Create field specification**
4. **Determine and establish table relationship**
    1. **Understand how the different tables are related**
    2. **Create relationship diagrams**
5. **Define and establish database rules**
    1. **Review and determine if constraints are needed**
    2. **Update field specification**
    3. **Think about how to test database rule**
6. **Determine and Define views**
    1. **Views Subset of database**
7. **Review data integrity**
    1. **Go through and check if implemented correctly**
    2. **Collate all the documentation**
8. **Database design complete!**