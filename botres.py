from collections import defaultdict as dd
from itertools import combinations

#return 1 for royal flush and 10 for high card
cards=["06H","13H","11H","10H","09H","08H","07H"] #cards dealt to one player + the board
hand=["14H","14H","14H","05H","05H"] #5cards selected from the cards list

def check_royalflush(hand):
    p=check_flush(hand)
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    if(p==5 and values==[10,11,12,13,14]):
        return True
    else:
        return False

def check_straightflush(hand):
    k=check_straight(hand)
    l=check_flush(hand)
    if(k==6 and l==5):
        return True
    else:
        return False

def check_fourofakind(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[1,4]):
        return True
    else:
        return False

def check_fullhouse(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[2,3]):
        return True
    else:
        return False

def check_flush(hand):
    c=0
    values=[i[2] for i in hand]
    for i in range (0,4):
        if(values[i]==values[i+1]):
            c+=1
    if(c==4):
        return True
    else:
        return False

def check_straight(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    if(values==[2,3,4,5,14]):
        return True
    for i in range(values[0], values[0]+5):
        if(i!=values[i-values[0]]):
            return False
    return True

def check_triplet(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    for i in range(3):
        if(values[i]==values[i+1] and values[i+1]==values[i+2]):
            return True
    return False

def check_twopair(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[1,2,2]):
        return True
    else:
        return False

def check_pair(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(set(values_dict.values())=={1,2}):
        return True
    else:
        return False

def check_hand(hand):
    if(check_royalflush(hand)):
        return 1
    elif(check_straightflush(hand)):
        return 2
    elif(check_fourofakind(hand)):
        return 3
    elif(check_fullhouse(hand)):
        return 4
    elif(check_flush(hand)):
        return 5
    elif(check_straight(hand)):
        return 6
    elif(check_triplet(hand)):
        return 7
    elif(check_twopair(hand)):
        return 8
    elif(check_pair(hand)):
        return 9
    else:
        return 10


def find_rank(cards,flag):
    cards.sort(reverse=True)
    pos_hand=list(combinations(cards,5))
    best_rank=10
    for hand in pos_hand:
        rank=check_hand(hand)
        if(rank<best_rank):
            best_rank=rank
            best_hand=hand
    if(flag==0):
        return best_rank
    elif(flag==1):
        return best_hand

