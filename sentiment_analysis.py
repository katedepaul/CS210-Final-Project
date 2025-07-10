import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Load tweets
df = pd.read_csv('tweets_raw.csv')

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Sentiment score & label
def get_sentiment_label(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

df['sentiment_score'] = df['text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

# Feature engineering
df['text_length'] = df['text'].apply(lambda x: len(str(x)))
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
df['hour_of_day'] = df['created_at'].dt.hour

# Plot sentiment distribution
sns.set_style('whitegrid')
sns.countplot(data=df, x='sentiment_label', palette='coolwarm')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()

# Save processed data
df.to_csv('tweets_processed.csv', index=False)
print(df.head())
print("Finished! Output saved to tweets_processed.csv")
