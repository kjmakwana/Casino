#Result

#FinalResult
import tkinter as tk
import generationofcards as goc
import botres as res
import FinalResult as fr
List= []
List1=[] 
List2=[]
List3=[]
List4=[]
deck=[]
List6=[]
table=[]


player_names=[]
player_who_have_folded=[]
cc=0
chc=0
b=0
purse=[]

round_pool=0
current_bet=1000

c=0
round_no=0

results=[]
#Tkinter
main_window = tk.Tk()
main_window.title("Poker")
#main_window.iconbitmap("C:/Users/sgmakwana/Downloads/poker_chip2.ico")
main_window['bg']='green'










# Beginning of bet

n=int(input("Enter number of players "))
print("Enter names of players")
for j in range (0,n):       #to input player names
    print("Player ",j+1,":",end="")
    name=input()
    player_names.append(name) 
    print()

for j in range (0,n):       #n is number of players
    purse.append(100000)

def blinds():
    global round_pool
    print("Player Purses are")
    for j in range(0,n):
        purse[j]-=current_bet
        round_pool+=current_bet
        print(player_names[j],":",purse[j])
blinds()


#End of bet


deck=goc.card_deck(List,List1,List2,List3,List4,deck)
deck,List6=goc.player_hand(deck,List6,n,player_names)


def round_number():
    global round_no,deck,table,results
    round_no+=1
    if(round_no==1):
        deck,table=goc.round1_reveal(deck,table)
        print(table)
    elif(round_no==2):
        deck,table=goc.round2_reveal(deck,table)
        print(table)
    elif(round_no==3):
        deck,table=goc.round3_reveal(deck,table)
        print(table)
    elif(round_no==4):
        destroy()
        for j in range(0,2*n,2):
            if(player_names[int(j/2)] not in player_who_have_folded):
                cards=[]
                cards.append(List6[j])
                cards.append(List6[j+1])
                cards+=table
                results.append(res.find_rank(cards))
        print(results)

        if(results.count(min(results))==1):
            print("Winner is",player_names[results.index(min(results))])
        else:
            fcards=[]
            count=0
            fplayer=0
            splayer=0
            for j in range(len(results)):
                if(results[j]==min(results)):
                    cards1=[]
                    cards1.append(List6[2*j])
                    cards1.append(List6[2*j+1])
                    cards1+=table
                    count+=1
                    splayer=j
                fcards+=cards1
                if(count==1):
                    fplayer=splayer
                elif(count==2):
                    count=1
                    w_player=fr.xyz(fcards,min(results))
                    if(w_player==1):
                        del(fcards[5:])
                        fplayer=fplayer
                    else:
                        del(fcards[0:5])
                        fplayer=splayer
                print("Winner is", fplayer)





        

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
        print("It must be more than the current bet which is $",current_bet)
        print("Your current purse is $",player_purse)
        r=int(input("enter amount: $"))
        if r<=player_purse and r%1000==0 and r>=current_bet:
            player_purse-=current_bet
            round_pool+=current_bet
            b=1
            current_bet=r
            break
        else:
            print("Please enter valid bet")
    call_button.grid(row=1,column=0)
    check_button.destroy()
    return player_purse,current_bet

def call(player_purse, current_bet):
    global i,cc,round_pool,purse
    print(player_names[i],"has called")
    purse[i]-=current_bet
    round_pool+=current_bet
    print(player_names[i],"'s current purse = $",purse[i])
    cc+=1
    if cc==(len(player_names)-len(player_who_have_folded)-1):
        cc=0
        check_button=tk.Button(main_window,text="Check",command=call_check)
        check_button.grid(row=0,column=1)
        round_number()
    player_change()

def check():
    global i,chc,b
    print(player_names[i],"has checked")
    chc+=1
    b=0
    if chc==(len(player_names)-len(player_who_have_folded)):
        chc=0
        check_button=tk.Button(main_window,text="Check",command=call_check)
        check_button.grid(row=0,column=1)
        round_number()
    player_change()

def fold():
    global i,chc,cc
    print(player_names[i],"has folded")
    player_who_have_folded.append(player_names[i])
    if chc==(len(player_names)-len(player_who_have_folded)):
        chc=0
        check_button=tk.Button(main_window,text="Check",command=call_check)
        check_button.grid(row=0,column=1)
        round_number()
    if cc==(len(player_names)-len(player_who_have_folded)-1):
        cc=0
        check_button=tk.Button(main_window,text="Check",command=call_check)
        check_button.grid(row=0,column=1)
        round_number()
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


def destroy():
    main_window.destroy()
bet_button=tk.Button(main_window,text="Raise",command=call_bet)
check_button=tk.Button(main_window,text="Check",command=call_check)
fold_button=tk.Button(main_window,text="Fold",command=call_fold)
call_button=tk.Button(main_window,text="Call",command=call_call)


bet_button.grid(row=0,column=0)
check_button.grid(row=0,column=1)
fold_button.grid(row=1,column=1)



main_window.mainloop()
