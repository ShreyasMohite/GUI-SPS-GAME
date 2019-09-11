from tkinter import *
import tkinter.messagebox
import random

class Employee:
     def __init__(self,root):
       self.root=root
       self.root.geometry('1400x750+0+0')
       self.root.title('payroll management system')

       plays=StringVar( )
       comp=StringVar( )
       win=StringVar( )
#=====================frame============================
#top frame heading of game
       frame=Frame(self.root,bg='Coral1')
       frame.pack()
       frame1=Frame(frame,height=50,width=1350,bd=8,relief=RIDGE,bg='peachpuff2')
       frame1.pack(side=TOP)
       f1=Frame(frame,height=600,width=600,bd=8,relief=RIDGE,padx=50,bg="burlywood1",pady=10)
       f1.pack(side=LEFT)
       f2=Frame(frame,height=700,width=300,bd=8,relief='raise')
       f2.pack(side=RIGHT)
       f3=Frame(f1,height=200,width=600,bd=8,bg="burlywood1")
       f3.pack(side=LEFT)
#===============================label&Entry====================
#label on top
       self.lab=Label(frame1,font=('arial',40,'bold'),text="                            STONE |PAPER| SESSOR                 ",fg='steel blue3',bd=3,bg="peachpuff2")
       self.lab.grid(row=0,column=0)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       player=Label(f1,font=('arial',18,'bold'),text="PLAYER",fg='steel blue3',bd=5,)
       player.pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       playerEntry=Entry(f1,relief=RIDGE,bd=16,textvariable=plays,font=('arial',14,'bold'),width=29,bg="powder blue",fg="red",justify="center")
       playerEntry.pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       comps=Label(f1,font=('arial',18,'bold'),text="COMPUTER",fg='steel blue3',bd=5)
       comps.pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       CompEntry=Entry(f1,relief=RIDGE,bd=16,textvariable=comp,font=('arial',14,'bold'),width=29,bg="powder blue",fg="red",justify="center")
       CompEntry.pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       winner=Label(f1,font=('arial',18,'bold'),text=" WINNER",fg='steel blue3',bd=5)
       winner.pack(side=TOP)
       sf=Label(f1,bg="burlywood1").pack(side=TOP)
       winEntry=Entry(f1,relief=RIDGE,bd=16,textvariable=win,font=('arial',14,'bold'),width=29,bg="powder blue",fg="red",justify="center")
       winEntry.pack(side=TOP)
 #=======================================def(function)============================
       def number_to_name(number):
           import random
           if number==1:
                return "ROCK"
           elif number==2:
                return "SCISSOR"
           elif number==3:
                return "PAPER"
           elif number==4:
                return "METAL"
           else:
               return -1
       computer_number=random.randrange(1,5)
       c_number=random.randrange(1,5)
       com_number=random.randrange(1,5)
       compq_number=random.randrange(1,5)
       compa_choice=number_to_name(computer_number)
       qx=number_to_name(c_number)
       qw=number_to_name(com_number)
       qr=number_to_name(compq_number)
       def paper():
            p=str(playerEntry.get())
            c=str(CompEntry.get())
            a=plays.set("PAPER")
            b=comp.set(compa_choice)
            if p=="PAPER"and c=="PAPER":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("THE MATCH IS TIE")
                 Answer.insert(END,"UNFORTUNATLY=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="PAPER" and c=="ROCK":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("PLAYER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="PAPER" and c=="SCISSOR":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="PAPER" and c=="METAL":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            else:
                 pass
           
                 
            
       def Rock():
            p=str(playerEntry.get())
            c=str(CompEntry.get())
            a=plays.set("ROCK")
            b=comp.set(qx)
            if p=="ROCK"and c=="PAPER":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="ROCK" and c=="ROCK":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("THE MATCH IS TIE")
                 Answer.insert(END,"UNFORTUNATLY=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="ROCK" and c=="SCISSOR":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("PLAYER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="ROCK" and c=="METAL":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            else:
                 pass

       def sessor():
            p=str(playerEntry.get())
            c=str(CompEntry.get())
            a=plays.set("SCISSOR")
            b=comp.set(qw)
            if p=="SCISSOR"and c=="PAPER":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("PLAYER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="SCISSOR" and c=="ROCK":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="SCISSOR" and c=="SCISSOR":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("THE MATCH IS TIE")
                 Answer.insert(END,"UNFORTUNATLY=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="SCISSOR" and c=="METAL":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            else:
                 pass

       def metal():
            p=str(playerEntry.get())
            c=str(CompEntry.get())
            a=plays.set("METAL")
            b=comp.set(qr)
            if p=="METAL"and c=="PAPER":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="METAL" and c=="ROCK":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="METAL" and c=="SCISSSOR":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("COMPUTER")
                 Answer.insert(END,"THE WINNER OF THIS MATCH IS=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            elif p=="METAL" and c=="METAL":
                 Answer.insert(END,"\t\tRESULT\n\n")
                 Answer.insert(END,"PLAYER=\t\t"+playerEntry.get()+"\n\n")
                 Answer.insert(END,"COMPUTER=\t\t"+CompEntry.get()+"\n\n")
                 win.set("THE MATCH IS TIE")
                 Answer.insert(END,"UNFORTUNATLY=\t\t"+winEntry.get()+"\n\n")
                 Answer.insert(END,"_______________________________________________________\n\n")
            else:
                pass

       def clear():
          playerEntry.delete(0,END)
          CompEntry.delete(0,END)
          winEntry.delete(0,END)
          Answer.delete("1.0",END)

       def iExit( ):
              iExit=tkinter.messagebox.askyesnocancel("Question","confirm if you want to exit")
              if iExit > 0:
                  root.destroy( )
                  return
          
          






#=====================================Buttons===============
       but1=Button(f3,text='ROCK',bg='light cyan',command=Rock,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=0)
       lab=Label(f3,bg="burlywood1").grid(row=1,column=0)
       but2=Button(f3,text='PAPER',bg='light cyan',command=paper,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=2,column=0)
       lab=Label(f3,bg="burlywood1").grid(row=3,column=0)
       but3=Button(f3,text='SCISSOR',bg='light cyan',command=sessor,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=4,column=0)
       lab=Label(f3,bg="burlywood1").grid(row=5,column=0)
       but3=Button(f3,text='METAL',bg='light cyan',bd=8,command=metal,height=3,width=10,font=('arial',10,'bold')).grid(row=6,column=0)
       lab=Label(f3,bg="burlywood1").grid(row=7,column=0)
       but4=Button(f3,text='CLEAR',bg='light cyan',bd=8,command=clear,height=3,width=10,font=('arial',10,'bold')).grid(row=8,column=0)
       lab=Label(f3,bg="burlywood1").grid(row=9,column=0)
       but5=Button(f3,text='Exit',bg='light cyan',bd=8,command=iExit,height=3,width=10,font=('arial',10,'bold')).grid(row=10,column=0)
       
#======================================TEXTBOX==================
       Answer=Text(f2, width=55,height=28,font=('arial',12,'bold'),bd=3,bg="gray53",fg="white",pady=15)
       Answer.grid(row=0,column=0)

       
       
if __name__=='__main__':
     root=Tk()
     application=Employee(root)
     root.mainloop()
