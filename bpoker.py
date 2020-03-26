from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import generationofcards as goc
import botres as res
import FinalResult as fr
import Bot
import gui
import time

hand_dict11= {11:"Folded",1:"Royal-Flush", 2:"Straight-Flush", 3:"Four-of-a-Kind", 4:"Full-HHouse", 5:"Flush", 6:"Straight", 7:"Three-of-a-Kind", 8:"Two-Pairs", 9:"One-Pair", 10:"Highest-Card"}

List= []
List1=[] 
List2=[]
List3=[]
List4=[]
deck=[]
deck1=[]
List6=[]
table=[]
debt=[]

x1=600
y1=450
rf=True

player_names=[]
player_who_have_folded=[]
cc=0
chc=0
rc=0
b=0
r=[0,0,0,0,0,0,0,0]
purse=[]
rno=2

round_pool=0
current_bet=1000
t=1000
c=0
round_no=0
dollar=0

results=[]
main_window = Tk()
main_window.title("Poker")
main_window['bg']='green'

slider=Scale()
submit=Scale()

n=0
qs="Yes"

def takeinput():
    global n
    n=simpledialog.askinteger("Number of players","Enter number of players")

def takeinputbot():
    global qs
    qs=messagebox.askyesno("Bot inclusion","Do you wish to include a bot")

takeinputbot()
takeinput()

for j in range (0,n):       #to input player names
    print("Player ",j+1,":",end="")
    name=simpledialog.askstring("Names","Please enter name of Player"+str(j+1))
    player_names.append(name) 
    print()
if(qs==True):
    player_names.append("BOT")
    n+=1

for j in range (0,n):       #n is number of players
    purse.append(100000)
    debt.append(0)

def blinds():
    global round_pool
    print("Player Purses are")
    for j in range(0,n):
        purse[j]-=current_bet
        round_pool+=current_bet
        print(player_names[j],":",purse[j])
blinds()


deck,deck1=goc.card_deck(List,List1,List2,List3,List4,deck)
deck,List6=goc.player_hand(deck,List6,n,player_names)

def round_number():
    global round_no,deck,table,results,deck1,x1,y1,call_button
    round_no+=1
    call_button.destroy()
    if(round_no%4==1):
        deck,table=goc.round1_reveal(deck,table)
        x1,y1=gui.flop_reveal(table,deck1,x1,y1)
        print(table)
    elif(round_no%4==2):
        deck,table=goc.round2_reveal(deck,table)
        x1,y1=gui.turn_reveal(table,deck1,x1,y1)
        print(table)
    elif(round_no%4==3):
        deck,table=goc.round3_reveal(deck,table)
        x1,y1=gui.river_reveal(table,deck1,x1,y1)
        print(table)
    elif(round_no%4==0):
        gui.finaldisplay(x1,y1,List6,n,deck1,player_names)
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
            messagebox.showinfo(title="Paisa hi paisa hoga",message="Winner of the current round is "+player_names[results.index(min(results))]+"\n"+"Winning Hand = "+str(hand_dict11[min(results)]))
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
                messagebox.showinfo(title="Paisa hi paisa hoga",message="Winner of the current round is "+player_names[fplayer]+"\n"+"Winning Hand = Better "+str(hand_dict11[min(results)]))
                purse[fplayer]+=round_pool
                print(purse[fplayer])
            else:
                print("The pot is split in between ",end="")
                
                split=set(split)
                for s in split:
                    print(player_names[s],end="  ")
                    purse[s]+=int(round_pool/len(split))
                    print(purse[s])
                    winnerw=winnerw+player_names[s]+" "
                messagebox.showinfo(title="Paisa hi paisa hoga",message="The pot is split between"+winnerw)


        reset()

def player_change():
    global x1,y1
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
    
    tpot=Label(text="Pot= $"+str(round_pool)+"            ",fg="white",bg="green")
    tpot.config(font=("Courier BOLD", 15))
    tpot.place(x=500,y=50)

    tbet=Label(text="Current Bet= $"+str(current_bet)+"           ",fg="white",bg="green")
    tbet.config(font=("Courier BOLD", 15))
    tbet.place(x=800,y=50)

    if player_names not in player_who_have_folded:
        x1,y1=gui.player_reveal(List6[2*i:2*i+2],deck1,x1,y1)
        pname=Label(text="Current Player: "+player_names[i]+"                       ",fg="white",bg="green")
        pname.config(font=("Courier BOLD", 15))
        pname.place(x=570,y=600)

    yy1=10
    for j in range(n):
        ppurse=Label(text=player_names[j]+"= $"+str(purse[j])+"        ",fg="white",bg="green")
        ppurse.config(font=("Courier BOLD", 12))
        ppurse.place(x=1300,y=yy1)
        yy1=yy1+25

    if(player_names[i]=="BOT"):
        Bot.head(round_no,current_bet,List6[-2:],table,deck,chc,player_who_have_folded,n)
    else:
        print("It is",player_names[i],"'s turn")
        print("Current Bet is $",current_bet)
        print("Money in pot is $",round_pool)

player_change()

def reset():

    global List,List1,List2,List3,List4,List6,deck,table,round_pool,round_no,current_bet,cc,chc,rc,player_who_have_folded,b,c,results,x1,y1,player_names,n,purse,rno
    l=0
    while(l!=n):
        if(purse[l]<=0):
            purse[l]+=100000
            player_names[l]+="*"
            debt[l]-=100000
            print(purse)
        l=l+1

    gui.reset(x1,y1,n,rno)
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
    rno+=1

    status1="                                                  "
    status=Label(text=status1)    
    status.config(font=("Courier BOLD", 15),bg="green",fg="white")
    status.place(x=570,y=360)

    current_bet=1000
    print()
    print()
    
    deck=List1+List2+List3+List4
    blinds()
    deck,List6=goc.player_hand(deck,List6,n,player_names)
    #player_change()




def bet(player_purse ,current_bet,bet_amount,i,dollar):   
    global round_pool,b,chc,cc,r,call_button,check_button
    cc=0
    chc=0

    if(bet_amount==0):
        while(True):
            print("Enter amount to raise")
            print("Amount must be a multiple of $1000")
            print("It must be more than the current bet which is $",current_bet)
            print("Your current purse is $",player_purse)
            dollar=int(dollar)
            if dollar<=player_purse and dollar%1000==0 and dollar>=current_bet:
                player_purse-=dollar
                round_pool+=dollar
                b=1
                r[i]=dollar
                current_bet=dollar
                break
                
    else:
        print("Bot has raised ",bet_amount)
        player_purse-=bet_amount
        round_pool+=bet_amount
        b=1
        current_bet=bet_amount
        r[i]=current_bet

    call_button.destroy()
    call_button=Button(text="Call ",command=call_call,padx=20,pady=10,bg="#006600",fg="white",width=5)
    call_button.config(font=("Courier BOLD", 12))
    call_button.place(x=1100,y=550)
    status1=player_names[i]+" has raised $"+str(current_bet)+"    "
    status=Label(text=status1)
    for cbc in range(1000):
        check_button.destroy()
    
    status.config(font=("Courier BOLD", 15),bg="green",fg="white")
    status.place(x=570,y=360)

    return player_purse,current_bet

def call(player_purse, current_bet):
    global i,cc,round_pool,purse,rc,call_button,check_button
    rc=0
    print(player_names[i],"has called")

    status1=player_names[i]+" has called                                       "
    status=Label(text=status1)    
    status.config(font=("Courier BOLD", 15),bg="green",fg="white")
    status.place(x=570,y=360)

    purse[i]-=max(r)-r[i]
    round_pool+=max(r)-r[i]
    print(player_names[i],"'s current purse = $",purse[i])
    cc+=1
    if cc==(len(player_names)-len(player_who_have_folded)-1):
        cc=0
        check_button=Button(text="Check",command=call_check,padx=20,pady=10,bg="#006600",fg="white")
        check_button.place(x=1000,y=600)
        check_button.config(font=("Courier BOLD", 12))
        round_number()
    player_change()

def check():
    global i,chc,b,check_button
    print(player_names[i],"has checked") 
    
    status1=player_names[i]+" has checked                                   "
    status=Label(text=status1)    
    status.config(font=("Courier BOLD", 15),bg="green",fg="white")
    status.place(x=570,y=360)

    chc+=1
    b=0

    if chc==(len(player_names)-len(player_who_have_folded)):
        chc=0
        check_button=Button(text="Check",command=call_check,padx=20,pady=10,bg="#006600",fg="white")
        check_button.place(x=1000,y=600)
        check_button.config(font=("Courier BOLD", 12))
        round_number()
    player_change()

def fold():
    global i,chc,cc,check_button
    print(player_names[i],"has folded")
    
    status1=player_names[i]+" has folded                                     "
    status=Label(text=status1)    
    status.config(font=("Courier BOLD", 15),bg="green",fg="white")
    status.place(x=570,y=360)

    player_who_have_folded.append(player_names[i])
    if(len(player_who_have_folded)-len(player_names)==-1):
        all_fold=list(set(player_names)-set(player_who_have_folded))
        print("Winner is ",all_fold[0])
        messagebox.showinfo(title="Paise hi paisa hoga",message="winner of the current round is "+all_fold[0]+"\n"+"All others have folded")
        purse[player_names.index(all_fold[0])]+=round_pool
        print(purse[player_names.index(all_fold[0])])
        reset()
    if chc==(len(player_names)-len(player_who_have_folded)):
        chc=0
        check_button=Button(text="Check",command=call_check,padx=20,pady=10,bg="#006600",fg="white")
        check_button.place(x=1000,y=600)
        check_button.config(font=("Courier BOLD", 12))
        round_number()
    if cc==(len(player_names)-len(player_who_have_folded)-1):
        cc=0
        check_button=Button(text="Check",command=call_check,padx=20,pady=10,bg="#006600",fg="white")
        check_button.place(x=1000,y=600)
        check_button.config(font=("Courier BOLD", 12))
        round_number()
    player_change()
  

def show(val):
    global t
    t=val

def call_bet(bet_amount=0):
    k=0
    print(bet_amount)
    global dollar,i,current_bet,slider,submit,purse
    if(bet_amount==0):
        slider=Scale(from_=current_bet, to=purse[i], resolution=1000,orient=VERTICAL,length=150,tickinterval=1000,command=show)
        slider.config(bg="#006600",fg="white",font=("Courier BOLD", 12))
        slider.place(x=1200,y=500)

        submit=Button(text="Place",command=lambda: submitbet(t,bet_amount),padx=20,pady=10,bg="#006600",fg="white")
        submit.place(x=1350,y=500)
    else:
        purse[i],current_bet=bet(purse[i],current_bet,bet_amount,i,dollar)
        player_change()




def submitbet(b,bet_amount):
    global k,dollar,purse,current_bet,slider,submit
    k=1
    print(k)
    dollar=b
    print(dollar)
    if k==1:
        purse[i],current_bet=bet(purse[i],current_bet,bet_amount,i,dollar)
        print(player_names[i],"'s purse =",purse[i])
        print("Current bet is $",current_bet) 
        player_change()
    slider.destroy()
    submit.destroy()

def call_check():
    check()
    
def call_fold():
    fold()

def call_call():
    global i,current_bet
    call(purse[i],current_bet)

bet_button=Button(text="Raise",command=call_bet,padx=20,pady=10,bg="#006600",fg="white")
check_button=Button(text="Check",command=call_check,padx=20,pady=10,bg="#006600",fg="white")
fold_button=Button(text="Fold ",command=call_fold,padx=20,pady=10,bg="#006600",fg="white",width=5)
call_button=Button(text="Call ",command=call_call,padx=20,pady=10,bg="#006600",fg="white",width=5)

bet_button.config(font=("Courier BOLD", 12))
check_button.config(font=("Courier BOLD", 12))
fold_button.config(font=("Courier BOLD", 12))
call_button.config(font=("Courier BOLD", 12))

bet_button.place(x=1100,y=600)
check_button.place(x=1000,y=600)
fold_button.place(x=1000,y=550)

mainloop()
