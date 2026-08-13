import math

def EUCDistance(P1,P2):
    Dist = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Dist

def KNNClassifier(X,Y):
    Data = [
        {'Point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'Point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'Point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'}
    ]

    border = "-"*40

    print(border)
    print("Dataset is :")
    print(border)
    for d in Data:
        print(d)
    print(border)

    print("New Data Point :")
    new_point = {'X' : X, 'Y' : Y}

    print(border)
    print(new_point)
    print(border)
    
    print("Distances from all points :")
    print(border)

    for d in Data:
        d['distance'] = EUCDistance(d,new_point)

    for d in Data:
        print(d)
    print(border)

    sorted_data = sorted(Data,key = lambda item : item['distance'])
    
    print("Sorted data using distances :")
    print(border)
    for d in sorted_data:
        print(d)
    print(border)

    k = 3

    nearest = sorted_data[:k]
    print(f'{k} nearest neighbours are : ')
    print(border)
    for d in nearest:
        print(d)
    print(border)

    voting = {}

    for neighbour in nearest:
        label = neighbour['Label']
        voting[label] = voting.get(label,0) + 1

    print("Voting result is : ")
    print(border)

    for d in voting:
        print("Names : ",d,"Number of votes : ",voting[d])
    print(border)

    max = 0
    Name = ""

    for d in voting:
        if(voting[d] > max):
            max = voting[d]
            Name = d
    print("Final Prediction is : ",Name)
    print(border)

def main():
    X = int(input("Enter X coordinate : "))
    Y = int(input("Enter Y coordinate : "))

    KNNClassifier(X,Y)

if __name__ == "__main__":
    main()