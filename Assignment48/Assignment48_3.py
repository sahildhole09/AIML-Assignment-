import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    border = "-"*50
    Experience = np.array([[1],[2],[3],[4],[5]])
    Salary = np.array([20000,25000,30000,35000,40000])

    print(border)
    print("Independent Variables - Experience : ",Experience)
    print("Dependent Variables - Salary : ",Salary)
    print(border)

    model = LinearRegression()

    model = model.fit(Experience,Salary)

    New_Experience = 6

    Predicted_Salary = model.predict([[New_Experience]])

    print("Predicted Salary for 6 Years Experience : Rs ",Predicted_Salary)

    plt.plot(
        Experience,
        Salary,
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 0.7,
    )

    plt.scatter(
        Experience,
        Salary,
        s = 100,                    
        marker="o",                
        alpha=0.8,               
        edgecolors="black",        
        linewidths=1,
        label = "Salary"
    )

    plt.title("Experience vs Salary")
    plt.xlabel("Experience")
    plt.ylabel("Salary")

    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()