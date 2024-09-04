import pandas as pd
import requests
import sqlite3

# Fetch data from the CDC API
url = "https://data.cdc.gov/resource/9bhg-hcku.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    print(df.head())
else:
    print("Failed to retrieve data:", response.status_code)

# Convert date columns to datetime
df['data_as_of'] = pd.to_datetime(df['data_as_of'])
df['start_date'] = pd.to_datetime(df['start_date'])

# Convert numeric columns
numeric_columns = ['covid_19_deaths', 'total_deaths', 'pneumonia_deaths', 
                   'pneumonia_and_covid_19_deaths', 'influenza_deaths', 
                   'pneumonia_influenza_or_covid']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Fill NaN values in numeric columns with 0
df[numeric_columns] = df[numeric_columns].fillna(0)

# Drop unnecessary columns
df_cleaned = df.drop(columns=['footnote'])

# Export to JSON
df_cleaned.to_json('cdc_covid19_data.json', orient='records', lines=True)

# Export to CSV
df_cleaned.to_csv('cdc_covid19_data.csv', index=False)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('cdc_covid19_data.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS covid_data (
        data_as_of TEXT,
        start_date TEXT,
        end_date TEXT,
        state TEXT,
        sex TEXT,
        age_group TEXT,
        covid_19_deaths INTEGER,
        total_deaths INTEGER,
        pneumonia_deaths INTEGER,
        pneumonia_and_covid_19_deaths INTEGER,
        influenza_deaths INTEGER,
        pneumonia_influenza_or_covid INTEGER
    )
''')

# Insert data into the table
df_cleaned.to_sql('covid_data', conn, if_exists='replace', index=False)

# Commit changes and close connection
conn.commit()
conn.close()

# Display cleaned data
print(df_cleaned.head())
