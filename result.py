#return 1 for royal flush and 10 for high card
cards=["07H","03H","03H","05D","06C","11S","12S"] #cards dealt to one player + the board
hand=["04H","02H","06H","05D","14C"] #5cards selected from the cards list
from collections import defaultdict as dd
from itertools import combinations




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
        rank=check_straight(hand)
        if(rank<best_rank):
            best_rank=rank
    print(best_rank)
find_rank(cards)



         








 