import numpy as np
import math
from sklearn.preprocessing import StandardScaler

def main():
    Dataset = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
        ])
    
    print("Actual Dataset : ")
    print(Dataset)

    p1 = Dataset[0]
    p2 = Dataset[2]

    distance_before = math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

    print("Eucledian Distance before applying Feature Scaling : ")
    print(distance_before)

    scaler = StandardScaler()

    Scaled_Dataset = scaler.fit_transform(Dataset)

    print("Scaled Dataset : ")
    print(Scaled_Dataset)

    p1 = Scaled_Dataset[0]
    p2 = Scaled_Dataset[2]

    distance_after = math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

    print("Eucledian Distance after applying Feature Scaling : ")
    print(distance_after)

if __name__ == "__main__":
    main()


######################################################################
#
#  Before scaling the salary values are very large,so they affect the distance more.
#  After scaling both features are brought to a same range.
#  This makes the distance calculation more balanced.
#  Scaling is important for algorithm like KNN, which use distance.
#  Scaling helps the model give fair importance to all features.
#
######################################################################
