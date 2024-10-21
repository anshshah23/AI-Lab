import numpy as np

# Step function to determine the output
def step_function(x):
    return 1 if x >= 0 else 0

# Perceptron learning algorithm
def perceptron_train(X, y, learning_rate=0.1, epochs=10):
    # X is the input matrix (each row is an example), y is the label vector
    num_samples, num_features = X.shape
    weights = np.zeros(num_features)
    bias = 0
    
    for epoch in range(epochs):
        for i in range(num_samples):
            # Compute the weighted sum of inputs
            linear_output = np.dot(X[i], weights) + bias
            prediction = step_function(linear_output)
            
            # Update weights if there is an error
            error = y[i] - prediction
            weights += learning_rate * error * X[i]
            bias += learning_rate * error
        
        print(f"Epoch {epoch+1}: Weights = {weights}, Bias = {bias}")
    
    return weights, bias

# Predict function
def perceptron_predict(X, weights, bias):
    linear_output = np.dot(X, weights) + bias
    return step_function(linear_output)

# Example usage:
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # AND gate inputs
y = np.array([0, 0, 0, 1])  # AND gate outputs

# Train the perceptron
weights, bias = perceptron_train(X, y, learning_rate=0.1, epochs=10)

# Test the perceptron
for x in X:
    print(f"Input: {x}, Prediction: {perceptron_predict(x, weights, bias)}")
