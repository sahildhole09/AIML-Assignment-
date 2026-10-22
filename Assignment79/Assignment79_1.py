import tkinter as tk

root = tk.Tk()

root.title("Marvellous Addition Calculator")
root.geometry("350x400")

tk.Label(root,text = "Marvellous Infosystems", 
         font=("Times New Roman",20,"bold")).pack(pady=15)

tk.Label(root,text="Enter First Number",
         font=("Times New Roman",14)).pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=10) 

tk.Label(root,text="Enter Second Number",
         font=("Times New Roman",14)).pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=10)

def Addition():
    No1 = int(entry1.get())
    No2 = int(entry2.get())

    result = No1 + No2

    labelResult.config(text = "Addition is : "+str(result))

tk.Button(root,text="Add",command=Addition).pack(pady=14)

labelResult = tk.Label(root,text="",font=("Times New Roman",15))
labelResult.pack()

root.mainloop()