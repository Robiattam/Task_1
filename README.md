In this task, I worked on cleaning and preparing the Titanic dataset for further analysis. I handled missing values, converted categorical columns into numbers, scaled some features, and also removed a few outliers to make the data more reliable.

 Loaded the dataset using pandas.
 Filled missing ages with the average age and filled missing embarkation points with the most common value.
 Converted text columns like 'Sex' and 'Embarked' into numbers using label encoding.
 Standardized 'Age' and 'Fare' to bring them onto a similar scale.
 Used boxplots to spot outliers and removed them using the IQR method.
 Finally, printed out the new shape of the dataset after cleaning.


