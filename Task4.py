#imports
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error 
from keras.models import Sequential
from keras.layers import Dense
#Data points from the assignment
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise
#Splitting the data points into training and testing data
X_train, X_test, y_train, y_test = train_test_split(x_data,y_data, test_size = 0.2,random_state=0)

#1.1 a, Linear regression model to predict the value of y
regression=LinearRegression()#using sklearn for linear regression
regression.fit(X_train,y_train)#fitting the model using the training data
#print("regression score for linear regression is: "+str(regression.score(X_test,y_test)))#print this for regression score
y_pred = regression.predict(X_test)#predicting the values of y given the values of X
plt.scatter(X_test, y_test, color ='b')
plt.plot(X_test, y_pred, color ='k') 
plt.title("Linear regression")
plt.show()
linear_mse=mean_squared_error(y_test,y_pred)

#1.1b polynomial model with highest power of 2
polynomial=PolynomialFeatures(degree=2)#imported from sklearn, degree is 2 as mentioned in the assignment descriptor
X_polynomial=polynomial.fit_transform(X_train)#using sklearn
X_test_polynomial=polynomial.transform(X_test)
polynomial_regression=LinearRegression()
polynomial_regression.fit(X_polynomial,y_train)#fitting the model using training data after transforming X
y_polynomial_pred=polynomial_regression.predict(X_test_polynomial)
polynomial_mse=mean_squared_error(y_test,y_polynomial_pred)
result=list(zip(X_test,y_polynomial_pred))#This is done to sort the list X test and Y predictions
sorted_tuples=sorted(result,key=lambda a: a[0])#for getting a curve to plot it instead of lines
sorted_x_test,sorted_y_polynomial_pred=zip(*sorted_tuples)
plt.scatter(X_test, y_test, color ='b')
plt.plot(sorted_x_test, sorted_y_polynomial_pred, color ='k') #note we are plotting sorted values of x not just x
plt.title("Polynomial regression")
plt.show()
#1.1c A three layer neural network to predict y_data
model = Sequential()
#first layer
model.add(Dense(units=6, input_shape=(1,), kernel_initializer='normal', activation='relu'))#this is the first layer, activation function is the rectified linear unit
#model.add(Dense(units=5, kernel_initializer='normal', activation='tanh'))#using a different activation function for the second layer
model.add(Dense(1, kernel_initializer='normal'))#third layer
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train ,batch_size = 20, epochs = 50, verbose=1)#50 epochs with a batch size of 20
y_prediction_neural = model.predict(X_test)#predicting the model
print("Neural network predictions: "+str(y_prediction_neural))
neural_mse=mean_squared_error(y_test,y_prediction_neural)
#1.1d Printing mean squared errors for the three models
print("Mean squared error for neural network is: "+str(neural_mse))
print("Mean squared error for polynomial regression is: "+str(polynomial_mse))
print("Mean squared error for linear regression is: "+str(linear_mse)) 