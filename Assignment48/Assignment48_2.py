def main():
    border = "-"*50

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(border)

    print("Independent Variables : ",X)
    print("Dependent Variables : ",Y)

    n = len(X)

    sum_x = 0
    sum_y = 0

    mean_x = 0
    mean_y = 0
    
    for i in X:
        sum_x = sum_x + i

    for i in Y:
        sum_y = sum_y + i

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print(border)

    print("Mean of X : ",mean_x)
    print("Mean of Y : ",mean_y)

    print(border)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    
    print("Slope (m) : ",m)
    print(border) 

    c = mean_y - m * mean_x

    print("Intercept (c) : ",c)
    print(border)

    for i in range(len(X)):
        Y_pred = m * X[i] + c
        print(f"For {X[i]} the predicted Y is : {Y_pred}")
    
    print(border)

    SS_res = 0

    for i in range(len(Y)):
        SS_res = SS_res + ((Y[i] - Y_pred) ** 2)

    MSE = 1 / n * SS_res

    print("Mean Squared Error (MSE) : ",MSE)
    print(border)

    SS_tot = 0

    for i in range(len(Y)):
        SS_tot = SS_tot + ((Y[i] - mean_y) ** 2)

    R2 = 1 - (SS_res / SS_tot)

    print("R2 Score : ",R2)
    print(border)

if __name__ == "__main__":
    main()