import numpy as np

def convolution(image,kernel):

    feature_map = []

    for i in range(3):
        row = []

        for j in range(3):
            result = (
                image[i][j] * kernel[0][0] +
                image[i][j+1] * kernel[0][1] +
                image[i][j+2] * kernel[0][2] +

                image[i+1][j] * kernel[1][0] +
                image[i+1][j+1] * kernel[1][1] +
                image[i+1][j+2] * kernel[1][2] +

                image[i+2][j] * kernel[2][0] +
                image[i+2][j+1] * kernel[2][1] +
                image[i+2][j+2] * kernel[2][2]
            )

            row.append(result)

        feature_map.append(row)

    print("\nFeature Map : \n")
    for row in feature_map:
        print(np.int64(row))

def main():
    image = np.array([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ])

    print("Input Image : \n")
    print(image)

    kernel = np.array([
        [-1,-1,-1],
        [0,0,0],
        [1,1,1]
    ])

    print("\nKernel : \n")
    print(kernel)

    convolution(image,kernel)

if __name__ == "__main__":
    main()