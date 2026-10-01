import numpy as np
import math

def mean_squared_error(actual_y,pred_y):
    n = len(pred_y)
    total_error = 0

    for i in range(n):
        error = actual_y[i] - pred_y[i]
        total_error = total_error + (error ** 2)

    MSE = total_error / n

    return MSE 

def binary_cross_entropy(actual_y,pred_y):
    n = len(pred_y)
    total_loss = 0

    for i in range(n):
        loss = (actual_y[i] * math.log(pred_y[i]) + (1 - actual_y[i]) * math.log(1 - pred_y[i]))

    total_loss = total_loss + loss

    BCE = -total_loss / n

    return BCE

def main():
    actual_y = np.array([1,0,1,1,0])
    print("Actual Values : ",actual_y)

    pred_y = np.array([0.9,0.2,0.8,0.7,0.1])
    print("Predicted Values : ",pred_y)

    MSE = mean_squared_error(actual_y,pred_y)
    print("Mean Squared Error : ",MSE)

    BCE = binary_cross_entropy(actual_y,pred_y)
    print("Binary Cross Entropy : ",BCE)

if __name__ == "__main__":
    main()

###################################################################
#
# Mean Squared Error (MSE) is used for Regression.
# Binary Cross Entropy is used for Binary Classification.
#
###################################################################
