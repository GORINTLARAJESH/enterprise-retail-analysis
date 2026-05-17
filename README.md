# Enterprise Retail Analytics Platform

## Project Objective
Build an enterprise-grade retail analytics solution using Python, PostgreSQL, SQL, and Power BI.

## Tech Stack
- Python
- Pandas
- PostgreSQL
- SQL
- Power BI

## Features
- ETL pipeline
- Data cleaning
- SQL warehouse
- KPI analytics
- Executive dashboard

## project Structure
Enterprise-Retail-Analytics/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── etl/
│   ├── load_data.py
│   ├── clean_data.py
│   └── transform_data.py
│
├── sql/
│   ├── schema.sql
│   ├── create_tables.sql
│   ├── load_data.sql
│   └── business_queries.sql
│
├── dashboard/
│   └── retail_dashboard.pbix
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── reports/
│   └── business_insights.md
│
├── screenshots/
│
├── logs/
│
├── requirements.txt
├── README.md
└── .gitignore
## project workflow
Dataset
   ↓
Python ETL
   ↓
Data Cleaning
   ↓
PostgreSQL
   ↓
SQL Analytics
   ↓
Power BI Dashboard
   ↓
Git Version Control

# Today's Journey — Day 1

## Enterprise Retail Analytics Platform

Today I started building an end-to-end Enterprise Retail Analytics Platform using Python, Pandas, SQL, PostgreSQL, and Power BI.

---

## Work Completed Today

### Project Initialization

* Created enterprise-grade project structure
* Organized folders for ETL, SQL, reports, dashboards, logs, and datasets
* Initialized Git repository for version control

---

### Dataset Setup

* Downloaded and organized Olist Ecommerce datasets
* Structured datasets into:

  * raw
  * cleaned
  * processed layers

---

### ETL Pipeline Development

Created modular ETL scripts:

* load_data.py
* clean_data.py
* transform_data.py

---

### Data Loading

* Loaded ecommerce datasets using Pandas
* Inspected schema and dataset structure
* Analyzed datatypes and missing values

---

### Data Cleaning

* Removed duplicate records
* Converted datetime columns
* Performed null-value analysis
* Generated cleaned datasets

---

### Data Transformation

* Merged datasets using business keys
* Created analytical metrics
* Extracted time-based features
* Generated analytics-ready transformed datasets

---

## Challenges Faced & Solved

* File path debugging
* CSV vs Excel extension confusion
* ETL dependency handling
* Output directory management
* Python syntax debugging

---

## Key Learnings

* ETL workflow fundamentals
* Enterprise project organization
* Data pipeline debugging
* Business-oriented data analysis
* Importance of clean data architecture

---

## Tech Stack Used

* Python
* Pandas
* Git
* VS Code

---

## Current Workflow

Raw Data
↓
Load Data
↓
Clean Data
↓
Transform Data
↓
Analytics-Ready Dataset

---

## Next Step

* PostgreSQL integration
* SQL analytics layer
* KPI queries
* Power BI dashboard development


# Today's Journey — Day 2

# Enterprise Retail Analytics Platform

Today I worked on PostgreSQL integration and successfully imported transformed ecommerce datasets into the analytics database.

---

# Work Completed Today

## PostgreSQL Setup

- Installed PostgreSQL 18
- Configured pgAdmin 4
- Connected local PostgreSQL server
- Created enterprise_retail_analytics database

---

## Database Setup

- Created orders table in PostgreSQL
- Configured table columns and datatypes
- Prepared database for analytics workflow

---

## Data Import Process

- Imported cleaned ecommerce dataset into PostgreSQL
- Successfully loaded 99,441 records into the orders table
- Verified imported records and database structure

---

# Problems Faced & Solved

## CSV Header Import Issue

Problem:
PostgreSQL treated CSV column headers as actual timestamp values.

Solution:
Enabled HEADER option during CSV import.

---

## Timestamp Parsing Error

Problem:
Timestamp columns generated datatype errors during import.

Solution:
Validated CSV import settings and corrected PostgreSQL configuration.

---

## CSV Import Configuration

Problem:
Incorrect import settings caused data loading failures.

Solution:
Verified delimiter, encoding, and header configurations.

---

# Key Learnings

- PostgreSQL installation and setup
- pgAdmin workflow
- SQL table creation
- CSV import handling
- Timestamp datatype debugging
- Database import troubleshooting
- Enterprise database workflow

---

# Tech Stack Used

- PostgreSQL
- pgAdmin 4
- SQL
- Python
- Pandas
- VS Code

---

# Current Workflow

Raw Data
↓
Cleaned Data
↓
Transformed Data
↓
PostgreSQL Database

---

# Project Status

✅ PostgreSQL Installed  
✅ Database Created  
✅ Orders Table Created  
✅ Ecommerce Data Imported Successfully  

---

# Next Step

- Write SQL analytics queries
- Create KPI metrics
- Perform business analysis
- Build Power BI dashboards