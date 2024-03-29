# -*- coding: utf-8 -*-
"""Titanic Disaster Survival Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v3mFq-sdxcyP3ecil86h_T7GvjNktjB6

<h1>Titanic Disaster Survival Prediction </h1>
<h1>CodSoft-DataScience-Internship-Task-1 </h1>
"""

#import libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""**Load the Data**"""

#load data

titanic_data=pd.read_csv('/content/Titanic-Dataset.csv')

len(titanic_data)

"""**View the data using head function which returns top  rows**"""

titanic_data.head()

titanic_data.index

titanic_data.columns

titanic_data.info()

titanic_data.dtypes

titanic_data.describe()

"""**Explaining Dataset**

survival : Survival 0 = No, 1 = Yes <br>
pclass : Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd <br>
sex : Sex <br>
Age : Age in years <br>
sibsp : Number of siblings / spouses aboard the Titanic
<br>parch # of parents / children aboard the Titanic <br>
ticket : Ticket number fare Passenger fare cabin Cabin number <br>
embarked : Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton <br>

<h1>Data Analysis

**Import Seaborn for visually analysing the data**

**Find out how many survived vs Died using countplot method of seaboarn**
"""

#countplot of subrvived vs not  survived

sns.countplot(x='Survived',data=titanic_data)

"""**Male vs Female Survival**"""

#Male vs Female Survived?

sns.countplot(x='Survived',data=titanic_data,hue='Sex')

"""**See age group of passengeres travelled **<br>
Note: We will use displot method to see the histogram. However some records does not have age hence the method will throw an error. In order to avoid that we will use dropna method to eliminate null values from graph
"""

#Check for null

titanic_data.isna()

#Check how many values are null

titanic_data.isna().sum()

#Visualize null values

sns.heatmap(titanic_data.isna())

#find the % of null values in age column

(titanic_data['Age'].isna().sum()/len(titanic_data['Age']))*100

#find the % of null values in cabin column

(titanic_data['Cabin'].isna().sum()/len(titanic_data['Cabin']))*100

#find the distribution for the age column

sns.displot(x='Age',data=titanic_data)

"""<h1>Data Cleaning

**Fill the missing values**<br> we will fill the missing values for age. In order to fill missing values we use fillna method.<br> For now we will fill the missing age by taking average of all age
"""

#fill age column

titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)

"""**We can verify that no more null data exist** <br> we will examine data by isnull mehtod which will return nothing"""

#verify null value

titanic_data['Age'].isna().sum()

"""**Alternatively we will visualise the null value using heatmap**<br>
we will use heatmap method by passing only records which are null.
"""

#visualize null values

sns.heatmap(titanic_data.isna())



"""**We can see cabin column has a number of null values, as such we can not use it for prediction. Hence we will drop it**"""

#Drop cabin column

titanic_data.drop('Cabin',axis=1,inplace=True)

#see the contents of the data

titanic_data.head()

"""**Preaparing Data for Model**<br>
No we will require to convert all non-numerical columns to numeric. Please note this is required for feeding data into model. Lets see which columns are non numeric info describe method
"""

#Check for the non-numeric column

titanic_data.info()

titanic_data.dtypes

"""**We can see, Name, Sex, Ticket and Embarked are non-numerical.It seems Name,Embarked and Ticket number are not useful for Machine Learning Prediction hence we will eventually drop it. For Now we would convert Sex Column to dummies numerical values******"""

#convert sex column to numerical values

gender=pd.get_dummies(titanic_data['Sex'],drop_first=True)

titanic_data['Gender']=gender

titanic_data.head()

#drop the columns which are not required

titanic_data.drop(['Name','Sex','Ticket','Embarked'],axis=1,inplace=True)

titanic_data.head()

#Seperate Dependent and Independent variables

x=titanic_data[['PassengerId','Pclass','Age','SibSp','Parch','Fare','Gender']]
y=titanic_data['Survived']

y

"""<h1>Data Modelling

**Building Model using Logestic Regression**

**Build the model**
"""

#import train test split method

from sklearn.model_selection import train_test_split

#train test split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#import Logistic  Regression

from sklearn.linear_model import LogisticRegression

#Fit  Logistic Regression

lr=LogisticRegression()

lr.fit(x_train,y_train)

#predict

predict=lr.predict(x_test)

"""<h1>Testing

**See how our model is performing**
"""

#print confusion matrix

from sklearn.metrics import confusion_matrix

pd.DataFrame(confusion_matrix(y_test,predict),columns=['Predicted No','Predicted Yes'],index=['Actual No','Actual Yes'])

#import classification report

from sklearn.metrics import classification_report

print(classification_report(y_test,predict))

"""**Precision is fine considering Model Selected and Available Data. Accuracy can be increased by further using more features (which we dropped earlier) and/or  by using other model**

Note: <br>
Precision : Precision is the ratio of correctly predicted positive observations to the total predicted positive observations <br>
Recall : Recall is the ratio of correctly predicted positive observations to the all observations in actual class
F1 score - F1 Score is the weighted average of Precision and Recall.


"""