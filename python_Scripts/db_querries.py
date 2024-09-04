import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect('cdc_covid19_data.db')
cur = conn.cursor()

def total_deaths_by_state():
    cur.execute('''
    SELECT state, SUM(covid_19_deaths) 
    FROM covid_data
    GROUP BY state
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['state', 'total_deaths'])
    df.to_json('data/total_deaths_by_state.json', orient='records')
    print(df)

def total_deaths_by_age_group():
    cur.execute('''
    SELECT age_group, SUM(covid_19_deaths) 
    FROM covid_data
    GROUP BY age_group
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['age_group', 'total_deaths'])
    df.to_json('data/total_deaths_by_age_group.json', orient='records')
    print(df)

def total_deaths_by_gender():
    cur.execute('''
    SELECT sex, SUM(covid_19_deaths) 
    FROM covid_data
    GROUP BY sex
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['sex', 'total_deaths'])
    df.to_json('data/total_deaths_by_gender.json', orient='records')
    print(df)

def deaths_over_time():
    cur.execute('''
    SELECT start_date, SUM(covid_19_deaths) 
    FROM covid_data
    GROUP BY start_date
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['start_date', 'total_deaths'])
    df.to_json('data/deaths_over_time.json', orient='records')
    print(df)

def compare_death_causes():
    cur.execute('''
    SELECT state, SUM(covid_19_deaths), SUM(total_deaths), SUM(total_deaths - covid_19_deaths) AS other_causes
    FROM covid_data
    GROUP BY state
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['state', 'covid_deaths', 'total_deaths', 'other_causes'])
    df.to_json('data/compare_death_causes.json', orient='records')
    print(df)

def deaths_by_state_and_age_group():
    cur.execute('''
    SELECT state, age_group, SUM(covid_19_deaths) 
    FROM covid_data
    GROUP BY state, age_group
    ''')
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=['state', 'age_group', 'total_deaths'])
    df.to_json('data/deaths_by_state_and_age_group.json', orient='records')
    print(df)

def main():
    print("Total COVID-19 Deaths by State:")
    total_deaths_by_state()
    
    print("\nTotal COVID-19 Deaths by Age Group:")
    total_deaths_by_age_group()
    
    print("\nTotal COVID-19 Deaths by Gender:")
    total_deaths_by_gender()
    
    print("\nCOVID-19 Deaths Over Time:")
    deaths_over_time()
    
    print("\nComparison of Death Causes by State:")
    compare_death_causes()
    
    print("\nCOVID-19 Deaths by State and Age Group:")
    deaths_by_state_and_age_group()

if __name__ == '__main__':
    main()

conn.close()
