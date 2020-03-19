import random

n=int(input("Enter the number of players: "))

List= []

List1=[] 

List2=[]

List3=[]

List4=[]

#List 5 for 1 deck
deck=[]

#List6 for storing the cards of players
List6=[]

#Table for cards on the table
table=[]

for i in range(2,15):
    List.append(i)                                                                

for j in range(0,13):
    if j<8:
        List1.append(str(0)+str(List[j])+'h')
    else:
        List1.append(str(List[j])+'h')

for k in range (0,13):
    if k<8:
        List2.append(str(0)+str(List[k])+'d')
    else:
        List2.append(str(List[k])+'d')    

for q in range (0,13):
    if q<8:
        List3.append(str(0)+str(List[q])+'s')
    else:
        List3.append(str(List[q])+'s') 

for m in range (0,13):
    if m<8:
        List4.append(str(0)+str(List[m])+'c')
    else:
        List4.append(str(List[m])+'c')     
deck=List1+List2+List3+List4


def player_hand():
    global l
    global o
    for p in range(1,n+1):
        l= random.choice(deck)
        o=random.choice(deck)
        print("player",p, "has", l,o )
        deck.remove(l)
        deck.remove(o)
        List6.append(l)
        List6.append(o)
        table.append(l)
        table.append(o)
player_hand()