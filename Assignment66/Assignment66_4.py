def main():
    x = 2
    weight = 0.5
    bias = 0.2
    target_output = 2.0
    learning_rate = 0.1

    pred_output = (x * weight) + bias

    error = target_output - pred_output

    gradient = (pred_output - target_output) * x

    old_weight = weight

    new_weight = weight - (learning_rate * gradient)

    print("Input : ",x)
    print("Weight : ",weight)
    print("Bias : ",bias)
    print("Target Output : ",target_output)
    print("Learning Rate : ",learning_rate)

    print("\nPrediction : ",pred_output)
    print("Error : ",error)
    print("Gradient : ",gradient)

    print("\nOld Weight : ",old_weight)
    print("Updated Weight : ",new_weight)

if __name__ == "__main__":
    main()