# Imports
import numpy as np

# Each row is a training example, each column is a feature [X1, X2, X3]
X = np.array(([0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]), dtype=float)
Y = np.array(([0], [1], [1], [0]), dtype=float)


# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))


# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)


# Class definition
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)
        self.layer1 = None
        self.layer2 = None

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect weights 2 and weights 1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, Y):
        self.output = self.feedforward()
        self.backprop()


NN = NeuralNetwork(X, Y)
for i in range(1500): # trains NN 100 times
    if i % 100 == 0:
        print("for iteration # " + str(i) + "\n")
        print("Input: \n" + str(X))
        print("Actual Output: \n" + str(Y))
        print("Predicted Output: \n" + str(NN.feedforward()))
        print("Loss: \n" + str(np.mean(np.square(Y - NN.feedforward())))) # mean sum squared loss
        print("\n")

    NN.train(X, Y)
