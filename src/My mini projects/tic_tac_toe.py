from tkinter import *
from tkinter import messagebox

window=Tk()

F=Frame(window,height=20,width=20)
F.place(relx=0.5,rely=0.5,anchor=CENTER)


board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def minimax(board,turn):
    if checkwin(u):
        return -10
    elif checkwin(c):
        return 10
    elif checkdraw():
        return 1
        
    if turn:
        score=-100
        for i in board.keys():
            if free(i):
                board[i]=c
                s=minimax(board,False)
                board[i]=' '
                if s>score:
                    score=s
        return score
    
    else:
        score=100
        for i in board.keys():
            if free(i):
                board[i]=u
                s=minimax(board,True)
                board[i]=' '
                if s<score:
                    score=s
        return score
    
def g(i):
    return board[i]

def ground():
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('--+---+--')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('--+---+--')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    
def free(index):
    if board[index]==' ':
        return True
    else:
        return False

def insert(index,letter):
    board[index]=letter
        
u='X'
c='O'

#def user(index):
#    return
#    user(index)
#    move(board)
#    
            # 

def us(index):
    if Tkboard[index]['text']=='  ':
        Tkboard[index]['text']='X'
        Tkboard[index]['state']=DISABLED
        insert(index,'X')
        move(board)
        if checkwin('O'):
            messagebox.showinfo('Game Ends','You LOSE')
            reset()
        if checkwin('X'):
            messagebox.showinfo('Game Ends','You WIN')
            reset()
            # 
        for i in Tkboard.keys():
            if Tkboard[i]['text']=='  ':
                
                return
        messagebox.showinfo('Game ends','Its a Draw')
        reset()
        # 
        
    else:
        pass

h=1
w=1

Tkboard={
1:Button(F,text='  ',command=lambda:us(1),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
2:Button(F,text='  ',command=lambda:us(2),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
3:Button(F,text='  ',command=lambda:us(3),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
4:Button(F,text='  ',command=lambda:us(4),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
5:Button(F,text='  ',command=lambda:us(5),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
6:Button(F,text='  ',command=lambda:us(6),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
7:Button(F,text='  ',command=lambda:us(7),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
8:Button(F,text='  ',command=lambda:us(8),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
9:Button(F,text='  ',command=lambda:us(9),height=h,width=w,
fg='red',bg='blue',activebackground='blue',font=('Arial',50,'bold')),
}



#Tkboard[1].place(x=150,y=290)
Tkboard[1].grid(row=4,column=4)
Tkboard[2].grid(row=4,column=5)
Tkboard[3].grid(row=4,column=6)
Tkboard[4].grid(row=5,column=4)
Tkboard[5].grid(row=5,column=5)
Tkboard[6].grid(row=5,column=6)
Tkboard[7].grid(row=6,column=4)
Tkboard[8].grid(row=6,column=5)
Tkboard[9].grid(row=6,column=6)




def reset():
    for i in range(1,10):
        Tkboard[i]['text']='  '
        board[i]=' '
        Tkboard[i].config(state=ACTIVE)


def move(board):
    best= 0
    score=-100
    for i in board.keys():
        if board[i]==' ':
            board[i]=c
            s=minimax(board,False)
            board[i]=' '
            if s>score:
                best=i
                score=s
    try:
        Tkboard[int(best)]['text']='O' 
        insert(best,'O')
    except:
        messagebox.showinfo('Game Ends','Its a DRAW')
        reset()
         


def checkwin(letter):
    if g(1)==g(2)==g(3)==letter:
        return True
    elif g(4)==g(5)==g(6)==letter:
        return True
    elif g(7)==g(8)==g(9)==letter:
        return True
    elif g(1)==g(5)==g(9)==letter:
        return True
    elif g(7)==g(5)==g(3)==letter:
        return True
    elif g(4)==g(1)==g(7)==letter:
        
        return True
    elif g(2)==g(5)==g(8)==letter:
        
        return True
    elif g(3)==g(6)==g(9)==letter:
        
        return True
    else:
        return False

def checkdraw():
    
    for i in board.keys():
        if board[i]==' ':
            return False
   
    return True



window.mainloop()




