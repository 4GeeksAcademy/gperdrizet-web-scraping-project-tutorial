'''Helper functions for web scraping and data processing.'''

def extract_table_data(table):
    """
    Extracts data from a BeautifulSoup table object and returns a list of rows.
    Song titles are extracted from <th> tags (with <a> if present),
    and other columns from <td> tags.
    """

    results = []

    data_rows = table.find_all('tr')[1:]

    for data_row in data_rows:
        values = []

        for tag in data_row:
            if tag.name == 'th':
                link = tag.find('a')

                if link:
                    title = link.get_text().strip()

                else:
                    title = None

                values.append(title)

            elif tag.name == 'td':
                values.append(tag.get_text().strip())

        results.append(values)

    return results