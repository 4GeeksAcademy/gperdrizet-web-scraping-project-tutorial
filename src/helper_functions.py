'''Helper functions for web scraping assignments.'''

import sqlite3
import matplotlib.pyplot as plt


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
