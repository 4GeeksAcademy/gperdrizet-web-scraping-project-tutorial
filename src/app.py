''''Downloads and parses Tesela earnings by year.'''

import requests
from bs4 import BeautifulSoup

import pandas as pd
import helper_functions as helper_funcs

# Target URL
URL='https://companies-market-cap-copy.vercel.app/earnings.html'


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
    df['Earnings']=df['Earnings'].apply(helper_funcs.parse_earnings)
    df['Year']=df['Year'].apply(helper_funcs.clean_year)

    # Print the result to STDOUT
    print('\nTesla earnings:')
    print(df.head())

    # Save to an SQL database
    helper_funcs.save_to_sql(df)

    # Plot the data
    helper_funcs.plot_data(df)

    # Get the row for the most recent year and its earnings
    df=df.sort_values('Year', ascending=False)
    last_year_row=df.iloc[0]
    last_year=int(last_year_row['Year'])
    message=f'\nTesla earned ${last_year_row["Earnings"]:,.2f} in {last_year}.'

    # Display the result
    print(message)
