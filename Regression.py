import numpy as np
import math

class LinearRegression:
    def __init__(self, x,y):
        self.x = np.vstack((np.ones(len(x.T)),x))
        self.y = np.array(y)
        self.weights = np.random.random((len(self.x),1))
        self.m = len(self.y.T)

    def hypo__(self):
        return np.dot(self.weights.T,self.x)

    def fit(self,iterations=10000,learning_rate=0.01):
    	for _ in range(0,iterations):
    		error = self.__hypo() - self.y
    		gradient = self.x * error
    		self.weights = self.weights - np.array([learning_rate * np.sum(gradient,axis=1)/self.m]).T

    def predict(self,x):
    	xt = np.vstack((1,x))
    	return np.dot(self.weights.T,xt)

    def cost(self):
    	temp = np.sum(np.square(self.__hypo() - self.y))
    	return (temp/(2*self.m))


class LogisticRegression:
    def __init__(self, x,y):
        self.x = np.vstack((np.ones(len(x.T)),x))
        self.y = np.array(y)
        self.weights = np.random.random((len(self.x),1))
        self.m = len(self.y.T)

    def __hypo(self):
        return 1/(1+np.exp(-np.dot(self.weights.T,self.x)))

    def fit(self,iterations=10000,learning_rate=0.01):
    	for _ in range(0,iterations):
    		error = self.__hypo() - self.y
    		gradient = self.x * error
    		self.weights = self.weights - np.array([learning_rate * np.sum(gradient,axis=1)/self.m]).T
    		# self.bias = self.bias - (learning_rate * np.sum(d_cost) / self.m)

    def predict(self,x):
    	xt = np.vstack((1,x))
    	return ((1/(1+np.exp(-np.dot(self.weights.T,xt)))) >= 0.5)

    def cost(self):
    	t = (self.y * np.log(self.__hypo())) + ((1 - self.y) * np.log(1-self.__hypo()))
    	return -np.sum(t)/self.m




# if any erros causes just remove __ in hypo method
