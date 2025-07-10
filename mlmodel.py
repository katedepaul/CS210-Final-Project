import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


engine = create_engine("postgresql+psycopg2://postgres:Sanasalma1@localhost:5432/mental_health_db")


df = pd.read_sql("SELECT * FROM tweets", engine)


X = df[['text_length', 'hour_of_day']]
y = df['sentiment_label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))


plt.figure(figsize=(6, 4))
df['sentiment_label'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.savefig("sentiment_distribution_plot.png")
plt.show()

import matplotlib.pyplot as plt

print(df['hour_of_day'].value_counts())


line_data = df.groupby('hour_of_day')['text_length'].mean().reset_index()
plt.figure(figsize=(8,5))
plt.plot(line_data['hour_of_day'], line_data['text_length'], marker='o', linestyle='-')
plt.title("Avg Tweet Length by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Avg Text Length")
plt.xticks(range(0, 24))
plt.grid(True)
plt.tight_layout()
plt.show()
