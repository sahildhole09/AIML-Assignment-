import math

def EUCDistance(P1,P2):
    Dist = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Dist

def KNNClassifier(X,Y,K):
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

    nearest = sorted_data[:K]
    print(f'{K} nearest neighbours are : ')
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

    KNNClassifier(X,Y,K = 1)

    KNNClassifier(X,Y,K = 3)

    KNNClassifier(X,Y,K = 5)


if __name__ == "__main__":
    main()


# Why does prediction change when K increase ?
# -> Prediction changes because K decides how many nearest neighbours are considered for voting.
#    With K = 1 only the closest point is considered,so the prediction depends completely depends on that one point.
#    With K = 3 the three closest points vote. Here two are Red and one is Blue,so prediction is Red.
#    With K = 5 five nearest neighbours are considered for voting,but in this given dataset there are only 4 data 
#    points so technically it is not valid for proper result of K = 5 it would require atleast 5 data points or
#    tie breaking rule.
#    Since more neighbours are included, farther data points can affect the prediction,which may change the 
#    majority class. 