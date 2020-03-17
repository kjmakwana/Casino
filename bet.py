import tkinter as tk
import math

main_window = tk.Tk()
main_window.title("Poker")

purse=[]                    #list will store the money in the purse of each player
player_names=[]

n=int(input("Enter number of players: "))

print("Enter names of players")
for j in range (0,n):       #to input player names
    print("Player ",j+1,":",end="")
    name=input()
    player_names.append(name) 
    print()

current_game={}             #this dict will store the names and the purse of the plauers in the game

for j in range (0,n):       #to fill purse initially at the start of each gaem
    purse.append(100000)

for j in range (0,n):
    current_game[player_names[j]]=purse[j]

current_bet=1000
pool=0
b=0                         #bet count
c=0                         #count variable
cc=0                        #call count
chc=0                       #check count
round_pool=0                #amount in the pool for the current round of cards
current_round={}            #this dictionary will hold the players cuurntly playing in the round(who have not folded) and their respective purse
players_in_current_round=[]     #this list will hold the keys of the above dictionary

for j in range(0,n):
    current_round[player_names[j]]=purse[j]

def players_in_current_round_func():
    players_in_current_round.clear()
    for keys in current_round:
        players_in_current_round.append(keys)  
players_in_current_round_func()  

def reset():                #this function will be called after every the result is displayed
    global current_bet,pool,c,cc,chc,round_pool
    current_bet=1000
    pool=0
    c=0                         #count variable
    cc=0                        #call count
    chc=0                       #check count 
    round_pool=0
    for j in range (0,n):
        current_game[player_names[j]]=purse[j]
    
def blinds():               #to subtract blinds
    global pool,round_pool
    for j in range(0,n):
        current_round[player_names[j]]-=current_bet
        pool+=current_bet
        round_pool=pool
blinds()

def player_change():        #to maintain player turns
    global c,player_no,i
    c=c+1 
    player_no = c%len(current_round)
    i=player_no-1
    print("Ït is ",players_in_current_round[i],"'s turn")
player_change()

def bet(player_purse ,current_bet):     #if the player wants to bet
    global cc,chc,b
    cc=0
    chc=0
    while(True):
        print("Enter amount to bet")
        print("Amount must be a multiple of $1000")
        print("It must at least be the current pool amount which is $",current_bet)
        print("Your current purse is $",player_purse)
        current_bet=int(input("enter amount: $"))
        if current_bet>=round_pool and current_bet%1000==0 and current_bet<=player_purse:
            player_purse-=current_bet
            player_who_bet=i
            b=1
            break
        else:
            print("Please enter valid bet")
    player_change()
    return player_purse,current_bet

def call(player_purse, current_bet):            #if the player wants to call        
    global i,pool,cc,round_pool,b
    cc+=1
    print(players_in_current_round[i],"has called")
    print("current bet is $",current_bet)
    current_round[player_names[i]]-=current_bet
    pool+=current_bet
    print("Money in the pool is $",pool)
    print(players_in_current_round[i],"'s current purse = $",current_round[player_names[i]])
    if cc==len(current_round):
        #distribute next set of cards
        b=0
        cc=0
        round_pool=0
    player_change()

def check():                                    #if the player wants to check
    global i,chc,round_pool,b
    chc+=1
    print(players_in_current_round[i],"has checked")
    print("Money in the pool is $",pool)
    if chc==len(current_round):
        #distribute next set of cards
        b=0
        chc=0
        round_pool=0
    player_change()

def fold():                                     #if the palyer wants to fold
    global i,n,c
    print(players_in_current_round[i],"has folded")
    print("Money in the pool is $",pool)
    current_game[player_names[i]]=current_round[player_names[i]]
    del current_round[player_names[i]]
    players_in_current_round_func()
    c-=n-len(current_round)
    player_change()
    #empty out the list having the cards of the player who wants to fold   

def call_bet():                                 #to call the bet function
    global i,current_bet
    purse[i],current_bet=bet(purse[i],current_bet)
    print(player_names[i],"'s purse =",purse[i])
    print("Current bet is $",current_bet)

def call_check():                               #to call the check function
    check()
    
def call_fold():                                #to call the fold function
    fold()

def call_call():                                #to call the call function
    global i
    call(purse[i],3000)
    

#following statements are for gui

bet_button=tk.Button(main_window,text="Bet",command=call_bet,fg='white',bg='black')
check_button=tk.Button(main_window,text="Check",command=call_check)
fold_button=tk.Button(main_window,text="Fold",command=call_fold)
call_button=tk.Button(main_window,text="Call",command=call_call)

bet_button.pack()
if b!=1:
    check_button.pack()
fold_button.pack()
call_button.pack()

main_window.mainloop()