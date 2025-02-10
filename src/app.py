''''Downloads and parses Tesela earnings by year.'''

import sqlite3
import requests
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt

# Target URL
URL='https://companies-market-cap-copy.vercel.app/earnings.html'


def parse_earnings(value):
    '''Converts earnings to float dollar amounts.'''

    try:
        value=value.replace(',', '').replace('$', '').strip()

        if "Billion" in value:
            return float(value.replace('Billion', '')) * 1_000_000_000

        elif "Million" in value:
            return float(value.replace('Million', '')) * 1_000_000

        elif "M" in value:
            return float(value.replace('M', '')) * 1_000_000

        elif "B" in value:
            return float(value.replace('B', '')) * 1_000_000_000

        else:
            return float(value)

    except ValueError:
        print(f'Warning: Could not convert the value "{value}". Setting it as NaN.')

        return float('nan')


def clean_year(value):
    '''Cleans up year value.'''

    try:
        return int(value.split()[0])
    except ValueError:
        print(f'Warning: Could not process the year value "{value}". Setting it as NaN.')
        return float('nan')


def save_to_sql(data_df):
    '''Saves parsed table in SQL database.'''

    # Connect to SQLite and save the data
    conn=sqlite3.connect('../data/tesla_revenues.db')
    cursor=conn.cursor()

    # Create table in SQLite
    _=cursor.execute("""
    CREATE TABLE IF NOT EXISTS revenue (
        year TEXT,
        earnings REAL
    )
    """)

    # Insert data into the database
    for _, data_row in data_df.iterrows():
        cursor.execute(
            'INSERT INTO revenue (year, earnings) VALUES (?, ?)',
            (data_row['Year'],
            data_row['Earnings'])
        )

    conn.commit()
    conn.close()


def plot_data(data_df):
    '''Plots timeseries of Tesla earning, saves plot as jpg.'''

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(data_df['Year'], data_df['Earnings'], marker='o', color='red', label='Revenue')
    plt.title('Tesla annual revenue')
    plt.xlabel('Year')
    plt.ylabel('Revenue (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save and display the chart
    plt.savefig('../data/revenue_plot.png')


if __name__ == "__main__":

    # Make the request to the page
    try:
        response=requests.get(URL, timeout=5)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f'\nCaught requests exception error: {e}')

    print(f'\nServer response: {response.status_code}')

    # Save the HTML as text
    with open('../data/earnings.html', 'w', encoding='UTF-8') as file:
        file.write(response.text)

    # Parse the HTML content
    html=BeautifulSoup(response.text, 'html.parser')

    # Extract the annual earnings table
    table=html.find('table', {'class': 'table'})
    rows=table.find_all('tr')[1:]

    # Extract data and convert it into lists
    data=[]

    for row in rows:
        columns=row.find_all('td')
        year=columns[0].text.strip()
        earnings=columns[1].text.strip()
        data.append({'Year': year, 'Earnings': earnings})

    # Create a DataFrame with the data
    df=pd.DataFrame(data)
    df['Earnings']=df['Earnings'].apply(parse_earnings)
    df['Year']=df['Year'].apply(clean_year)

    # Print the result to STDOUT
    print('\nTesla earnings:')
    print(df.head())

    # Save to an SQL database
    save_to_sql(df)

    # Plot the data
    plot_data(df)

    # Get the row for the most recent year and its earnings
    df=df.sort_values('Year', ascending=False)
    last_year_row=df.iloc[0]
    last_year=int(last_year_row['Year'])
    message=f'\nTesla earned ${last_year_row["Earnings"]:,.2f} in {last_year}.'

    # Display the result
    print(message)
