# 🐦 Twitter Trend Analysis Platform

This project implements a Python-based platform for analyzing social media trends using a Twitter dataset. It leverages **Pandas** for data manipulation, **Object-Oriented Programming (OOP)** for user profiling, and **Matplotlib/Seaborn** for data visualization.

---

## 📌 Project Overview

The goal of this assignment is to process a dataset of tweets (`twitter_dataset.csv`) and extract meaningful insights regarding user activity and trending topics.

### Key Features:
* **Data Handling:** Efficient loading and cleaning of CSV data using Pandas.
* **Analytics:** Calculation of total tweets, unique users, engagement metrics (likes/retweets), and trending hashtags.
* **OOP Architecture:** Implementation of `Tweet` and `UserManager` classes to model data entities and calculate user impact.
* **Visualization:** Generation of charts for daily activity trends and top hashtags.

---

## 📂 Repository Structure

The project follows a modular architecture:
```
Assignment_1_Twitter/
│
├── twitter_dataset.csv         # The dataset file (Input)
├── main.py                     # Main execution script
├── config.py                   # Configuration settings (paths)
├── data_loader.py              # Task 1: Loading & Cleaning data
├── analytics.py                # Task 2: Statistical Analysis
├── models.py                   # Task 3: OOP Classes (Tweet, UserManager)
├── visualizer.py               # Task 4: Plotting & Visualization
└── README.md                   # Project documentation
```

## ⚙️ Prerequisites & Installation

To run this project, you need **Python 3.x** and the following libraries:

```bash
pip install pandas matplotlib seaborn
```

## 🚀 How to Run

1.  **Clone or Download** the repository.
2.  Ensure `twitter_dataset.csv` is in the same directory as the Python scripts.
3.  Run the main script:

```bash
python main.py
```

### Expected Output
Upon execution, the script will:
* Print basic statistics (Total tweets, likes, retweets) to the console.
* Display the top trending hashtags.
* Show the most active users and create sample OOP objects.
* Generate and save plots in the `results/plots/` directory.

---

## 📊 Modules Description

### 1. `data_loader.py`
Handles the ingestion of the CSV file. It performs cleaning operations such as:
* Removing duplicate tweets.
* Handling missing values in hashtags.
* Converting date columns to `datetime` objects.

### 2. `analytics.py`
Performs core data analysis tasks:
* **Basic Stats:** Total volume of interaction.
* **Trending:** Identifying the top 5 most frequent hashtags.

### 3. `models.py`
Implements the Object-Oriented design:
* **`Tweet` Class:** Represents an individual tweet entity.
* **`UserManager` Class:** Manages user-centric operations, such as finding the most active users and calculating "User Impact" based on their engagement metrics.

### 4. `visualizer.py`
Uses `matplotlib` and `seaborn` to create:
* **Daily Activity Plot:** A line chart showing tweet volume over time.
* **Top Hashtags Plot:** A bar chart visualizing the most popular topics.

---

## 📈 Results

After running the program, check the `results/plots/` folder for:
* **`daily_activity.png`**: Visualizes how tweet volume changes over time.
* **`top_hashtags.png`**: Shows the most discussed topics in the dataset.
