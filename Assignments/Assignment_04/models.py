# File: models.py

class User:
    """
    Task 3.1: User Class representing a platform user.
    """
    def __init__(self, user_id, sessions, avg_time, purchases, churned):
        self.user_id = user_id
        self.sessions = sessions
        self.avg_time = avg_time
        self.purchases = purchases
        self.churned = bool(churned)

    def get_engagement_score(self):
        """
        Custom metric: Engagement = (Sessions * Time) + (Purchases * 10)
        """
        return (self.sessions * self.avg_time) + (self.purchases * 10)

    def __str__(self):
        status = "Churned" if self.churned else "Active"
        return f"User {self.user_id} | {status} | Purchases: {self.purchases}"

class UserBase:
    """
    Task 3.2: Manager class for user collection.
    """
    def __init__(self):
        self.users = []

    def load_users(self, df):
        for _, row in df.iterrows():
            user = User(
                row['user_id'],
                row['sessions'],
                row['avg_session_time'],
                row['purchases'],
                row['churned']
            )
            self.users.append(user)

    def get_high_value_users(self, min_purchases=10):
        """
        Returns users with more than N purchases.
        """
        return [u for u in self.users if u.purchases >= min_purchases]
    
    def get_churn_rate(self):
        """
        Calculates percentage of churned users.
        """
        if not self.users: return 0.0
        churned_count = sum(1 for u in self.users if u.churned)
        return (churned_count / len(self.users)) * 100