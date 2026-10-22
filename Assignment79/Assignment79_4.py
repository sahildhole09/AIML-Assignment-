import tkinter as tk

root = tk.Tk()

root.title("Voting Eligibility Checker")
root.geometry("350x350")

tk.Label(root,text="Marvellous Voting Eligibility Checker",
         font=("Arial",11,"bold")).pack(pady=20)

tk.Label(root,text="Enter Your Name",
         font=("Arial",10,"bold")).pack()
entry1 = tk.Entry(root)
entry1.pack(pady=8)

tk.Label(root,text="Enter Your Age",
         font=("Arial",10,"bold")).pack()
entry2 = tk.Entry(root)
entry2.pack(pady=8)

def CheckEligibility():
    Age = int(entry2.get())

    if Age >= 18:
        labelResult.config(text="You are Eligible for Voting")
    else:
        labelResult.config(text="Sorry! You are Not Eligible for Voting")

tk.Button(root,text="Check Eligibility",command=CheckEligibility).pack(pady=10)

labelResult = tk.Label(root,text="",font=("Arial",10,"bold"))
labelResult.pack(pady=10)

root.mainloop()