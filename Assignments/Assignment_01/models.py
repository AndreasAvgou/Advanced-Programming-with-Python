# File: models.py

class Tweet:
    """
    Task 3.1: Tweet Class representing a single tweet.
    """
    def __init__(self, tweet_id, user_id, text, likes):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.text = text
        self.likes = likes

    def __str__(self):
        return f"Tweet(ID: {self.tweet_id}, User: {self.user_id}, Likes: {self.likes})"

class UserManager:
    """
    Task 3.2: User Profiling Subsystem.
    Manages user statistics and calculates risks/activity.
    """
    def __init__(self, df):
        self.df = df

    def get_most_active_users(self, top_n=5):
        """
        Finds users with the most tweets.
        """
        active_users = self.df['user_id'].value_counts().head(top_n)
        return active_users

    def get_user_impact(self, user_id):
        """
        Calculates total impact (likes + retweets) for a specific user.
        """
        user_tweets = self.df[self.df['user_id'] == user_id]
        if user_tweets.empty:
            return 0
        
        impact = user_tweets['likes'].sum() + user_tweets['retweets'].sum()
        return impact