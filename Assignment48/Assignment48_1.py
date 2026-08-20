def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

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

    print("Mean of X : ",mean_x)
    print("Mean of Y : ",mean_y)

    # Slope(m) = Sum((X - Xbar)(Y - Ybar)) / Sum(X - Xbar) ** 2

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    print("Slope (m) : ",m)

    # Y = mX + c
    # mean_y = 0.4 * mean_x + c
    # 3.6 = 0.4 * 3.0 + c
    # 3.6 = 1.2 + c
    # c = 3.6 - 1.2

    # c = mean_y - m * mean_x 

    c = mean_y - m * mean_x
    print("Intercept (c) : ",c)

    X = 6

    Y = 0.4 * X + 2.4
    print("Predicted Y for X = 6 is : ",Y)

if __name__ == "__main__":
    main()