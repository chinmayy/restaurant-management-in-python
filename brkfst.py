from Tkinter import *
import tkMessageBox
class item:
    def __init__(self,a,b):
        self.name=a
        self.price=b
        self.c=IntVar()

root=Tk()
root.title("restraunt managment")
root.configure(bg="#FFEFD5")
d=[]
m1=item("samosa chat",30)
d.append(m1)
m2=item("idli sambhar",50)
d.append(m2)
m3=item("bread omlete",50)
d.append(m3)
m4=item("cheese sandwitch",80)
d.append(m4)
m5=item("paneer pakoda",120)
d.append(m5)
m6=item("aloo paratha",60)
d.append(m6)
m7=item("boiled egg",20)
d.append(m7)
m8=item("pasta",150)
d.append(m8)
m9=item("french toast",150)
d.append(m9)
m10=item("chilli paneer",200)
d.append(m10)
m11=item("sizzler",250)
d.append(m11)
m12=item("sprouts",110)
d.append(m12)
m13=item("chhola bhatura",80)
d.append(m13)
m14=item("momos",100)
d.append(m14)
m15=item("upama",110)
d.append(m15)
m16=item("milk ",40)
d.append(m16)
Label(root,text='Good Morning...',bg="#FFEFD5",foreground="red",font='ALGERIAN 25 bold',height=2).grid(row=0,column=0,columnspan=4)
Label(root,text="Today's menu:-",bg="#FFEFD5",foreground="red",font='Arial 25 bold',height=2).grid(row=1,column=0,columnspan=4)

i=1
j=2
while i<=16:
    if i%2==1:
        Checkbutton(root,text=d[i-1].name,font="Arial 10 ",bg="#FFEFD5",variable=d[i-1].c,onvalue=1).grid(row=j,column=0,columnspan=2,sticky=W)
        Label(root,text="                        ............."+(str(d[i-1].price)+"          "),font="Ariel 10 ",bg="#FFEFD5").grid(row=j,column=2,columnspan=2,sticky=W)
    else:
        Checkbutton(root,text=d[i-1].name,font="Arial 10",bg="#FFEFD5",variable=d[i-1].c,onvalue=1).grid(row=j+8,column=0,columnspan=2,sticky=W)
        Label(root,text="                        ............."+(str(d[i-1].price)+"          "),font="Ariel 10",bg="#FFEFD5").grid(row=j+8,column=2,columnspan=2,sticky=W)
        j=j+1
    i=i+1
def check():
    root.destroy()
    root1=Tk()
    root1.configure(bg="#FFEFD5")
    root1.title("final")
    
    s=0
    k=0
    while k<16:
        if (d[k].c).get()==1:
            s=s+d[k].price
            Label(root1,text=d[k].name+"..."+str(d[k].price),bg="#FFEFD5").pack()
        k=k+1
    buttoncheck(s)
    Label(root1,text="total bill: "+str(s)+" INR",bg="#FFEFD5",font="Arial 20 bold").pack()
    Button(root1,text="DONE",bg="red",height=2,command=lambda: e1()).pack()
    def e1():
        root1.destroy()
        tkMessageBox.showinfo(title='thank you',message="have a nice day ")
    
def buttoncheck(s):
    tkMessageBox.showinfo(title='Total Bill',message="Total Amount of your Breakfast: "+str(s)+" INR")
    
#Label(root,text="Total Amount of your Breakfast: "+str(s)+" INR",font="Arial 20 bold").grid(row=j+1,column=2,columnspan=2)
def e():
    root.destroy()

Button(root,text="generate bill",bg="red",height=2,command=lambda: check()).grid(row=j+9,column=0,sticky=W+E+N+S)
Button(root,text="Exit",bg="red",height=2,command=lambda: e()).grid(row=j+9,column=1,columnspan=2,sticky=W+E+N+S)

root.mainloop()
