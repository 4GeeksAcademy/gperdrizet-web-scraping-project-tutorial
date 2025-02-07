'''Downloads and parses Tesela earnings by year.'''

import requests
import sqlite3
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt

# Target URL
URL="https://companies-market-cap-copy.vercel.app/earnings.html"


def parse_earnings(value):
    '''Converts earnings to dollar amounts.'''

    try:
        value=value.replace(",", "").replace("$", "").strip()

        if "Billion" in value:
            return float(value.replace("Billion", "")) * 1_000_000_000

        elif "Million" in value:
            return float(value.replace("Million", "")) * 1_000_000

        elif "M" in value:
            return float(value.replace("M", "")) * 1_000_000

        elif "B" in value:
            return float(value.replace("B", "")) * 1_000_000_000

        else:
            return float(value)

    except ValueError:
        print(f"Warning: Could not convert the value '{value}'. Setting it as NaN.")

        return float("nan") 


def clean_year(value):
    '''Cleans up year value.'''

    try:
        return int(value.split()[0]) 
    except ValueError:
        print(f"Warning: Could not process the year value '{value}'. Setting it as NaN.")
        return float("nan")


def save_to_sql(df):
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
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO revenue (year, earnings) VALUES (?, ?)", (row["Year"], row["Earnings"])
        )

    conn.commit()
    conn.close()


def plot_data(df):
    '''Plots timeseries of Tesla earning, saves plot as jpg.'''

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df["Year"], df["Earnings"], marker='o', color='red', label="Revenue")
    plt.title("Tesla annual revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save and display the chart
    plt.savefig('../data/revenue_plot.png')

if __name__ == "__main__":
    '''Main function to do data retreival and parsing'''

    # Make the request to the page
    response=requests.get(URL)
    response.raise_for_status() 

    # Parse the HTML content
    html=BeautifulSoup(response.text, "html.parser")

    # Extract the annual earnings table
    table=html.find("table", {"class": "table"}) 
    rows=table.find_all("tr")[1:] 

    # Extract data and convert it into lists
    data=[]

    for row in rows:
        columns=row.find_all("td")
        year=columns[0].text.strip() 
        earnings=columns[1].text.strip()  
        data.append({"Year": year, "Earnings": earnings})

    # Create a DataFrame with the data
    df=pd.DataFrame(data)
    df["Earnings"]=df["Earnings"].apply(parse_earnings)
    df["Year"]=df["Year"].apply(clean_year)
    print(df.head())

    # Save to an SQL database
    save_to_sql(df)

    # Plot the data
    plot_data(df)

    # Get the row for the most recent year and its earnings
    df=df.sort_values("Year", ascending=False)
    last_year_row=df.iloc[0]
    last_year=int(last_year_row["Year"])
    message=f"Tesla has generated ${last_year_row['Earnings']:,.2f} in earnings in the year {last_year}."

    # Display the result
    print(message)