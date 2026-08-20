import numpy as np

def main():
    Dataset = np.array([6,7,8,9,10,11,12])

    print("Dataset is : ",Dataset)

    variance = np.var(Dataset)

    standard_deviation = np.std(Dataset)

    print("Variance of Dataset : ",variance)
    print("Standard Deviation of Dataset : ",standard_deviation)

if __name__ == "__main__":
    main()