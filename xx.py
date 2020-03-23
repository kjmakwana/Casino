from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()

#import random

n=int(input("Enter the number of players: "))

List= []

List1=[] 

List2=[]

List3=[]

List4=[]

#List 5 for 1 deck
deck=[]

#List6 for storing the cards of players
List6=[]

#Table for cards on the table
table=[]

deck1=[]

for i in range(2,15):
    List.append(i)                                                                

for j in range(0,13):
    if j<8:
        List1.append(str(0)+str(List[j])+'C')
    else:
        List1.append(str(List[j])+'C')

for k in range (0,13):
    if k<8:
        List2.append(str(0)+str(List[k])+'S')
    else:
        List2.append(str(List[k])+'S')    

for q in range (0,13):
    if q<8:
        List3.append(str(0)+str(List[q])+'H')
    else:
        List3.append(str(List[q])+'H') 

for m in range (0,13):
    if m<8:
        List4.append(str(0)+str(List[m])+'D')
    else:
        List4.append(str(List[m])+'D')     
deck=List1+List2+List3+List4
deck1=List1+List2+List3+List4

def player_hand():
    global l
    global o
    for p in range(1,n+1):
        l= random.choice(deck)
        o=random.choice(deck)
        print("player",p, "has", l,o )
        deck.remove(l)
        deck.remove(o)
        List6.append(l)
        List6.append(o)
player_hand()


#FLOP ROUND

def round1_reveal():
    global y
    global x
    global z
    y=random.choice(deck)
    x= random.choice(deck)
    z=random.choice(deck)
    print("Dealer has ",y,x,z)
    deck.remove(y)
    deck.remove(x)
    deck.remove(z)
round1_reveal() 


#TURN ROUND

def round2_reveal():
    global w
    w= random.choice(deck)
    print("Dealer has ",y,x,z,w)
    deck.remove(w)
round2_reveal()  


#RIVER ROUND

def round3_reveal():
    global v
    v= random.choice(deck)
    print("Dealer has ",y,x,z,w,v)
    deck.remove(v)
round3_reveal()

#Cards on the table

def table_cards():
    table.append(y)
    table.append(x)
    table.append(z)
    table.append(w)
    table.append(v)
table_cards()

x1=600
y1=450

    
def my_func2C():
    global my_img2
    my_img2=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2C.jpg"))
    my_label2=Label(root,image=my_img2)   
    my_label2.place(x=x1,y=y1)

def my_func3C():
    global my_img3
    my_img3=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3C.jpg"))
    my_label3=Label(image=my_img3)   
    my_label3.place(x=x1,y=y1)

def my_func4C():
    global my_img4
    my_img4=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4C.jpg"))
    my_label4=Label(image=my_img4)   
    my_label4.place(x=x1,y=y1)

def my_func5C():
    global my_img5
    my_img5=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5C.jpg"))
    my_label5=Label(image=my_img5)   
    my_label5.place(x=x1,y=y1)

def my_func6C():
    global my_img6
    my_img6=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6C.jpg"))
    my_label6=Label(image=my_img6)   
    my_label6.place(x=x1,y=y1)

def my_func7C():
    global my_img7
    my_img7=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7C.jpg"))
    my_label7=Label(image=my_img7)   
    my_label7.place(x=x1,y=y1)

def my_func8C():
    global my_img8
    my_img8=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8C.jpg"))
    my_label8=Label(image=my_img8)   
    my_label8.place(x=x1,y=y1)

def my_func9C():
    global my_img9
    my_img9=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9C.jpg"))
    my_label9=Label(image=my_img9)   
    my_label9.place(x=x1,y=y1)

def my_func10C():
    global my_img10
    my_img10=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10C.jpg"))
    my_label10=Label(image=my_img10)   
    my_label10.place(x=x1,y=y1)

def my_func11C():
    global my_img11
    my_img11=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JC.jpg"))
    my_label11=Label(image=my_img11)   
    my_label11.place(x=x1,y=y1)

def my_func12C():
    global my_img12
    my_img12=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QC.jpg"))
    my_label12=Label(image=my_img12)   
    my_label12.place(x=x1,y=y1)

def my_func13C():
    global my_img13
    my_img13=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KC.jpg"))
    my_label13=Label(image=my_img13)   
    my_label13.place(x=x1,y=y1)

def my_func14C():
    global my_img14
    my_img14=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AC.jpg"))
    my_label14=Label(image=my_img14)   
    my_label14.place(x=x1,y=y1)



def my_func2S():
    global my_img15
    my_img15=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2S.jpg"))
    my_label15=Label(image=my_img15)   
    my_label15.place(x=x1,y=y1)

def my_func3S():
    global my_img161
    my_img161=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3S.jpg"))
    my_label161=Label(image=my_img161)   
    my_label161.place(x=x1,y=y1)

def my_func4S():
    global my_img162
    my_img162=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4S.jpg"))
    my_label162=Label(image=my_img162)   
    my_label162.place(x=x1,y=y1)

def my_func5S():
    global my_img17
    my_img17=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5S.jpg"))
    my_label17=Label(image=my_img17)   
    my_label17.place(x=x1,y=y1)

def my_func6S():
    global my_img18
    my_img18=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6S.jpg"))
    my_label18=Label(image=my_img18)   
    my_label18.place(x=x1,y=y1)

def my_func7S():
    global my_img19
    my_img19=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7s.jpg"))
    my_label19=Label(image=my_img19)   
    my_label19.place(x=x1,y=y1)

def my_func8S():
    global my_img20
    my_img20=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8S.jpg"))
    my_label20=Label(image=my_img20)   
    my_label20.place(x=x1,y=y1)

def my_func9S():
    global my_img21
    my_img21=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9S.jpg"))
    my_label21=Label(image=my_img21)   
    my_label21.place(x=x1,y=y1)

def my_func10S():
    global my_img22
    my_img22=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10S.jpg"))
    my_label22=Label(image=my_img22)   
    my_label22.place(x=x1,y=y1)

def my_func11S():
    global my_img23
    my_img23=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JS.jpg"))
    my_label23=Label(image=my_img23)   
    my_label23.place(x=x1,y=y1)

def my_func12S():
    global my_img24
    my_img24=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QS.jpg"))
    my_label24=Label(image=my_img24)   
    my_label24.place(x=x1,y=y1)

def my_func13S():
    global my_img25
    my_img25=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KS.jpg"))
    my_label25=Label(image=my_img25)   
    my_label25.place(x=x1,y=y1)

def my_func14S():
    global my_img26
    my_img26=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AS.jpg"))
    my_labe26=Label(image=my_img26)   
    my_label26.place(x=x1,y=y1)



def my_func2H():
    global my_img27
    my_img27=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2H.jpg"))
    my_label27=Label(image=my_img27)   
    my_label27.place(x=x1,y=y1)

def my_func3H():
    global my_img28
    my_img28=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3H.jpg"))
    my_label28=Label(image=my_img28)   
    my_label28.place(x=x1,y=y1)

def my_func4H():
    global my_img29
    my_img29=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4H.jpg"))
    my_label29=Label(image=my_img29)   
    my_label29.place(x=x1,y=y1)

def my_func5H():
    global my_img30
    my_img30=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5H.jpg"))
    my_label30=Label(image=my_img30)   
    my_label30.place(x=x1,y=y1)

def my_func6H():
    global my_img31
    my_img31=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6H.jpg"))
    my_label31=Label(image=my_img31)   
    my_label31.place(x=x1,y=y1)

def my_func7H():
    global my_img32
    my_img32=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7H.jpg"))
    my_label32=Label(image=my_img32)   
    my_label32.place(x=x1,y=y1)

def my_func8H():
    global my_img33
    my_img33=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8H.jpg"))
    my_label33=Label(image=my_img33)   
    my_label33.place(x=x1,y=y1)

def my_func9H():
    global my_img34
    my_img34=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9H.jpg"))
    my_label34=Label(image=my_img34)   
    my_label34.place(x=x1,y=y1)

def my_func10H():
    global my_img35
    my_img35=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10H.jpg"))
    my_label35=Label(image=my_img35)   
    my_label35.place(x=x1,y=y1)

def my_func11H():
    global my_img36
    my_img36=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JH.jpg"))
    my_label36=Label(image=my_img36)   
    my_label36.place(x=x1,y=y1)

def my_func12H():
    global my_img37
    my_img37=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QH.jpg"))
    my_label37=Label(image=my_img37)   
    my_label37.place(x=x1,y=y1)

def my_func13H():
    global my_img38
    my_img38=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KH.jpg"))
    my_label38=Label(image=my_img38)   
    my_label38.place(x=x1,y=y1)

def my_func14H():
    global my_img39
    my_img39=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AH.jpg"))
    my_label39=Label(image=my_img39)   
    my_label39.place(x=x1,y=y1)



def my_func2D():
    global my_img40
    my_img40=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2D.jpg"))
    my_label40=Label(image=my_img40)   
    my_label40.place(x=x1,y=y1)

def my_func3D():
    global my_img41
    my_img41=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3D.jpg"))
    my_label41=Label(image=my_img41)   
    my_label41.place(x=x1,y=y1)

def my_func4D():
    global my_img42
    my_img42=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4D.jpg"))
    my_label42=Label(image=my_img42)   
    my_label42.place(x=x1,y=y1)

def my_func5D():
    global my_img43
    my_img43=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5D.jpg"))
    my_label43=Label(image=my_img43)   
    my_label43.place(x=x1,y=y1)

def my_func6D():
    global my_img44
    my_img44=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6D.jpg"))
    my_label44=Label(image=my_img44)   
    my_label44.place(x=x1,y=y1)

def my_func7D():
    global my_img45
    my_img45=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7D.jpg"))
    my_label45=Label(image=my_img45)   
    my_label45.place(x=x1,y=y1)

def my_func8D():
    global my_img46
    my_img46=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8D.jpg"))
    my_label46=Label(image=my_img46)   
    my_label46.place(x=x1,y=y1)

def my_func9D():
    global my_img47
    my_img47=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9D.jpg"))
    my_label47=Label(image=my_img47)   
    my_label47.place(x=x1,y=y1)

def my_func10D():
    global my_img48
    my_img48=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10D.jpg"))
    my_label48=Label(image=my_img48)   
    my_label48.place(x=x1,y=y1)

def my_func11D():
    global my_img49
    my_img49=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JD.jpg"))
    my_label49=Label(image=my_img49)   
    my_label49.place(x=x1,y=y1)

def my_func12D():
    global my_img50
    my_img50=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QD.jpg"))
    my_label50=Label(image=my_img50)   
    my_label50.place(x=x1,y=y1)

def my_func13D():
    global my_img51
    my_img51=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KD.jpg"))
    my_label51=Label(image=my_img51)   
    my_label51.place(x=x1,y=y1)

def my_func14D():
    global my_img52
    my_img52=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AD.jpg\"))
    my_label52=Label(image=my_img52)   
    my_label52.place(x=x1,y=y1)

List7=[]

List7.append(my_func2C)
List7.append(my_func3C)
List7.append(my_func4C)
List7.append(my_func5C)
List7.append(my_func6C)
List7.append(my_func7C)
List7.append(my_func8C)
List7.append(my_func9C)
List7.append(my_func10C)
List7.append(my_func11C)
List7.append(my_func12C)
List7.append(my_func13C)
List7.append(my_func14C)

List7.append(my_func2S)
List7.append(my_func3S)
List7.append(my_func4S)
List7.append(my_func5S)
List7.append(my_func6S)
List7.append(my_func7S)
List7.append(my_func8S)
List7.append(my_func9S)
List7.append(my_func10S)
List7.append(my_func11S)
List7.append(my_func12S)
List7.append(my_func13S)
List7.append(my_func14S)

List7.append(my_func2H)
List7.append(my_func3H)
List7.append(my_func4H)
List7.append(my_func5H)
List7.append(my_func6H)
List7.append(my_func7H)
List7.append(my_func8H)
List7.append(my_func9H)
List7.append(my_func10H)
List7.append(my_func11H)
List7.append(my_func12H)
List7.append(my_func13H)
List7.append(my_func14H)

List7.append(my_func2D)
List7.append(my_func3D)
List7.append(my_func4D)
List7.append(my_func5D)
List7.append(my_func6D)
List7.append(my_func7D)
List7.append(my_func8D)
List7.append(my_func9D)
List7.append(my_func10D)
List7.append(my_func11D)
List7.append(my_func12D)
List7.append(my_func13D)
List7.append(my_func14D)


print(List6)
print(table)


def player_reveal():
    global x1,y1
    for g in range (0,2):
        for i1 in range (0,52):
            if List6[g]==deck1[i1]:
                List7[i1]()
                x1=x1+50

def flop_reveal():
    global x1,y1
    x1=525
    y1=200
    for g in range (0,3):
        for i1 in range (0,52):
            if table[g]==deck1[i1]:
                List7[i1]()
                x1=x1+50


def turn_reveal():
    global x1,y1
    for i1 in range (0,52):
        if table[3]==deck1[i1]:
            List7[i1]()
            x1=x1+50


def river_reveal():
    global x1,y1
    for i1 in range (0,52):
        if table[4]==deck1[i1]:
            List7[i1]()
            x1=x1+50

player_reveal()
flop_reveal()
turn_reveal()
river_reveal()
mainloop()
