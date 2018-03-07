from Tkinter import*
import os
root=Tk()
root.configure(bg='white')
root.geometry('800x400')
root.title("ONLINE SHOPPING PORTAL")

Label(root,text="Chinmay Gupta",font='Calibri 30 bold italic',bg='white',foreground='orange').pack()

Label(root,text="B2 ",font='Calibri 30 bold italic',foreground='orange',bg='white').pack()

Label(root,text="151272",font='Calibri 30 bold italic',foreground='orange',bg='white').pack()


Label(root,text="PROJECT:",font='calibri 30 bold',fg='magenta',bg='white').pack()
Label(root,text="RESTAURANT MANAGEMENT SYSTEM",font='calibri 30 bold',fg='orange',bg='white').pack()

def fun():
    root.destroy()
    os.startfile("welcome.py")
    
Button(root,text="hungry kya..??",bd=7,font='arial 20 bold',foreground='white',background='red',command=fun).pack()



root.mainloop()
