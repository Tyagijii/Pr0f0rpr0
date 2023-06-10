import random
import sys
'''import pywhatkit
pywhatkit.init
pywhatkit.sendwhatmsg('+919837500951' , 'Hello' , 14 , 50)'''
G=True
while G:
    a=random.randint(1,3)
    if a==1:
        com="Stone"
    elif a==2:
        com='Paper'
    else:
        com="Scissor"
    U=input("Choose Stone(st) or Paper(p) or scissor(sc)")
    if U=='stone' or U=='st' or U=='Stone' or U=='r':
        user="Stone"
    elif U=='paper' or U=='p' or U=='Paper':
        user="Paper"
    elif U=='scissor' or U=='sc' or U=='Scissor':
        user="Scissor"
    print('Computer choose :' , com)
    print('You choose: ' , user)
    if user==com:
        print('The Game is a Tie')
    elif (user=='Paper' and com=='Scissor') or (user=='Stone' and com=='Paper') or (user=='Scissor' and com=='Stone'):
        print('You lose')
    elif (com=='Paper' and user=='Scissor') or (com=='Stone' and user=='Paper') or (com=='Scissor' and user=='Stone'):
        print('You win')
    A=input('Want to play more : ')
    if A=='Yes' or A=='yes' or A=='y':
        G=True
    elif A=='No' or A=='no' or A=='n':
        G=input('')
        
    else:
        print('Command not satisfied please write again')
        A=input('want to play more : ')
sys.exit()
quit()