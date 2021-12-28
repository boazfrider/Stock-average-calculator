
from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("Average Stock Calcukator")

def calc():
    total=0
    avg=0
    mone=0
    mechane=0
    temp=0
    for i in range(0,9,2):
        total+=int((lst[i].get("1.0",END)))
        
    for i in range(0,9,2):
        mone=float((lst[i].get("1.0",END)))
        mechane=float((lst[i+1].get("1.0",END)))
        temp=(mone/total)*float((lst[i+1].get("1.0",END)))
        avg+=temp

    texttoinsert="total shares : "+ str(total) + " average: " + ("{:.2f}".format(avg))
    result_label.config(text=texttoinsert)
    #result_label.configure(font=('Arial',18))
    


e1=Label(window,text="amount of share")
e1.place(relx=0.25,rely=0.05)


e2=Label(window,text="price")
e2.place(relx=0.65,rely=0.05)

result_label=Label(window,text="")
result_label.place(relx=0.18, rely= 0.75)
result_label.configure(font=('Arial',15))

lst=[]
for i in range(1,6):
    t1=Text(window,height=1,width=10)
    
    t1.delete("1.0",END)
    t1.insert(END,"0")
    # t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    # t1.insert(END,"hello")

    t2=Text(window,height=1,width=10)
    t2.delete("1.0",END)
    t2.insert(END,"0")
    t1.place(relx=0.25 , rely=0.05+0.08*i)
    t2.place(relx=0.65 , rely=0.05+0.08*i)
    lst.append(t1)
    lst.append(t2)
btn=Button(window,text="Calculate",command=calc)
btn.place(relx=0.45 , rely=0.65)

# t=lst[2]
# t.delete("1.0",END)
# t.insert(END,"hello")
# print(type(t))
window.mainloop()
