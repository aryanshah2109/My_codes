import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

def gradientDescent(x,y):
    mCurrent = 0
    bCurrent = 0
    iteration = 10
    n = len(x)
    learningRate = 0.01
    for i in range(iteration):
        yPredicted = mCurrent * x + bCurrent
        costFunction = (1/n) * sum([val**2 for val in (y-yPredicted)])
        mDerivative = (-2/n) * sum(x*(y-yPredicted))
        bDerivative = (-2/n) * sum(y-yPredicted)
        mCurrent = mCurrent - learningRate * mDerivative
        bCurrent = bCurrent - learningRate * bDerivative
        print(f"m {mCurrent} , b {bCurrent} , cost Function {costFunction}, iteration {i}")
        
    

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradientDescent(x,y)