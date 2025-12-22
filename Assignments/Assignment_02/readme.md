# 🎵 Music Data Analysis System

This project implements a Python-based system for analyzing music datasets. It provides functionality for cleaning data, calculating statistics per genre and artist, managing a music library using **OOP principles**, and generating visual insights.

---

## 📌 Project Overview

The goal is to process the `music_dataset.csv` file to extract insights about musical trends, such as the correlation between energy and popularity, and the distribution of genres.

### Key Features:
* **Data Processing:** Clean and normalize music track data.
* **Analytics:** Compute average tempo/energy per genre and identify top artists.
* **OOP Architecture:** `Track` and `MusicLibrary` classes to manage collections of songs programmatically.
* **Visualization:** Generate charts for genre distribution and attribute correlations.

---

## 📂 Repository Structure
```
Assignment_2_Music/
│
├── music_dataset.csv       # Input dataset
├── main.py                 # Entry point
├── config.py               # Settings & paths
├── data_loader.py          # Task 1: Data ingestion
├── analytics.py            # Task 2: Statistical Analysis
├── models.py               # Task 3: OOP Classes
├── visualizer.py           # Task 4: Plotting
└── README.md               # Documentation
```

---

## ⚙️ Prerequisites

* Python 3.x
* Libraries: `pandas`, `matplotlib`, `seaborn`

To install dependencies:
```bash
pip install pandas matplotlib seaborn
```

## 🚀 How to Run

1.  Place `music_dataset.csv` in the project folder.
2.  Run the main script:

```bash
python main.py
```

### Expected Output
The script will output:
* **Genre Statistics:** Average tempo, energy, and popularity per genre.
* **Top Artists:** A list of artists with the highest average popularity.
* **OOP Insights:** The top 3 most energetic tracks managed by the `MusicLibrary` class.
* **Plots:** Saved in `results/plots/`:
    * `genre_distribution.png`
    * `energy_vs_popularity.png`

---

## 📊 Modules Description

### 1. `data_loader.py`
Responsible for loading the CSV and ensuring data quality (e.g., clipping energy values to [0,1], filtering valid release years).

### 2. `analytics.py`
Contains functions to group data by genre or artist and compute aggregate metrics (mean, count).

### 3. `models.py`
* **`Track`:** A class representing a single song with attributes like artist, genre, and energy.
* **`MusicLibrary`:** A manager class that holds a list of `Track` objects and provides methods to filter or sort them.

### 4. `visualizer.py`
* **Genre Distribution:** A count plot showing how many tracks belong to each genre.
* **Energy vs Popularity:** A scatter plot to visualize if energetic songs tend to be more popular.
