# Spotify Streaming Records Web Scraping & Visualization

A hands-on project focused on web scraping, data cleaning, and exploratory data analysis of Spotify's most-streamed songs. This project demonstrates the end-to-end process of extracting real-world data, transforming it, and visualizing key insights using Python.

![Project Preview](assets/preview.png)

## Project Overview

This project guides you through scraping Spotify streaming records from Wikipedia, processing the data, and visualizing trends using **Matplotlib** and **Pandas**. You'll learn practical web scraping techniques, data wrangling, and how to communicate findings through clear visualizations in Jupyter notebooks.

Key topics covered include:

- Web scraping with `requests` and `BeautifulSoup`
- Data cleaning and transformation with `pandas`
- Storing and querying data using SQLite
- Visualizing distributions, trends, and categorical data

## Learning Objectives

### Data Acquisition & Processing
- Extract tabular data from web pages
- Clean and structure real-world datasets
- Store data in a relational database (SQLite)

### Visualization & Analysis
- Create histograms, scatter plots, and bar charts
- Analyze trends by year, month, and artist
- Interpret and communicate data-driven insights

## Getting Started

### Using GitHub Codespaces (Recommended)

Launch this project instantly in a fully configured cloud development environment:

1. Click the green "Code" button on the GitHub repository
2. Select the "Codespaces" tab
3. Click "Create codespace on main"
4. Wait for the environment to initialize (all dependencies will be installed automatically)
5. Open `src/explore.ipynb` to start the analysis

GitHub Codespaces provides a complete VS Code environment in your browser with all required extensions and packages pre-installed.

### Local Installation

#### Prerequisites

- Python 3.11+
- Jupyter Notebook or VS Code with Jupyter extension

#### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/4GeeksAcademy/gperdrizet-web-scraping-project-tutorial.git
   cd gperdrizet-web-scraping-project-tutorial
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open the project**:
   ```bash
   jupyter notebook src/explore.ipynb
   ```
   Or open the notebook files in VS Code with the Jupyter extension.

## Project Structure

```
├── assets/                 # Resources and preview images
│   └── preview.png         # Project preview image
├── data/                   # SQLite database and data files
│   └── spotify.db          # Scraped and processed data
├── src/                    # Source code and notebooks
│   ├── app.py              # (Optional) App or script entry point
│   ├── explore.ipynb       # Main analysis notebook
│   ├── solution.ipynb      # Reference solution notebook
│   └── helper_functions.py # Utility functions for scraping/cleaning
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Analysis Overview

### Data Extraction
- Scrape Spotify streaming records from Wikipedia
- Parse HTML tables and extract relevant columns

### Data Cleaning
- Remove unnecessary columns and handle missing values
- Convert data types for analysis

### Data Storage
- Save cleaned data to a local SQLite database

### Visualization & Insights
- **Stream Count Distribution**: Explore how streams are distributed among the top 100 songs
- **Release Date Trends**: Analyze how streaming popularity varies by release year and month
- **Artist Analysis**: Identify the most frequently appearing artists in the top 100

## Key Concepts Covered

### Web Scraping Best Practices
- Respectful scraping with custom headers
- Error handling for robust data extraction

### Data Analysis & Visualization
- Using pandas for data wrangling
- Creating clear, informative plots with Matplotlib
- Interpreting and communicating findings

## Sample Data

The project uses real-world data scraped from Wikipedia's "List of Spotify streaming records" page, providing up-to-date and relevant insights into music streaming trends.

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

## Educational Value

This project is ideal for:
- Learners interested in web scraping and real-world data analysis
- Data science students seeking hands-on experience
- Anyone wanting to practice data cleaning, storage, and visualization in Python

You'll gain practical skills in extracting, transforming, and visualizing data, with a focus on best practices and clear communication of insights.

