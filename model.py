from pandas import read_csv
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Loading the Data as Pandas Dataframe
df  = read_csv('student_scores.csv')

#Preprocessing the Data according to our needs
X = df["Hours"].values.reshape(25,1)
y = df["Scores"]

#Splitting the Data into training Set(80%) and Test set(20%)
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

#Initiated the Machine Learning Model
mind = LinearRegression()

#Trained the Machine Learning Model using X_train, y_train data
mind.fit(X_train, y_train)

#Saving the Model as pickle file
dump(mind,"StudentScore.pkl")

#Loading the Data as Pandas Dataframe
df  = read_csv('student_scores.csv')

#Preprocessing the Data according to our needs
X = df["Hours"].values.reshape(25,1)
y = df["Scores"]

#Splitting the Data into training Set(80%) and Test set(20%)
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

#Initiated the Machine Learning Model
mind = LinearRegression()

#Trained the Machine Learning Model using X_train, y_train data
mind.fit(X_train, y_train)

#Saving the Model as pickle file
dump(mind,"StudentScore.pkl")
