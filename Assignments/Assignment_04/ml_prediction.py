# File: ml_prediction.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import config
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_churn_model(df):
    """
    Task 4: Train a model to predict if a user will churn.
    """
    print("\n--- Training Churn Prediction Model ---")
    
    # Features (X) and Target (y)
    # We drop 'user_id' (not predictive) and 'churned' (target)
    # We also drop 'conversion_rate' if it was added, to avoid data leakage or keep it if computed from raw data
    features = ['sessions', 'avg_session_time', 'purchases', 'last_active_days']
    X = df[features]
    y = df['churned']
    
    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE
    )
    
    # Initialize and Train Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=config.RANDOM_STATE)
    model.fit(X_train, y_train)
    
    # Make Predictions
    y_pred = model.predict(X_test)
    
    # Evaluate
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc*100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature Importance
    plot_feature_importance(model, features)
    
    return model

def plot_feature_importance(model, feature_names):
    """
    Visualizes which features are most important for churn prediction.
    """
    importances = model.feature_importances_
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=importances, y=feature_names, palette='viridis')
    plt.title('Feature Importance for Churn Prediction')
    plt.xlabel('Importance Score')
    
    save_path = os.path.join(config.PLOTS_DIR, 'feature_importance.png')
    plt.savefig(save_path)
    plt.close()
    print(f"[Info] Saved feature importance plot to {save_path}")