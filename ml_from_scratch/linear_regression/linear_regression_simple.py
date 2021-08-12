import numpy as np

coefficients = np.random.random((5,1))
bias = np.random.random(1)
input_vals = np.random.random((1000, 5))
output = np.dot(input_vals, coefficients)+ bias

def mse(estimate, true):
    return sum((estimate - true)**2) / len(estimate)

assert mse(output, output) == 0

estimated_coefficients = np.random.random((5, 1))
estimated_bias = np.random.random(1)

output_estimated = np.dot(input_vals, estimated_coefficients) + bias

mse_ = mse(output_estimated, output)

learning_rate = 0.01

while mse_ > 0.00001:
    estimated_coefficients -= (learning_rate*sum((output_estimated - output) * input_vals)/ len(output) * 2).reshape((5,1))
    bias -= (learning_rate*sum(output_estimated - output)/ len(output) * 2)
    output_estimated = np.dot(input_vals, estimated_coefficients) + bias

    mse_ = mse(output_estimated, output)
    print(mse_)

print(coefficients)
print(estimated_coefficients)