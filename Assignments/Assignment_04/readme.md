# 🛒 User Behavior Analysis & Churn Prediction 

This project implements a Python-based system for analyzing user behavior on online platforms. It uses **Pandas** for data manipulation, **OOP** for user profiling, and **Scikit-Learn** (Random Forest) to predict user churn.

---

## 📌 Project Overview

The goal is to process the `user_behavior_dataset.csv` file to identify patterns distinguishing active users from those who churn (leave the platform), and build a predictive model.

### Key Features:
* **Data Processing:** Load and clean user interaction logs.
* **Analytics:** Compare behavior (Sessions, Time, Purchases) between Churned vs Active users.
* **OOP Architecture:** `User` and `UserBase` classes to manage user profiles and calculate engagement scores.
* **Machine Learning:** A **Random Forest Classifier** that predicts whether a user will churn based on their activity history.
* **Visualization:** Correlation matrices and Feature Importance charts.

---

## 📂 Repository Structure
```
Assignment_4_UserBehavior/
│
├── user_behavior_dataset.csv   # Input dataset
├── main.py                     # Entry point
├── config.py                   # Settings & paths
├── data_loader.py              # Task 1: Data ingestion
├── analytics.py                # Task 2: Behavioral Analytics
├── models.py                   # Task 3: OOP Classes
├── ml_prediction.py            # Task 4: Churn Prediction (ML)
└── README.md                   # Documentation
```

## 🚀 How to Run

1.  Place `user_behavior_dataset.csv` in the project folder.
2.  Run the main script:

```bash
python main.py
```

---

### Expected Output
The script will output:
* **Behavioral Comparison:** Average purchases/sessions for Churned vs Non-Churned users.
* **OOP Insights:** Total Churn Rate calculated via the `UserBase` class.
* **Model Performance:** Accuracy score and Classification Report for the Random Forest model.
* **Plots:** Saved in `results/plots/`:
    * `correlation_matrix.png`: Heatmap of feature relationships.
    * `feature_importance.png`: Bar chart showing which factors (e.g., `last_active_days`) most affect churn.

---

## 📊 Modules Description

### 1. `data_loader.py`
Loads the CSV, removes duplicate user IDs, and handles missing values.

### 2. `analytics.py`
Calculates the **Conversion Rate** (Purchases / Sessions) and compares statistics between the two target groups (Churned=0 vs Churned=1).

### 3. `models.py`
* **`User`:** Represents a single user with methods to calculate a custom `engagement_score`.
* **`UserBase`:** Manages the list of users, allowing filtering (e.g., "High Value Users") and aggregate calculations.

### 4. `ml_prediction.py`
Trains a **Random Forest Classifier** to predict the `churned` label. It also extracts **Feature Importance** to understand *why* users leave (e.g., users inactive for many days are more likely to churn).
