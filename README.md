# Django CSV Upload and Data Processing Project

This Django project allows users to upload CSV files, processes the data using pandas, and visualizes the data with matplotlib and seaborn. It provides functionality to display
the processed data, summary statistics, and visualizations on a web page.

## Features

- Upload CSV files.
- Display the first few rows of the data.
- Calculate and display summary statistics (mean, median, standard deviation) for numerical columns.
- Identify and display missing values.
- Generate and display basic plots (histograms) for numerical columns.

## Setup Instructions

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)
- Virtualenv (optional but recommended)
- Git

### Installation

1. Clone the Repository
git clone (https://github.com/satwik81/env1)

Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`

Follow requirements.txt file
Then run:
pip install -r requirements.txt

Set Up Django
Run the following commands to create database migrations and set up the project:
python manage.py makemigrations
python manage.py migrate

Run the Development Server
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000 to see the application.

### Project Structure
task1/ - Project settings and URLs.
app1/ - Main application directory containing models, views, forms, and templates.
templates/ - HTML templates for rendering web pages.
media/ - Directory for uploaded files.

## Usage
Upload CSV File

Choose a CSV file and click the "Upload" button.
View Processed Data and Visualizations

After uploading, you will be redirected to a page displaying the processed data, summary statistics, missing values, and generated plots.
