#Result

#FinalResult
import tkinter as tk
import generationofcards as goc
import botres as res
import FinalResult as fr
import Bot
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
rc=0
b=0
r=[0,0,0,0,0,0,0,0]
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
qs=int(input("Do you wish to include a bot "))

n=int(input("Enter number of players "))
print("Enter names of players")
for j in range (0,n):       #to input player names
    print("Player ",j+1,":",end="")
    name=input()
    player_names.append(name) 
    print()
if(qs==1):
    player_names.append("BOT")
    n+=1

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


deck=goc.card_deck(List,List1,List2,List3,List4,deck)
print(deck)
deck,List6=goc.player_hand(deck,List6,n,player_names)


def round_number():
    global round_no,deck,table,results
    round_no+=1
    if(round_no%4==1):
        deck,table=goc.round1_reveal(deck,table)
        print(table)
    elif(round_no%4==2):
        deck,table=goc.round2_reveal(deck,table)
        print(table)
    elif(round_no%4==3):
        deck,table=goc.round3_reveal(deck,table)
        print(table)
    elif(round_no%4==0):
        
        for j in range(0,2*n,2):
            if(player_names[int(j/2)] not in player_who_have_folded):
                cards=[]
                cards.append(List6[j])
                cards.append(List6[j+1])
                cards+=table
                flag=0
                results.append(res.find_rank(cards,flag))
            else:
                results.append(11)
        print(results)
        if(results.count(min(results))==1):
            print("Winner is",player_names[results.index(min(results))])
            purse[results.index(min(results))]+=round_pool
            print(purse[results.index(min(results))])
        else:
            fcards=[]
            cards1=[]
            split=[]
            count=0
            fplayer=0
            splayer=0
            print()
            print()
            for j in range(len(results)):
                if(results[j]==min(results)):
                    flag=1
                    cards1=[]
                    cards1.append(List6[2*j])
                    cards1.append(List6[2*j+1])
                    cards1+=table
                    cards1=res.find_rank(cards1,flag)
                    count+=1
                    if(count==1):
                        fplayer=splayer
                    splayer=j
                    fcards+=cards1
                print(fcards)

                
                if(count==2):
                    count=1
                    w_player=fr.xyz(fcards,min(results))
                    if(w_player==1):
                        del fcards[5:]
                        fplayer=fplayer
                    elif(w_player==2):
                        del fcards[0:5]
                        fplayer=splayer
                    else:
                        del fcards[0:5]
                        split.append(fplayer)
                        split.append(splayer)

            if(fplayer not in split):
                print("Winner is", player_names[fplayer])
                purse[fplayer]+=round_pool
                print(purse[fplayer])
            else:
                print("The pot is split in between ",end="")
                split=set(split)
                for s in split:
                    print(player_names[s],end="  ")
                    purse[s]+=int(round_pool/len(split))
                    print(purse[s])


        reset()

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
    if(player_names[i]=="BOT"):
        Bot.head(round_no,current_bet,List6[-2:],table,deck,chc,player_who_have_folded,n)
    else:
        print("It is",player_names[i],"'s turn")
        print("Current Bet is $",current_bet)
        print("Money in pot is $",round_pool)

player_change()

def reset():

    global List,List1,List2,List3,List4,List6,deck,table,round_pool,round_no,current_bet,cc,chc,rc,player_who_have_folded,b,c,results
    List6=[]
    deck=[]
    table=[]
    results=[]
    player_who_have_folded=[]
    results=[]
    r=[0,0,0,0,0,0,0,0]
    round_pool=0
    round_no=0
    cc=0
    chc=0
    rc=0
    b=0
    c=0
    current_bet=1000
    print()
    print()
    deck=List1+List2+List3+List4
    blinds()
    deck,List6=goc.player_hand(deck,List6,n,player_names)
    #player_change()


def bet(player_purse ,current_bet,bet_amount,i):   #player_purse is the amount in the purse of the player who wants to raise
    global round_pool,b,chc,cc,r
    cc=0
    chc=0
    if(bet_amount==0):
        while(True):
            print("Enter amount to raise")
            print("Amount must be a multiple of $1000")
            print("It must be more than the current bet which is $",current_bet)
            print("Your current purse is $",player_purse)
            dollar=int(input("enter amount: $"))
            if dollar<=player_purse and dollar%1000==0 and dollar>current_bet:
                player_purse-=dollar
                round_pool+=dollar
                b=1
                r[i]=dollar
                current_bet=dollar
                break
            else:
                print("Please enter valid bet")
    else:
        print("Bot has raised ",bet_amount)
        player_purse-=bet_amount
        round_pool+=bet_amount
        b=1
        current_bet=bet_amount

    call_button.grid(row=1,column=0)
    check_button.destroy()
    return player_purse,current_bet

def call(player_purse, current_bet):
    global i,cc,round_pool,purse,rc
    rc=0
    print(player_names[i],"has called")
    print(max(r))
    purse[i]-=max(r)-r[i]
    round_pool+=max(r)-r[i]
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
    if(len(player_who_have_folded)-len(player_names)==-1):
        all_fold=list(set(player_names)-set(player_who_have_folded))
        print("Winner is ",all_fold[0])
        purse[player_names.index(all_fold[0])]+=round_pool
        print(purse[player_names.index(all_fold[0])])
        reset()
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

def call_bet(bet_amount=0):
    global i,current_bet
    purse[i],current_bet=bet(purse[i],current_bet,bet_amount,i)
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




bet_button=tk.Button(main_window,text="Raise",command=call_bet)
check_button=tk.Button(main_window,text="Check",command=call_check)
fold_button=tk.Button(main_window,text="Fold",command=call_fold)
call_button=tk.Button(main_window,text="Call",command=call_call)


bet_button.grid(row=0,column=0)
check_button.grid(row=0,column=1)
fold_button.grid(row=1,column=1)



main_window.mainloop()
