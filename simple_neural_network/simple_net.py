import numpy as np

data = np.array([[1,1,2],
        [3,4,5],
        [6,7,8]])

ans = np.array([[4,12,21]]).T

hidden_nodes = 1000
lr = .01

def relu(x):
    return (x > 0)*x

def relu_deriv(x):
    return x > 0

weights_X_1 = 2*np.random.random((3, hidden_nodes)) - 1
weights_1_2 = 2*np.random.random((hidden_nodes, hidden_nodes)) - 1
weights_2_O = 2*np.random.random((hidden_nodes, 1)) - 1


for epoch in range(1000):
    layer_1 =  relu(data.dot(weights_X_1))
    layer_2 =  relu(layer_1.dot(weights_1_2))
    layer_3 = layer_2.dot(weights_2_O)
    
    layer_3_delta = layer_3-ans
    layer_2_delta = layer_3_delta.dot(weights_2_O.T)*(relu_deriv(layer_2))
    layer_1_delta = layer_2_delta.dot(weights_1_2.T)*(relu_deriv(layer_1))
    weights_2_O -= lr*layer_2.T.dot(layer_3_delta)
    weights_1_2 -= lr*layer_1.T.dot(layer_2_delta)
    weights_X_1 -= lr*data.T.dot(layer_1_delta)

    print("Epoch %i, loss (mse): %f, mae: %f" % (epoch+1, 0.5*np.sum((layer_3 - ans)**2)/3.0, np.sum(np.abs(layer_3 - ans))))