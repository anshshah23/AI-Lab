import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class using Backpropagation
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights randomly
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.bias_output = np.zeros((1, output_size))

    def feedforward(self, X):
        # Forward pass through the network
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        return self.final_output

    def backpropagation(self, X, y, learning_rate=0.1):
        # Forward pass
        output = self.feedforward(X)
        
        # Compute error (output - target)
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)  # Gradient for output layer
        
        # Backpropagate the error to the hidden layer
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)  # Gradient for hidden layer

        # Update the weights
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs=10000, learning_rate=0.1):
        for epoch in range(epochs):
            self.backpropagation(X, y, learning_rate)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - self.feedforward(X)))
                print(f"Epoch {epoch}: Loss = {loss}")

    def predict(self, X):
        return self.feedforward(X)

# Example usage (XOR problem):
if __name__ == "__main__":
    # XOR inputs and outputs
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Initialize neural network (2 inputs, 2 hidden neurons, 1 output)
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Train the network
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the network
    print("Predictions after training:")
    for x in X:
        print(f"Input: {x}, Output: {nn.predict(x)}")
