import math

purse=[]
n=int(input("Enter number of players: "))


for i in range (0,n):       #n is number of players
    purse.append(100000)
#print(purse)



def blinds():
    for i in range(0,n):
        purse[i]-=1000
    

def bet(player_purse ,current_bet):   #player_purse is the amount in the purse of the player who wants to raise
    while(True):
        max_raise=min(purse)
        print("Enter ampount to raise")
        print("Amount must be a multiple of $1000 and less than or equal to the amount of money in the player's purse having least money")
        r=int(input("enter amount: "))
        if r<=max_raise and r%1000==0 and r>current_bet:
            player_purse-=r
            break
        else:
            print("Please enter valid bet")
    return player_purse

blinds()
purse[2]=bet(purse[2],2000)
print(purse[2])

    
