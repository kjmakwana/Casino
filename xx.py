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

for i in range(2,15):
    List.append(i)                                                                

for j in range(0,13):
    if j<8:
        List1.append(str(0)+str(List[j])+'h')
    else:
        List1.append(str(List[j])+'h')

for k in range (0,13):
    if k<8:
        List2.append(str(0)+str(List[k])+'d')
    else:
        List2.append(str(List[k])+'d')    

for q in range (0,13):
    if q<8:
        List3.append(str(0)+str(List[q])+'s')
    else:
        List3.append(str(List[q])+'s') 

for m in range (0,13):
    if m<8:
        List4.append(str(0)+str(List[m])+'c')
    else:
        List4.append(str(List[m])+'c')     
deck=List1+List2+List3+List4


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
        table.append(l)
        table.append(o)
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
    table.append(l)
    table.append(o)
    table.append(y)
    table.append(x)
    table.append(z)
    table.append(w)
    table.append(v)
table_cards()


def my_func1():
    my_img1=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AC.jpg"))
    my_label1=Label(image=my_img1)   
    my_label1.pack()
    
def my_func2():
    my_img2=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2C.jpg"))
    my_label2=Label(image=my_img2)   
    my_label2.pack()

def my_func3():
    my_img3=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3C.jpg"))
    my_label3=Label(image=my_img3)   
    my_label3.pack()

def my_func4():
    my_img4=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4C.jpg"))
    my_label4=Label(image=my_img4)   
    my_label4.pack()

def my_func5():
    my_img5=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5C.jpg"))
    my_label5=Label(image=my_img5)   
    my_label5.pack()

def my_func6():
    my_img6=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6C.jpg"))
    my_label6=Label(image=my_img6)   
    my_label6.pack()

def my_func7():
    my_img7=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7C.jpg"))
    my_label7=Label(image=my_img7)   
    my_label7.pack()

def my_func8():
    my_img8=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8C.jpg"))
    my_label8=Label(image=my_img8)   
    my_label8.pack()

def my_func9():
    my_img9=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9C.jpg"))
    my_label9=Label(image=my_img9)   
    my_label9.pack()

def my_func10():
    my_img10=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10C.jpg"))
    my_label10=Label(image=my_img10)   
    my_label10.pack()

def my_func11():
    my_img11=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JC.jpg"))
    my_label11=Label(image=my_img11)   
    my_label11.pack()

def my_func12():
    my_img12=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QC.jpg"))
    my_label12=Label(image=my_img12)   
    my_label12.pack()

def my_func13():
    my_img13=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KC.jpg"))
    my_label13=Label(image=my_img13)   
    my_label13.pack()

def my_func14():
    my_img14=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AS.jpg"))
    my_label14=Label(image=my_img14)   
    my_label14.pack()

def my_func15():
    my_img15=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2S.jpg"))
    my_label15=Label(image=my_img15)   
    my_label15.pack()

def my_func16():
    my_img161=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3S.jpg"))
    my_label161=Label(image=my_img161)   
    my_label161.pack()

def my_func17():
    my_img162=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4S.jpg"))
    my_label162=Label(image=my_img162)   
    my_label162.pack()

def my_func18():
    my_img17=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5S.jpg"))
    my_label17=Label(image=my_img17)   
    my_label17.pack()

def my_func19():
    my_img18=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6S.jpg"))
    my_label18=Label(image=my_img18)   
    my_label18.pack()

def my_func20():
    my_img19=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7s.jpg"))
    my_label19=Label(image=my_img19)   
    my_label19.pack()

def my_func21():
    my_img20=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8S.jpg"))
    my_label20=Label(image=my_img20)   
    my_label20.pack()

def my_func22():
    my_img21=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9S.jpg"))
    my_label21=Label(image=my_img21)   
    my_label21.pack()

def my_func23():
    my_img22=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10S.jpg"))
    my_label22=Label(image=my_img22)   
    my_label22.pack()

def my_func24():
    my_img23=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JS.jpg"))
    my_label23=Label(image=my_img23)   
    my_label23.pack()

def my_func25():
    my_img24=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QS.jpg"))
    my_label24=Label(image=my_img24)   
    my_label24.pack()

def my_func26():
    my_img25=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KS.jpg"))
    my_label25=Label(image=my_img25)   
    my_label25.pack()

def my_func27():
    my_img26=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AH.jpg"))
    my_label26=Label(image=my_img26)   
    my_label26.pack()

def my_func28():
    my_img27=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2H.jpg"))
    my_label27=Label(image=my_img27)   
    my_label27.pack()

def my_func29():
    my_img28=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3H.jpg"))
    my_label28=Label(image=my_img28)   
    my_label28.pack()

def my_func30():
    my_img29=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4H.jpg"))
    my_label29=Label(image=my_img29)   
    my_label29.pack()

def my_func31():
    my_img30=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5H.jpg"))
    my_label30=Label(image=my_img30)   
    my_label30.pack()

def my_func32():
    my_img31=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6H.jpg"))
    my_label31=Label(image=my_img31)   
    my_label31.pack()

def my_func33():
    my_img32=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7H.jpg"))
    my_label32=Label(image=my_img32)   
    my_label32.pack()

def my_func34():
    my_img33=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8H.jpg"))
    my_label33=Label(image=my_img33)   
    my_label33.pack()

def my_func35():
    my_img34=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9H.jpg"))
    my_label34=Label(image=my_img34)   
    my_label34.pack()

def my_func36():
    my_img35=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10H.jpg"))
    my_label35=Label(image=my_img35)   
    my_label35.pack()

def my_func37():
    my_img36=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JH.jpg"))
    my_label36=Label(image=my_img36)   
    my_label36.pack()

def my_func38():
    my_img37=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QH.jpg"))
    my_label37=Label(image=my_img37)   
    my_label37.pack()

def my_func39():
    my_img38=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KH.jpg"))
    my_label38=Label(image=my_img38)   
    my_label38.pack()

def my_func40():
    my_img39=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\AD.jpg"))
    my_label39=Label(image=my_img39)   
    my_label39.pack()

def my_func41():
    my_img40=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\2D.jpg"))
    my_label40=Label(image=my_img40)   
    my_label40.pack()

def my_func42():
    my_img41=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\3D.jpg"))
    my_label41=Label(image=my_img41)   
    my_label41.pack()

def my_func43():
    my_img42=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\4D.jpg"))
    my_label42=Label(image=my_img42)   
    my_label42.pack()

def my_func44():
    my_img43=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\5D.jpg"))
    my_label43=Label(image=my_img43)   
    my_label43.pack()

def my_func45():
    my_img44=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\6D.jpg"))
    my_label44=Label(image=my_img44)   
    my_label44.pack()

def my_func46():
    my_img45=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\7D.jpg"))
    my_label45=Label(image=my_img45)   
    my_label45.pack()

def my_func47():
    my_img46=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\8D.jpg"))
    my_label46=Label(image=my_img46)   
    my_label46.pack()

def my_func48():
    my_img47=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\9D.jpg"))
    my_label47=Label(image=my_img47)   
    my_label47.pack()

def my_func49():
    my_img48=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\10D.jpg"))
    my_label48=Label(image=my_img48)   
    my_label48.pack()

def my_func50():
    my_img49=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\JD.jpg"))
    my_label49=Label(image=my_img49)   
    my_label49.pack()

def my_func51():
    my_img50=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\QD.jpg"))
    my_label50=Label(image=my_img50)   
    my_label50.pack()

def my_func52():
    my_img51=ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\python\PNG\KD.jpg"))
    my_label51=Label(image=my_img51)   
    my_label51.pack()


List7=[]
#for i2 in range (1,52):
List7.append(my_func1)
List7.append(my_func2)


for g in range (n):
    for i1 in range (1):
        if List6[g]==deck[i1]:
            List7[i1]()



mainloop()
