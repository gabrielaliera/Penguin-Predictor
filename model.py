#Import required libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle


## Read the penguins csv file and load into a dataframe called df
df = pd.read_csv("C:/Users/Owner/Desktop/Project_CISB_60/data/penguins_size.csv")

#####Clean data####
df = df[df['sex']!='.']

#Drop rows containing NaN -only 2.901% of dataset
df = df.dropna()

#Map categorical data to numbers
df['sex'] = df['sex'].map({'MALE':0,'FEMALE':1})
df['island'] = df['island'].map({'Torgersen':0,'Dream':1,'Biscoe':2})

print(df.head())

#Create X and y dataframe
X = df.drop('species',axis=1)
y = df['species']

#Splitting data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=10)


#Preparing Support Vector Classifier Model
final_model = SVC(C=10,kernel='linear')
final_model.fit(X_train,y_train)

#Find y-predict
y_predict= final_model.predict(X_test)

# Saving model to disk
pickle.dump(final_model, open('model.pkl','wb'))

#Print y_predic 
print(y_predict)