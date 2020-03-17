import random
n=int(input("Enter the number of players: "))
List= []
List1=[] 
List2=[]
List3=[]
List4=[]
#List 5 for 1 deck
List5=[]
#List6 for storing the cards of players
List6=[]
for i in range(2,15):
    List.append(i)                                                                
for j in range(0,13):
    List1.append(str(List[j])+'h')
for k in range (0,13):
    List2.append(str(List[k])+'d')     
for q in range (0,13):
    List3.append(str(List[q])+'s')  
for m in range (0,13):
    List4.append(str(List[m])+'c')     
List5=List1+List2+List3+List4
for p in range(1,n+1):
    y= random.choice(List5)
    x=random.choice(List5)
    print("player",p, "has", y, x)
    List5.remove(y)
    List5.remove(x)
    List6.append(y)
    List6.append(x)
#FLOP ROUND
z=random.choice(List5)
def round1_reveal():
    y= random.choice(List5)
    x=random.choice(List5)
    print("Dealer has ",y,x,z)
    List5.remove(y)
    List5.remove(x)
    List5.remove(z)
round1_reveal() 
#TURN ROUND
w= random.choice(List5)
def round2_reveal():
    print("Dealer has ",y,x,z,w)
    List5.remove(w)
round2_reveal()  
#RIVER ROUND
def round3_reveal():
    v= random.choice(List5)
    print("Dealer has ",y,x,z,w,v)
    List5.remove(v)
round3_reveal()