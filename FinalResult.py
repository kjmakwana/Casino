#rf doesnt have any case
from collections import defaultdict as dd
#sf,flush, straight, highcard can be solved using one function
hand1=["14H","14H","11H","09H","11H"]
hand2=["14H","14H","10H","13H","10H"]
def solve1(hand1,hand2):
    values1=[i[0:2] for i in hand1]
    values1=list(map(int,values1))
    values1.sort()
    values2=[i[0:2] for i in hand2]
    values2=list(map(int,values2))
    values2.sort()
    
    for (i,j) in zip(values1,values2):
        if(i>j):
            return 1
        elif(j<i):
            return 2
    return 0


#Fok,tok,two pair,full house and one pair can be solved using one function
def solve2(hand1,hand2):
    values1=[i[0:2] for i in hand1]
    values1=list(map(int,values1))
    values_dict1=dd(lambda:0)
    for i in values1:
        values_dict1[i]+=1

    values2=[i[0:2] for i in hand2]
    values2=list(map(int,values2))
    values_dict2=dd(lambda:0)
    for i in values2:
        values_dict2[i]+=1

    sv1=sorted(values_dict1.items(), reverse=True,key=lambda kv: (kv[1],kv[0]))
    sv2=sorted(values_dict2.items(), reverse=True,key=lambda kv: (kv[1],kv[0]))
    for i in range(len(sv1)):
        if(sv1[i][0]>sv2[i][0]):
            return 1
        elif(sv1[i][0]<sv2[i][0]):
            return 2
    return 0

print(solve2(hand1,hand2))