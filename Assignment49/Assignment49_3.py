import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    Dataset = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
        ])
    
    print("Actual Dataset : ")
    print(Dataset)

    scaler = StandardScaler()

    Scaled_Dataset = scaler.fit_transform(Dataset)

    print("Scaled Dataset : ")
    print(Scaled_Dataset)

if __name__ == "__main__":
    main()