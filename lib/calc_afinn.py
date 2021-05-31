from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


class YourSentiment:

    def __init__(self, data):
        self.data = data
        self.posts_df = ''
        self.avg_sentiment = ''
        self.get_affinity()
        self.final_affinity()

    def get_affinity(self):

        analyzer = SentimentIntensityAnalyzer()
        self.posts_df = pd.DataFrame(self.data)
        sentiment = self.posts_df[0].apply(analyzer.polarity_scores)
        self.avg_sentiment = pd.DataFrame(sentiment.tolist())
        self.avg_sentiment = float(self.avg_sentiment['compound'].mean())
        self.avg_sentiment = self.avg_sentiment * 100

    def final_affinity(self):

        if self.avg_sentiment > 0:
            print(f"Your posts are {self.avg_sentiment:.2f}% positive!")
        elif self.avg_sentiment < 0:
            print(f"Your posts are {self.avg_sentiment:.2f}% negative!")
        else:
            print(f"Your posts are very neutral!")











