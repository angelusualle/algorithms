import numpy as np

data = np.array([[1,1,2],
        [3,4,5],
        [6,7,8]])

ans = np.array([[4,12,21]]).T

hidden_nodes = 4
lr = 100

def relu(x):
    return (x > 0)*x

def relu_deriv(x):
    return x > 0

weights_X_1 = 2*np.random.random((3, hidden_nodes)) - 1
weights_1_O = 2*np.random.random((hidden_nodes, 1)) - 1

for epoch in range(100):
    layer_1 =  relu(data.dot(weights_X_1))
    layer_2 =  layer_1.dot(weights_1_O)
    
    layer_2_delta = layer_2-ans
    layer_1_delta = layer_2_delta.dot(weights_1_O.T)*(relu_deriv(layer_1))
    weights_1_O -= lr*layer_1.T.dot(layer_2_delta)
    weights_X_1 -= lr*data.T.dot(layer_1_delta)

    print("Epoch %i, loss (mse): %f" % (epoch+1, np.sum((layer_2 - ans)**2)))