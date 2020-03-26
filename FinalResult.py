from collections import defaultdict as dd
#sf,flush, straight, highcard can be solved using one function
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

def xyz(cardlist,rank):
    hand1=cardlist[0:5]
    hand2=cardlist[5:11]
    if(rank==2 or rank==5 or rank==6 or rank==10):
        return(solve1(hand1,hand2))
    elif(rank==3 or rank==4 or rank==7 or rank==8 or rank==9):
        return(solve2(hand1,hand2))
    else:
        return 0

