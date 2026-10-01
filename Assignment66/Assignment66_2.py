import numpy as np
import matplotlib.pyplot as plt
import math 

def Sigmoid(input):
    return 1 / (1 + np.exp(-input))

def ReLU(input):
    return np.maximum(0,input)

def Tanh(input):
    return np.tanh(input)

def main():
    inputs = np.linspace(-10,10,1000)

    y_sigmoid = Sigmoid(inputs)
    y_relu = ReLU(inputs)
    y_tanh = Tanh(inputs)

    plt.figure(figsize=(7,5))
    plt.plot(inputs,y_sigmoid)
    plt.title("Sigmoid Activation Function")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(inputs,y_relu)
    plt.title("ReLU Activation Function")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(inputs,y_tanh)
    plt.title("Tanh Activation Function")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

####################################################################
#
# Sigmoid Activation Function ->
#
# Output Range : 0 to 1
# Mainly used in binary classification output.
# Converts values into probability like values.
#
####################################################################
#
# ReLU Activation Function ->
# 
# Output Range : 0 to infinity
# Commonly used in hidden layers of neural networks
# Negative values become 0.
# Positive values remain same.
#
####################################################################
# 
# Tanh Activation Function ->
# 
# Output Range : -1 to +1
# Commonly used in some neural network architectures.
# Zero centered.
#
####################################################################

