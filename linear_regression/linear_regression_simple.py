import numpy as np
import random
import matplotlib.pyplot as plt

x = np.arange(100)
delta = np.random.uniform(-1, 10, 100)
y = 3*x + 10 + delta

plt.plot(x,y, label="Original")

weight = random.random()
bias = 10
yhat = weight*x + bias

plt.plot(x, yhat, label="Untrained Projection")


def gradient_descent(weight, bias, x, y, lr=0.000001):
    # weight:
    weight_gradient = -x*(y - weight*x-bias)
    bias_gradient = -(y-weight*x-bias)
    return weight-lr*np.sum(weight_gradient), bias-lr*np.sum(bias_gradient)
epochs = 10
for i in range(epochs):
    weight, bias = gradient_descent(weight, bias, x, y)
    yhat_1_epoch = weight*x + bias
    plt.plot(x, yhat_1_epoch, label="%i epoch training " % (i+1))

plt.legend()
plt.show()