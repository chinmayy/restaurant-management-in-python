from Tkinter import*
import os
root=Tk()

root.configure(bg='white')
root.title("welcome")


def lunch():
    root.destroy()
    os.startfile("lunch.py")
def brkfst():
    root.destroy()
    os.startfile("brkfst.py")


Button(root,text="breakfast",bd=7,font='arial 20 bold',foreground='green',background='white',command=brkfst).pack()
Button(root,text="   lunch and dinner  ",bd=7,font='arial 20 bold',foreground='green',background='white',command=lunch).pack()


root.mainloop()
