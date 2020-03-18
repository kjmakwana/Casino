import tkinter as tk
import math



main_window = tk.Tk()
main_window.title("Poker")



player_names=[]
player_who_have_folded=[]
cc=0
chc=0
b=0




purse=[]
n=int(input("Enter number of players: "))


for j in range (0,n):       #n is number of players
    purse.append(100000)


print("Enter names of players")
for j in range (0,n):       #to input player names
    print("Player ",j+1,":",end="")
    name=input()
    player_names.append(name) 
    print()
players_in_current_round=player_names

round_pool=0
current_bet=1000

def blinds():
    global round_pool
    print("Player Purses are")
    for j in range(0,n):
        purse[j]-=current_bet
        round_pool+=current_bet
        print(player_names[j],":",purse[j])
        
blinds()


c=0




def player_change():
    while True:
        global c,i    
        c=c+1
        global player_no
        player_no = c%n
        if c%n==0:
            player_no=n
        i=player_no-1
        if player_names[i] in player_who_have_folded:
            continue
        else:
            break
    print("It is",player_names[i],"'s turn")
    print("Current Bet is $",current_bet)
    print("Money in pot is $",round_pool)
    

player_change()


def bet(player_purse ,current_bet):   #player_purse is the amount in the purse of the player who wants to raise
    global round_pool,b
    while(True):
        print("Enter amount to raise")
        print("Amount must be a multiple of $1000")
        print("It must be more than the current money in the pot which is $",round_pool)
        print("Your current purse is $",player_purse)
        current_bet=int(input("enter amount: $"))
        if current_bet<=player_purse and current_bet%1000==0 and current_bet>=round_pool:
            player_purse-=current_bet
            round_pool+=current_bet
            b=1
            break
        else:
            print("Please enter valid bet")
    return player_purse,current_bet

def call(player_purse, current_bet):
    global i,cc,round_pool,purse
    print(player_names[i],"has called")
    purse[i]-=current_bet
    round_pool+=current_bet
    print(player_names[i],"'s current purse = $",purse[i])
    cc+=1
    if cc==(len(player_names)-len(player_who_have_folded)):
        cc=0
        #distribute next set of cards
    player_change()

def check():
    global i,chc,b
    print(player_names[i],"has checked")
    chc+=1
    b=0
    if chc==(len(player_names)-len(player_who_have_folded)):
        chc=0
        #distribute next set of cards
    player_change()

def fold():
    global i
    print(player_names[i],"has folded")
    player_who_have_folded.append(player_names[i])
    player_change()
    #empty out the list having the cards of the player who wants to fold  

def call_bet():
    global i,current_bet
    purse[i],current_bet=bet(purse[i],current_bet)
    print(player_names[i],"'s purse =",purse[i])
    print("Current bet is $",current_bet) 
    player_change()

def call_check():
    check()
    

def call_fold():
    fold()

def call_call():
    global i,current_bet
    call(purse[i],current_bet)




bet_button=tk.Button(main_window,text="Raise",command=call_bet,fg='white',bg='black')
check_button=tk.Button(main_window,text="Check",command=call_check)
fold_button=tk.Button(main_window,text="Fold",command=call_fold)
call_button=tk.Button(main_window,text="Call",command=call_call)


bet_button.pack()
check_button.pack()
fold_button.pack()
call_button.pack()


main_window.mainloop()





