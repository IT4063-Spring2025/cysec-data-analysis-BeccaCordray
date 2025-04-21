import pandas as pd

df = pd.read_csv('data/UNSW-NB15.csv',)
dfDummies = pd.get_dummies(df, columns=[col for col in df.select_dtypes(include=['object', 'category']).columns if col != 'class'], drop_first=True)
