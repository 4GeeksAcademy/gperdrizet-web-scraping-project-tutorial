# Spotify Streaming Records Web Scraping & Visualization

[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/gperdrizet-web-scraping-project-tutorial/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-web-scraping-project-tutorial/actions/workflows/codespaces/create_codespaces_prebuilds)

A hands-on project focused on web scraping, data cleaning, and exploratory data analysis of Spotify's most-streamed songs. This project demonstrates the end-to-end process of extracting real-world data, transforming it, and visualizing key insights using Python.

![Project Preview](assets/preview.png)


## Project Overview

This project guides you through scraping Spotify streaming records from Wikipedia, processing the data, and visualizing trends using **Matplotlib** and **Pandas**. You'll learn practical web scraping techniques, data wrangling, and how to communicate findings through clear visualizations in Jupyter notebooks.

Key topics covered include:

- Web scraping with `requests` and `BeautifulSoup`
- Data cleaning and transformation with `pandas`
- Storing and querying data using SQLite
- Visualizing distributions, trends, and categorical data

For detailed assignment instructions, see [`INSTRUCTIONS.md`](INSTRUCTIONS.md).



## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - 4Geeks students: set 4GeeksAcademy as the owner - 4Geeks pays for your codespace usage. All others, set yourself as the owner
   - Give the fork a descriptive name. 4Geeks students: I recommend including your GitHub username to help in finding the fork if you loose the link
   - Click "Create fork"
   - 4Geeks students: bookmark or otherwise save the link to your fork

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/assignment.ipynb` in the Jupyter interface
   - Follow the step-by-step instructions in the notebook

### Option 2: Local Development

1. **Prerequisites**
   - Git
   - Python >= 3.10

2. **Fork the repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - Optional: give the fork a new name and/or description
   - Click "Create fork"

3. **Clone the repository**
   - From your fork of the repository, click the green "Code" button at the upper right
   - From the "Local" tab, select HTTPS and copy the link
   - Run the following commands on your machine, replacing `<LINK>` and `<REPO_NAME>`

   ```bash
   git clone <LINK>
   cd <REPO_NAME>
   ```

4. **Set Up Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Launch Jupyter & start the notebook**
   ```bash
   jupyter notebook notebooks/assignment.ipynb
   ```

## Project Structure

```
├── .devcontainer/          # Codespace/development container configuration
├── assets/                 # Resources and preview images
│   └── preview.png         # Project preview image
│ 
├── data/                   # SQLite database and data files
│   └── spotify.db          # Scraped and processed data
│ 
├── notebooks/              # Notebooks directory
│   ├── assignment.ipynb    # Complete the assignment here
│   ├── solution.ipynb      # Reference solution
│   └── helper_functions.py # Utility functions for scraping/cleaning
│ 
├── .gitignore              # Files/directories not tracked by git
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


## Sample Data

The project uses real-world data scraped from Wikipedia's "List of Spotify streaming records" page, providing up-to-date and relevant insights into music streaming trends.


## Learning Objectives

### Data Acquisition & Processing
- Extract tabular data from web pages
- Clean and structure real-world datasets
- Store data in a relational database (SQLite)

### Visualization & Analysis
- Create histograms, scatter plots, and bar charts
- Analyze trends by year, month, and artist
- Interpret and communicate data-driven insights


## Technologies Used

- **Python 3.11**: Core programming language
- **Requests**: HTTP library for web scraping
- **BeautifulSoup**: HTML parsing and data extraction
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **SQLite**: Lightweight database for structured storage
- **Jupyter**: Interactive development environment

## Contributing

This project is designed for educational purposes. Contributions to improve the analysis, add new visualizations, or enhance explanations are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

