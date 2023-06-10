import random


para=("""He was aware there were numerous wonders of this world including the unexplained creations of humankind that showed the wonder of our ingenuity. There are huge heads on Easter Island. There are the Egyptian pyramids. There’s Stonehenge. But he now stood in front of a newly discovered monument that simply didn't make any sense and he wondered how he was ever going to be able to explain it


If you're looking for random paragraphs, you've come to the right place. When a random word or a random sentence isn't quite enough, the next logical step is to find a random paragraph. We created the Random Paragraph Generator with you in mind. The process is quite simple. Choose the number of random paragraphs you'd like to see and click the button Your chosen number of paragraphs will instantly appear

While it may not be obvious to everyone, there are a number of reasons creating random paragraphs can be useful. A few examples of how some people use this generator are listed in the following paragraphs.""")

names=("""arnav akshit kartikey lakshay kartik abhay suryansh madhav prateek harshit""")


lis=names.split(" ")

sword=random.choice(lis)
swordl=[]
swordl[:0]=sword
sword1=swordl

slist=[]
for i in sword1:
  slist.append("?")


chances=len(sword)+5
win=False
print(slist)

while chances:
  print("You have ",chances,"chances")
  
  choice=input("Enter guess")
  chances-=1
  if choice in swordl:
    if choice in slist:
      sind=slist.index(choice)
      try:
        ind=sword.index(choice,sind+1)
      except:
        ind=sword.index(choice,sind)
    
    else:
      ind=swordl.index(choice)
    try:
      slist[ind]=choice
    except:
      pass
    try:
      pass
      #swordl.remove(choice)
    except:
      pass
    
    print("Correct")
    
  else:
    print("Wrong")
  print(slist) 
  if slist==sword1:
    print("You win")
    win=True
    break
    
print("The word is",sword)
if not win:
  print("You lose")
 
   
