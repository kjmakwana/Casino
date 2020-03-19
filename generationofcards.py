import random
def card_deck(List,List1,List2,List3,List4,deck):

    for i in range(2,15):
        List.append(i)                                                                

    for j in range(0,13):
        if j<8:
            List1.append(str(0)+str(List[j])+'H')
        else:
            List1.append(str(List[j])+'H')

    for k in range (0,13):
        if k<8:
            List2.append(str(0)+str(List[k])+'D')
        else:
            List2.append(str(List[k])+'D')    

    for q in range (0,13):
        if q<8:
            List3.append(str(0)+str(List[q])+'S')
        else:
            List3.append(str(List[q])+'S') 

    for m in range (0,13):
        if m<8:
            List4.append(str(0)+str(List[m])+'C')
        else:
            List4.append(str(List[m])+'C')     
    deck=List1+List2+List3+List4
    return deck


def player_hand(deck,List6,n,player_names):
    global l
    global o
    for p in range(1,n+1):
        l= random.choice(deck)
        o=random.choice(deck)
        print(player_names[p-1],"=", l,o )
        deck.remove(l)
        deck.remove(o)
        List6.append(l)
        List6.append(o)

    return deck,List6
        #table.append(l)
        #table.append(o)


#FLOP ROUND

def round1_reveal(deck,table):
    #global y
    #global x
    #global z
    y=random.choice(deck)
    x= random.choice(deck)
    z=random.choice(deck)
    deck.remove(y)
    deck.remove(x)
    deck.remove(z)
    table.append(y)
    table.append(x)
    table.append(z)
    return deck,table



#TURN ROUND

def round2_reveal(deck,table):
    w= random.choice(deck)
    deck.remove(w)
    table.append(w)
    return deck,table
 


#RIVER ROUND

def round3_reveal(deck,table):
    v= random.choice(deck)
    deck.remove(v)
    table.append(v)
    return deck,table


#Cards on the table

#def table_cards():
    #table.append(l)
    #table.append(o)
    #table.append(y)
    #table.append(x)
    #table.append(z)
    #table.append(w)
    #table.append(v)
