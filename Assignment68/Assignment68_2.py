import numpy as np

def main():
    feature_map = np.array([
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ])
    
    relu = []

    for row in feature_map:
        new_row = []
        
        for x in row:
            if x < 0:
                x = 0

            new_row.append(x)
                
        relu.append(new_row)

    print("After ReLU:\n")
    for row in relu:
        print(np.int64(row))

    pool = []

    for i in range(2):
        row = []
        
        for j in range(2):
            maximum = max(
                relu[i][j],
                relu[i][j+1],
                relu[i+1][j],
                relu[i+1][j+1]
                )
            
            row.append(maximum)
            
        pool.append(np.int64(row))

    print("\nAfter Max Pooling:\n")
    for row in pool:
        print(row)

if __name__ == "__main__":
    main()

###########################################################
#
# Pooling reduces the size of a feature map by summarizing a group of values into a single value.
# In max pooling, the maximum value from each pooling region is selected. 
# This reduces computation and retains the important features.
#
###########################################################