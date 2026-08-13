import math

def EUCDistance(P1,P2):
    Dist = math.sqrt((P1['Study Hours']-P2['Study Hours'])**2 + (P1['Attendance']-P2['Attendance'])**2)
    return Dist

def KNNClassifier(StudyHours,Attendance):
    border = "-"*50

    print(border)
    print("Dataset is : ")
    print(border)

    Dataset = [
        {'Study Hours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
        {'Study Hours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
        {'Study Hours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
        {'Study Hours' : 1, 'Attendance' : 50, 'Result' : 'Fail'}
    ]

    for d in Dataset:
        print(d)
    print(border)

    print("New Points are : ")
    new_point = {'Study Hours' : StudyHours, 'Attendance' : Attendance}
    print(new_point)
    print(border)

    print("Dataset with Distance is : ")
    print(border)
    for d in Dataset:
        d['distance'] = EUCDistance(d,new_point)

    for d in Dataset:
        print(d)
    print(border)

    sorted_data = sorted(Dataset,key=lambda item : item['distance'])
    print("Sorted Dataset is : ")
    print(border)
    for d in sorted_data:
        print(d)
    print(border)

    K = 3

    nearest = sorted_data[:K]
    print(f"{K} Nearest Neighbors are : ")
    print(border)
    for d in nearest:
        print(d)
    print(border)

    votes = {}
    for neighbours in nearest:
        Result = neighbours['Result']
        votes[Result] = votes.get(Result,0) + 1

    for vote in votes:
        print("Result : ",vote,"& Number of votes are : ",votes[vote])

    max = 0
    Result = ""

    for v in votes:
        if(votes[v] > max):
            max = votes[v]
            Result = v
    print(border)
    print("Final Predicted Result is : ",Result)
    print(border)

def main():
    StudyHours = int(input("Enter Study Hours : "))
    Attendance = int(input("Enter Attendance in Percentage : "))

    KNNClassifier(StudyHours,Attendance)

if __name__ == "__main__":
    main()