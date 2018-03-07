from Tkinter import *
import tkMessageBox
class item:
    def __init__(self,a,b):
        self.name=a
        self.price=b
        self.c=IntVar()

root=Tk()
root.title("restraunt managment")
root.configure(bg="#D2B48C")
d=[]
m1=item("Dal tadka",100)
d.append(m1)
m2=item("Panner tikka",320)
d.append(m2)
m3=item("Paneer bhurji",190)
d.append(m3)
m4=item("Paneer handi",220)
d.append(m4)
m5=item("Paneer kadhai",250)
d.append(m5)
m6=item("plain naan",40)
d.append(m6)
m7=item("Butter chicken",450)
d.append(m7)
m8=item("butter naan",50)
d.append(m8)
m9=item("Roasted chicken",300)
d.append(m9)
m10=item("stuffed naan",70)
d.append(m10)
m11=item("pneer-do-pyaza",150)
d.append(m11)
m12=item("missi",50)
d.append(m12)
m13=item("chicken masala",260)
d.append(m13)
m14=item("rumali roti",55)
d.append(m14)
m15=item("dum aloo",150)
d.append(m15)
m16=item("tandoori roti...",20)
d.append(m16)
Label(root,text='MENU...',font='Algerian 28 bold',bg="#D2B48C",height=2).grid(row=0,column=0,columnspan=4)

i=1
j=2
while i<=16:
    if i%2==1:
        Checkbutton(root,text=d[i-1].name,font="Arial 10",bg="#D2B48C",variable=d[i-1].c,onvalue=1).grid(row=j,column=0,columnspan=2,sticky=W)
        Label(root,text="                   ................."+str(d[i-1].price),bg="#D2B48C",font="Arial 10").grid(row=j,column=2,columnspan=2,sticky=W)
        
    else:
        Checkbutton(root,text=d[i-1].name,bg="#D2B48C",font="Arial 10 ",variable=d[i-1].c,onvalue=1).grid(row=j+8,column=0,columnspan=2,sticky=W)
        Label(root,text="                   ................."+str(d[i-1].price),bg="#D2B48C",font="Arial 10").grid(row=j+8,column=2,columnspan=2,sticky=W)
        j=j+1
    i=i+1
def check():
    root.destroy()
    root1=Tk()
    root1.configure(bg="#D2B48C")
    root1.title("final")
    s=0
    k=0
    while k<16:
        if (d[k].c).get()==1:
            s=s+d[k].price
            Label(root1,text=d[k].name+"..."+str(d[k].price),bg="#D2B48C").pack()
        k=k+1
    buttoncheck(s)
    Label(root1,text="total bill: "+str(s)+" INR",bg="#D2B48C",font="Arial 20 bold").pack()
    Button(root1,text="DONE",bg="#8B4513",height=2,command=lambda: e1()).pack()
    def e1():
        root1.destroy()
        tkMessageBox.showinfo(title='thank you',message="have a nice day ")
def buttoncheck(s):
    tkMessageBox.showinfo(title='total bill',message="total amount: "+str(s)+" INR")
    
def e():
    root.destroy()
Button(root,text="generate bill",bg="#8B4513",height=2,command=lambda: check()).grid(row=j+9,column=0,sticky=W+E+N+S)
Button(root,text="Exit",bg="#8B4513",height=2,command=lambda: e()).grid(row=j+9,column=1,sticky=W+E+N+S)

root.mainloop()
