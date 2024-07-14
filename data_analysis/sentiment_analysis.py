import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(file_path):
    df = pd.read_csv(file_path)
    sid = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda x: sid.polarity_scores(x)['compound'])
    return df

df = analyze_sentiment('social_media_data.csv')
df.to_csv('social_media_sentiment.csv', index=False)
