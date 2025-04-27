
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
df = pd.read_csv("C:\\project_py\\Titanic-Dataset.csv")
print("Dataset Info:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nFirst few rows:\n", df.head())
df['Age'].fillna(df['Age'].mean(), inplace=True)  
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True) 

label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

numerical_features = ['Age', 'Fare'] 

scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

for feature in numerical_features:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

for feature in numerical_features:
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[feature] >= lower_bound) & (df[feature] <= upper_bound)]


print("\nFinal dataset shape after removing outliers:", df.shape)
print(df.head())