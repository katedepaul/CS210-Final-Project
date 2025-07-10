import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("tweets_processed.csv")


engine = create_engine("postgresql+psycopg2://postgres:Sanasalma1@localhost:5432/mental_health_db")


df.to_sql('tweets', engine, if_exists='append', index=False)

print("Data inserted successfully!")
