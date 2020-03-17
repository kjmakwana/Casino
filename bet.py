import tkinter as tk
import math



main_window = tk.Tk()
main_window.title("Poker")


purse=[]
n=int(input("Enter number of players: "))


for j in range (0,n):       #n is number of players
    purse.append(100000)


current_bet=1000

def blinds():
    for j in range(0,n):
        purse[j]-=current_bet
blinds()


c=0


def player_change():
    global c    
    c=c+1
    global player_no
    player_no = c%n
    if c%n==0:
        player_no=n
    print("Ït is player",player_no,"s turn")
    global i
    i=player_no-1

player_change()


def bet(player_purse ,current_bet):   #player_purse is the amount in the purse of the player who wants to raise
    while(True):
        max_raise=min(purse)
        print("Enter ampount to raise")
        print("Amount must be a multiple of $1000 and less than or equal to the amount of money in the player's purse having least money")
        print("It must be more than the current bet amount which is $",current_bet)
        print("Your current purse is $",player_purse)
        r=int(input("enter amount: $"))
        if r<=max_raise and r%1000==0 and r>current_bet:
            player_purse-=r
            current_bet=r
            break
        else:
            print("Please enter valid bet")
    player_change()
    return player_purse,current_bet

def call_bet():
    global i,current_bet
    purse[i],current_bet=bet(purse[i],current_bet)
    print("player",player_no,"s purse =",purse[i])
    print("Current bet is $",current_bet)

def call(player_purse, current_bet):
    global i
    print("Player",i+1,"has called")
    purse[i]-=current_bet
    print("Player",i+1,"s current purse = $",purse[i])

def check():
    global i
    print("Player",i+1,"has checked")
    player_change()

def fold():
    global i
    print("Player",i+1,"has folded")
    player_change()
    #empty out the list having the cards of the player who wants to fold   

def call_check():
    check()
    

def call_fold():
    fold()

def call_call():
    global i
    call(purse[i],3000)
    



bet_button=tk.Button(main_window,text="Raise",command=call_bet,fg='white',bg='black')
check_button=tk.Button(main_window,text="Check",command=call_check)
fold_button=tk.Button(main_window,text="Fold",command=call_fold)
call_button=tk.Button(main_window,text="Call",command=call_call)
bet_button.pack()
check_button.pack()
fold_button.pack()
call_button.pack()
main_window.mainloop()





