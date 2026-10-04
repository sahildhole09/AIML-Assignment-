import numpy as np

def main():
    matrix = np.array([
        [6,4],
        [8,6]
    ])
    
    print("Input Matrix : \n")
    print(matrix)

    flatten = matrix.flatten()

    print("\nFlatten Output : ")
    print(flatten)

    weights = np.array([1,1,1,1])
    print("\nWeights to respective inputs : ")
    print(weights)

    bias = 1
    print("\nBias : ")
    print(bias)

    Output = np.sum(flatten * weights) + bias

    print("\nFinal Output : ")
    print(Output)

if __name__ == "__main__":
    main()