import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_train(X, y, learning_rate=0.1, epochs=10):
    num_samples, num_features = X.shape
    weights = np.zeros(num_features)
    bias = 0
    
    for epoch in range(epochs):
        for i in range(num_samples):
            linear_output = np.dot(X[i], weights) + bias
            prediction = step_function(linear_output)
            error = y[i] - prediction
            weights += learning_rate * error * X[i]
            bias += learning_rate * error
        
        print(f"Epoch {epoch+1}: Weights = {weights}, Bias = {bias}")
    
    return weights, bias

def perceptron_predict(X, weights, bias):
    linear_output = np.dot(X, weights) + bias
    return step_function(linear_output)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # AND gate inputs
y = np.array([0, 0, 0, 1])  
weights, bias = perceptron_train(X, y, learning_rate=0.1, epochs=10)

for x in X:
    print(f"Input: {x}, Prediction: {perceptron_predict(x, weights, bias)}")
