#return 1 for royal flush and 10 for high card
cards=["14H","14H","11H","14H","10H","11S","12S"] #cards dealt to one player + the board
hand=["14H","14H","14H","05H","05H"] #5cards selected from the cards list
from collections import defaultdict as dd
from itertools import combinations

def check_royalflush(hand):
    p=check_flush(hand)
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    if(p==5 and values==[10,11,12,13,14]):
        return 1
    else:
        return check_straightflush(hand)

def check_straightflush(hand):
    k=check_straight(hand)
    l=check_flush
    if(k==6 and l==5):
        return 2
    else:
        return check_fourofakind(hand)


def check_fourofakind(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[1,4]):
        return 3
    else:
        return check_fullhouse(hand)



def check_fullhouse(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[2,3]):
        return 4
    else:
        return check_flush(hand)


def check_flush(hand):
    c=0
    values=[i[2] for i in hand]
    for i in range (0,4):
        if(values[i]==values[i+1]):
            c+=1
    if(c==4):
        return 5
    else:
        return check_straight(hand)

def check_straight(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    if(values==[2,3,4,5,14]):
        return 6
    for i in range(values[0], values[0]+5):
        if(i!=values[i-values[0]]):
            return check_triplet(hand)
    return 6

def check_triplet(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values.sort()
    for i in range(3):
        if(values[i]==values[i+1] and values[i+1]==values[i+2]):
            return 7
    return check_twopair(hand)

def check_twopair(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(sorted(values_dict.values())==[1,2,2]):
        return 8
    else:
        return check_pair(hand)

def check_pair(hand):
    values=[i[0:2] for i in hand]
    values=list(map(int,values))
    values_dict=dd(lambda:0)
    for i in values:
        values_dict[i]+=1
    if(set(values_dict.values())=={1,2}):
        return 9
    else:
        return 10

def find_rank(cards):
    pos_hand=list(combinations(cards,5))
    best_rank=10
    for hand in pos_hand:
        rank=check_royalflush(hand)
        if(rank<best_rank):
            best_rank=rank
    print(best_rank)
find_rank(cards)



         








 