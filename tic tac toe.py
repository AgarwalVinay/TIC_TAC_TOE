from tkinter import *
import tkinter.messagebox
import itertools
root=Tk()
f11=Frame(root,bg='powder blue')
#img=PhotoImage(file='x.png')
#img2=PhotoImage(file='o.png')
l=[]
selected=IntVar()

playeroneturn=True
pl1=[]
pl2=[]
wincom=[(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9)]
def ReSet():
    global counter
    b1['state']='active'
    b1['text']='Start'
    pl2.clear()
    pl1.clear()
    counter=0
    button()
    
def button():
    for i in range(3):
        for j in range(3):
            l.append(Button(f11,width=25,height=10,bd=5,state='disable',command=lambda x=(i,j):(g(x) if playeroneturn==True else m(x))))
            l[-1].grid(row=i,column=j,padx=5,pady=5)
def f():
    for i in l:
        i['state']='active'
        rad1.select()
    b1['text']='Restart'
    b1['state']='disable'
def g(t):
    global playeroneturn
    global pl1
    global counter
    pl1.append(3*t[0]+t[1]+1)
    rad2.select()
    Button(f11,width=25,height=10,bd=5,bg="#446CB3",state='disable').grid(row=t[0],column=t[1])
    playeroneturn=False
    r=Result(pl1)
    counter=counter+1
    if r==True:
        print("player 1")
        for i in l:
            i['state']='disable'
        tkinter.messagebox.showinfo('Result','player1 win')
        ReSet()
    elif counter==9:
        counter=0
        tkinter.messagebox.showinfo('Result','Draw')
        ReSet()
def m(t):
    global playeroneturn
    global pl2
    global counter
    pl2.append(3*t[0]+t[1]+1)
    rad1.select()
    Button(f11,width=25,height=10,bd=5,bg="#F4D03F",state='disable').grid(row=t[0],column=t[1])
    playeroneturn=True
    counter=counter+1
    r=Result(pl2)
    if r==True:
        print("player 2")
        for i in l:
            i['state']='disable'
        tkinter.messagebox.showinfo('Result','player2 win')
        ReSet()
    elif counter==9:
        counter=0
        tkinter.messagebox.showinfo('Result','Draw')
        ReSet()
        
    
def Result(l):
    global wincom
    if len(l)>=3:
        for i in itertools.permutations(l,3):
            if i in wincom:
                return True
    return False
counter=0
button()
b1=Button(f11,text='Start',command=f)
b1.grid(row=4,column=1)
rad1=Radiobutton(f11,text='Player 1',bg="#446CB3",font=('arial',20,'bold'),fg='black',value=1,variable=selected,state='disable')
rad2=Radiobutton(f11,text='Player 2',bg="#F4D03F",font=('arial',20,'bold'),fg='black',value=2,variable=selected,state='disable')
rad1.grid(row=4,column=0)
rad2.grid(row=4,column=2)
f11.grid()
root.mainloop()
