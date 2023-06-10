import random

p1=input("Enter first player name")
p2=input("Enter second payer name")


def cric(player):
  print(player , "chance")

  score=0
  w=3
  while w:
    b=input("enter")
    if b=='q' or b=='Q':
      break
    else:
      run = random.randint(0,9)
      
      for i in [0,7,8]:
        if run==i:
          
        
          w-=1
          print("OUT by",run)
      if run==9:
        print("Wide ball")
      
        score+=1
      elif run<7 and run>0:
        print('This ball made ',run)
      
        score+=run
      print("Your total score till now is",score)
  return score    
      
      
      
  
pl1=cric(p1)
print()
pl2=cric(p2)

print("Runs made by" ,p1 ,"are",pl1)
print("Runs made by" ,p2 ,"are",pl2)

if pl1>pl2:
  print(p1," wins")
elif pl2>pl1:
  print(p2," wins")
else:
  print("It's a tie")












