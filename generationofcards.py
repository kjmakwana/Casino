import random
def card_deck(List,List1,List2,List3,List4,deck):                                                           
    for j in range(0,13):
        if j<8:
            List1.append(str(0)+str(j+2)+'C')
        else:
            List1.append(str(j+2)+'C')

    for k in range (0,13):
        if k<8:
            List2.append(str(0)+str(k+2)+'S')
        else:
            List2.append(str(k+2)+'S')    

    for q in range (0,13):
        if q<8:
            List3.append(str(0)+str(q+2)+'H')
        else:
            List3.append(str(q+2)+'H') 

    for m in range (0,13):
        if m<8:
            List4.append(str(0)+str(m+2)+'D')
        else:
            List4.append(str(m+2)+'D')     
    deck=List1+List2+List3+List4
    deck1=List1+List2+List3+List4
    return deck,deck1

card_deck([],[],[],[],[],[])
def player_hand(deck,List6,n,player_names):
    for p in range(1,n+1):
        l=random.choice(deck)
        deck.remove(l)
        o=random.choice(deck)
        deck.remove(o)
        if(player_names[p-1]=="BOT"):
            print(player_names[p-1],"=",l,o)
        else:
            print(player_names[p-1],"=", l,o )
        List6.append(l)
        List6.append(o)

    return deck,List6

def round1_reveal(deck,table):
    y=random.choice(deck)
    deck.remove(y)
    x=random.choice(deck)
    deck.remove(x)
    z=random.choice(deck)
    deck.remove(z)
    table.append(y)
    table.append(x)
    table.append(z)
    return deck,table

def round2_reveal(deck,table):
    w= random.choice(deck)
    deck.remove(w)
    table.append(w)
    return deck,table
 
def round3_reveal(deck,table):
    v= random.choice(deck)
    deck.remove(v)
    table.append(v)
    return deck,table


