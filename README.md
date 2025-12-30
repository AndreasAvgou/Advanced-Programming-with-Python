# Advanced Programming with Python 

This repository contains a collection Python scripts developed. The projects progress from Object-Oriented Programming (OOP) principles to advanced data analysis, visualization, and real-time API integration.

## Repository Structure

The exercises are organized into 9 modules and 4 assignments, each focusing on specific advanced Python concepts:

---

### 🔹 1: Introduction to Pandas
* **Focus:** Basic DataFrame manipulation.
* **Description:** An analysis of a small retail dataset (`products_sales.csv`).
* **Key Tasks:**
    * Calculating total value per product ($Price \times Quantity$).
    * Grouping data to find average prices per category.
    * Sorting and identifying top-value products.

---

### 🔹 2: Object-Oriented Student Manager
* **Focus:** Classes, Methods, and File I/O.
* **Description:** Implementation of a `StudentManager` system to handle student records.
* **Key Features:**
    * `Student` class with attributes for grades and biographical data.
    * Methods for calculating individual and class-wide averages.
    * **CSV Import/Export** functionality with error handling.
    * *Bonus:* Visualization of class grades using `matplotlib`.

---

### 🔹 3: Sales Manager System
* **Focus:** Integrating OOP with Pandas.
* **Description:** A `SalesManager` class designed to track store transactions.
* **Key Features:**
    * Dynamic addition of sales via the `add_sale()` method.
    * Conversion of transaction objects into a Pandas DataFrame.
    * Analytics methods: `total_sales_per_category()` and `top_selling_products()`.

---

### 🔹 4: Real-World Data Analysis
* **Focus:** Data Cleaning and Exploratory Data Analysis (EDA).
* **Description:** Processing a raw e-commerce dataset (`sales_data.csv`).
* **Key Tasks:**
    * **Data Cleaning:** Handling missing values and converting date formats.
    * **Feature Engineering:** Creating new columns (e.g., Total Sales).
    * **Visualization:** Bar charts showing sales by category and country.

---

### 🔹 5: Crypto Financial Analysis (API) 🪙
* **Focus:** REST APIs, Financial Metrics, and Correlation.
* **Description:** A financial tool that fetches historical data for 5 cryptocurrencies (Bitcoin, Ethereum, etc.) using the **CoinGecko API**.
* **Key Features:**
    * Fetching 30-day historical data and resampling time-series.
    * Calculating **Daily Returns**, **Volatility**, and **Pearson Correlation**.
    * Interactive visualizations using **Plotly** (Time series & Heatmaps).

---

### 🔹 6: Flight Radar Analysis (API) ✈️
* **Focus:** Real-time Data, Geo-spatial Data, and Anomaly Detection.
* **Description:** Analysis of live aircraft data using the **OpenSky Network API**.
* **Key Features:**
    * Fetching and parsing real-time JSON data.
    * **Z-Score Analysis:** Detecting anomalies in aircraft velocity.
    * Geo-spatial filtering and Pivot Tables (Country vs. Velocity).
    * Scatter plots mapping aircraft positions (Longitude/Latitude).

---

### 🔹 7: Text Analysis & NLP 📝
* **Focus:** Modular Programming, Regex, and Natural Language Processing.
* **Description:** A text mining project analyzing public sentiment and trends using a dataset of tweets (`energy_tweets.csv`).
* **Key Features:**
    * **Modular Architecture:** Code split into 5 specialized modules (Loader, Cleaner, Analyzer, Visualizer, Main).
    * **Advanced Cleaning:** Utilizing **Regex** to strip URLs, mentions, and noise.
    * **Frequency Analysis:** Extracting trending hashtags and calculating word distributions.
    * **Visualization:** Generating bar charts for top words and hashtags using `matplotlib`.

---

### 🔹 8: Spotify Audio Analysis 🎧
* **Focus:** Descriptive Statistics, Correlation Analysis, and Visualization.
* **Description:** Analyzing a dataset of music tracks and their audio features (energy, danceability, tempo, etc.) using `data.csv`.
* **Key Features:**
    * **Data Loading:** Converting raw CSV data into a Pandas DataFrame.
    * **Statistical Analysis:** Using `.describe()` and `.corr()` to understand feature distributions.
    * **Correlation Heatmap:** Visualizing feature relationships using `seaborn`.
    * **Feature Insights:** Identifying which audio characteristics correlate most with high "Energy" tracks.
    * **Visualization:** Bar charts displaying the average intensity of each audio feature.

---

### 🔹 9: Music & Social Media Sentiment Analysis 🎵
* **Focus:** Data Merging, Sentiment Analysis (NLP), and Correlation.
* **Description:** A comprehensive project merging music data (`songs.csv`) with user reactions (`tweets.csv`) to study the impact of audio features on sentiment.
* **Key Features:**
    * **Data Cleaning:** Handling missing values in both text and numeric datasets.
    * **Sentiment Analysis:** Using **TextBlob** to calculate polarity scores for tweets.
    * **Data Merging:** Aggregating tweet sentiment by song and merging with audio features.
    * **Correlation:** Investigating if "Energy" or "Danceability" drives positive sentiment.
    * **Visualization:** Scatter plots and bar charts correlating music metrics with user opinions.

---

## 🛠️ Prerequisites & Installation

To run these scripts, you will need **Python 3.x** and the following external libraries:

```bash
pip install pandas numpy matplotlib requests plotly
```

## How to Run

Ensure you have Python installed (version 3.x is recommended).

1.  Clone the repository.
   
```bash
git clone [https://github.com/yourusername/advanced-python-labs.git](https://github.com/yourusername/advanced-python-labs.git)
```

2.  Navigate to the directory.

```bash
cd Advanced-Programming-with-Python
```

3.  Run specific exercises (ensure required CSV files are in the same directory):

```bash
python main.py
```

## 📝 Key Learning Outcomes
Through these exercises, the following concepts are demonstrated:

* Object-Oriented Design: Building robust classes to manage complex data structures.
* Data Science Stack: Proficiency with pandas for data manipulation and numpy for calculations.
* API Integration: Handling HTTP requests, parsing JSON, and dealing with rate limits.
* Data Visualization: Creating static (matplotlib) and interactive (plotly) charts.
* Statistical Analysis: Implementing correlation matrices and anomaly detection algorithms.




