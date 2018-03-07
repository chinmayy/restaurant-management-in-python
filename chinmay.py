from Tkinter import *

class item:
    def __init__(self,a,b):
        self.name=a
        self.price=b
        self.c=IntVar()

root=Tk()
root.title("restraunt managment")
root.geometry("1280x1000")
d=[]
m1=item("macroni",105)
d.append(m1)
m2=item("pav bhaji",110)
d.append(m2)
m3=item("sandwich",80)
d.append(m3)
m4=item("pasta",80)
d.append(m4)
m5=item("aloo paratha",200)
d.append(m5)
m6=item("omelete",30)
d.append(m6)
m7=item("poha",50)
d.append(m7)
m8=item("fruits",40)
d.append(m8)
m9=item("noodles",120)
d.append(m9)
m10=item("bread butter",20)
d.append(m10)
m11=item("egg",20)
d.append(m11)
m12=item("sprouts",65)
d.append(m12)
m13=item("idli",60)
d.append(m13)
m14=item("porage",55)
d.append(m14)
m15=item("upama",70)
d.append(m15)
m16=item("milk corn flakes",25)
d.append(m16)
Label(root,text='Select Your Breakfast',font='Arial 28 bold',height=2).grid(row=0,column=0,columnspan=4)

i=1
j=2
while i<=16:
    if i%2==1:
        Checkbutton(root,text=d[i-1].name+"("+str(d[i-1].price)+")",font="Arial 30 bold",variable=d[i-1].c,onvalue=1).grid(row=j,column=0,columnspan=2,sticky=W)
    else:
        Checkbutton(root,text=d[i-1].name+"("+str(d[i-1].price)+")",font="Arial 30 bold",variable=d[i-1].c,onvalue=1).grid(row=j,column=2,columnspan=2,sticky=W)
        j=j+1
    i=i+1
def check():
    s=0
    k=0
    while k<16:
        if (d[k].c).get()==1:
            s=s+d[k].price
        k=k+1
    Label(root,text="Total Amount of your Breakfast: "+str(s)+" INR",font="Arial 20 bold").grid(row=j+1,column=2,columnspan=2)
def e():
    root.destroy()
Button(root,text="Check Rs.",height=2,command=lambda: check()).grid(row=j+1,column=0,sticky=W+E+N+S)
Button(root,text="Exit",height=2,command=lambda: e()).grid(row=j+1,column=1,sticky=W+E+N+S)

root.mainloop()
