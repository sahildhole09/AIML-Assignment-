import numpy as np
import math

def Sigmoid(z):
    return 1 / (1 + math.exp(-z))

def main():
    Inputs = np.array([2,3])
    print("Inputs : ",Inputs)

    Weights = np.array([0.4,0.6])
    print("Weights : ",Weights)

    Bias = 0.5
    print("Bias : ",Bias)

    z = np.dot(Inputs,Weights) + Bias
    print("Weighted Sum : ",z)

    output = Sigmoid(z)

    print("Final Output : ",output)

    if output < 0.5 :
        print("Output is close to 0")
    else:
        print("Output is close to 1")

if __name__ == "__main__":
    main()
