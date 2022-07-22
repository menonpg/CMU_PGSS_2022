import pandas as pd
import sklearn 
import random

def simulate_random_data(n):
   """Simulate random data"""
   x1 = [random.randint(0,n) for i in range(n)]
   x2 = [random.randint(0,n) for i in range(n)]
   beta1 = random.randint(0,n)
   beta2 = random.randint(0,n)
   y  = [x1[i]*beta1 + x2[i]*beta2 for i in range(n)] 
   return pd.DataFrame ({'x1':x1, 'x2':x2, 'y':y})

def generate_data_set(csvFile):
   """Generate a data set"""
   df = pd.read_csv(csvFile)
   X = df[['x1', 'x2']]
   y = df['y']
   return X, y


def visualize_data_frame(csvFile):
   """Read a data frame from a csv file and create a boxplot""" 
   df = pd.read_csv(csvFile)
   df.boxplot()

from sklearn.linear_model import LinearRegression
def train_linear_regression(X,y):
   """Train a linear regression model"""
   lr = LinearRegression()
   lr.fit(X, y)
   return lr

def predict_linear_regression(lr, x1, x2):
   """Predict a value using a linear regression model"""
   return lr.predict([[x1, x2]])

if __name__ == "__main__":
   test_csv = "test_data.csv"

   df = simulate_random_data(10)
   df.to_csv(test_csv)
   
   visualize_data_frame(test_csv)
   X, y = generate_data_set(test_csv)

   lr = train_linear_regression(X, y)
   print(predict_linear_regression(lr, 1, 1))
   print(predict_linear_regression(lr, 1, 2))