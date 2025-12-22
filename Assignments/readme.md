# 🐍 Advanced Programming with Python: Assignments

This repository contains a collection of four distinct data science and software engineering projects developed for the **"Advanced Programming with Python"** .

Each project focuses on specific domains—Social Media, Music Analytics, Finance, and E-commerce behavior—demonstrating proficiency in **Modular Programming**, **Object-Oriented Design (OOP)**, **Data Analysis (Pandas)**, and **Machine Learning (Scikit-Learn)**.

---

## 📂 Repository Structure

The repository is organized into four separate folders, one for each assignment:

```text
/
├── Assignment_1/         # Social Media Trend Analysis
├── Assignment_2/         # Music Library & Genre Analytics
├── Assignment_3_/        # Portfolio Management & Forecasting
└── Assignment_4/         # User Churn Prediction (ML)
```

## 🛠️ Prerequisites & Installation

All projects require **Python 3.x**. To run all assignments, install the common dependencies listed below:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## 📝 Project Summaries

### 🐦 Assignment 1: Twitter Trend Analysis Platform
**Goal:** Analyze social media interactions to identify trending hashtags and active users.

* **Key Concepts:** Data Cleaning, OOP for User Profiling, Time-series visualization.
* **Core Logic:**
    * **`Tweet` & `UserManager` Classes:** Model the relationship between users and their content.
    * **Trend Detection:** Algorithms to count and rank hashtags.
* **Input:** `ex1_twitter_dataset.csv`

### 🎵 Assignment 2: Music Data Analysis System
**Goal:** Analyze a music library to understand genre characteristics and artist popularity.

* **Key Concepts:** Audio Feature Analysis (Tempo, Energy), OOP for Library Management.
* **Core Logic:**
    * **`MusicLibrary` Class:** Manages collections of `Track` objects.
    * **Correlations:** Visualizing the relationship between a song's energy and its popularity.
* **Input:** `ex2_music_dataset.csv`

### 📈 Assignment 3: Automated Investment Portfolio Management
**Goal:** Manage financial assets, optimize investment weights based on risk, and forecast prices.

* **Key Concepts:** Financial Metrics (Volatility, Rolling Averages), Portfolio Optimization, Linear Regression.
* **Core Logic:**
    * **Risk Management:** Detecting high-volatility periods.
    * **Optimization:** Determining portfolio weights using **Inverse Volatility**.
    * **Forecasting:** Using **Linear Regression** to predict asset prices for the next 5 days.
* **Input:** `finance_dataset.csv`

### 🛒 Assignment 4: User Behavior & Churn Prediction
**Goal:** Analyze user activity on an online platform and predict which users are likely to stop using the service (Churn).

* **Key Concepts:** E-commerce metrics (Conversion Rate), Feature Importance, Classification.
* **Core Logic:**
    * **OOP Profiling:** `UserBase` class to calculate engagement scores.
    * **Machine Learning:** Training a **Random Forest Classifier** to predict user churn.
    * **Feature Importance:** Identifying why users leave (e.g., inactivity vs. low purchases).
* **Input:** `user_behavior_dataset.csv`

## 🚀 How to Run

Each assignment is self-contained. To run a specific project:

1.  **Navigate** to the assignment directory.
2.  **Ensure the dataset** is present in that folder.
3.  **Run** the `main.py` script.

**Example for Assignment 4:**
```bash
cd Assignment_4_UserBehavior
python main.py
```

### 📊 Expected Outputs
* **Console:** Statistical summaries, top lists, model accuracy scores, and OOP object demonstrations.
* **Files:** Processed data and plots are saved in the `results/` directory within each assignment folder (e.g., `results/plots/correlation_matrix.png`).

---

## 👨‍💻 Technical Implementation Details

All projects follow a strict **Modular Architecture**:

* **`config.py`**: Global settings and directory management.
* **`data_loader.py`**: Data ingestion, cleaning, and preprocessing.
* **`analytics.py`**: Statistical analysis and feature extraction.
* **`models.py`**: Object-Oriented classes (e.g., `User`, `Asset`, `Track`).
* **`visualizer.py` / `forecasting.py`**: Plotting utilities and Machine Learning logic.
* **`main.py`**: The orchestrator script that ties all modules together.
