import tkinter as tk

root = tk.Tk()

root.title("Largest Number")
root.geometry("350x400")

tk.Label(root,text="Marvellous Largest Number Evaluator",
         font=("Arial",11,"bold")).pack(pady=20)

tk.Label(root,text="Enter First Number",
         font=("Arial",10,"bold")).pack()
entry1 = tk.Entry(root)
entry1.pack(pady=8)

tk.Label(root,text="Enter Second Number",
         font=("Arial",10,"bold")).pack()
entry2 = tk.Entry(root)
entry2.pack(pady=8)

tk.Label(root,text="Enter Third Number",
         font=("Arial",10,"bold")).pack()
entry3 = tk.Entry(root)
entry3.pack(pady=8)

def LargestNo():
    No1 = int(entry1.get())
    No2 = int(entry2.get())
    No3 = int(entry3.get())

    if No1 > No2 and No1 > No3:
        labelResult.config(text="Largest Number is : "+str(No1))
    elif No2 > No1 and No2 > No3:
        labelResult.config(text="Largest Number is : "+str(No2))
    else:
        labelResult.config(text="Largest Number is : "+str(No3))

tk.Button(root,text="Find Maximum",command=LargestNo).pack(pady=8)

labelResult = tk.Label(root,text="",font=("Arial",10,"bold"))
labelResult.pack(pady=8)

root.mainloop()