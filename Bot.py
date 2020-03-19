import random
from collections import defaultdict as dd

from itertools import combinations
List=[]
List1=[] 
List2=[]
List3=[]
List4=[]
#List 5 for 1 deck
List5=[]
#List6 for storing the cards of players
for i in range(2,15):
    if(i<10):
        List.append('0'+str(i))  
    else:
        List.append(str(i))
                                                              
for j in range(0,13):
    List1.append(str(List[j])+'H')
for k in range (0,13):
    List2.append(str(List[k])+'D')     
for q in range (0,13):
    List3.append(str(List[q])+'S')  
for m in range (0,13):
    List4.append(str(List[m])+'C')     
List5=List1+List2+List3+List4

print(List5)

bcards=[]
def distribute(bcards, List5):
    for i in range(2):
        bcards.append(random.choice(List5))
        List5.remove(bcards[i])


print()
print()
print(bcards)

dealer=[]
def flop(dealer,List5):
    for i in range(3):
        dealer.append(random.choice(List5))
        List5.remove(dealer[i])

def turn(dealer,List5):
    dealer.append(random.choice(List5))
    List5.remove(dealer[3])

def river(dealer,List5):
    dealer.append(random.choice(List5))
    List5.remove(dealer[4])

distribute(bcards,List5)
flop(dealer, List5)


turn(dealer,List5)
print(dealer)

def pre_river(bcards,dealer,List5):
    avc=bcards+dealer
    print(avc)
    for i in range(46):
        count=0
        avcf=[]
        avcf.append(List5[i])
        avcf+=avc
        
        


    print(avcf)
pre_river(bcards,dealer,List5)