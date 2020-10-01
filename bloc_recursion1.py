import os
from math import sqrt, floor
import csv
#Global Values Start
d=["asia","middle east","africa","other","latin","south america"]
cost=[]
mgcost=[]
oilcost=[]
rmcost=[]
#Global Values End

#System Tab Start
def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def region():
    print()
    print("Regions :-")
    print("(1)Asia")
    print("(2)Middle East")
    print("(3)Africa")
    print("(4)Other")
    print("(5)Latin")
    print("(6)South America")
    global c
    c=input("What is your region :- ")
    print()
    c.lower()
#System Tab End
        
#Milliatry Tab Start
def planecost():
    a=int(input("Enter how many planes do you have:- "))
    b=int(input("Enter how many planes do you want to build :-"))
    pointcost=[]
    for i in range(b+1):
        mgcost.append((11+a)*(a/2))
        oilcost.append(5+a)
        pointcost.append((11+a)*(a/2))
        a=a+1
    print("You need :- ",sum(mgcost)," mg or ",sum(pointcost)," relations and ",sum(oilcost)," oils")

def navycost():
    a=int(input("Enter how many ships do you have :- "))
    b=int(input("Enter how many ships do you want to make :- "))
    for i in range (b+1):
        mgcost.append(a+10)
        oilcost.append(a+10)
        a=a+1
    print("You need ",sum(mgcost)," mg and ",sum(oilcost)," oils")

def traincost():
    a=int(input("Enter how many troops do you have :- "))
    b=int(input("Enter how much training do you have :- "))
    c=int(input("Enter how much training do you want to get :- "))
    t=c-b
    tt=t//5
    cost=[]
    for i in range(tt+1):
        cost.append((floor(((a*a/100*b*b/100)/2)))//2)
        b=b+5
    print("Cash needed :- ",sum(cost))

def warscore():
    a=int(input("Enter how many troops do you have:- "))
    aa=int(input("Enter how many troops does the rival have :- "))
    print()
    t=int(input("Enter your training :- "))
    tt=int(input("Enter rival's training :- "))
    print()
    b=int(input("Enter how many planes do you have :- "))
    bb=int(input("Enter how many planes does the rival have :- "))
    print()
    w=int(input("Enter how many weapons do you have :- "))
    ww=int(input("Enter how many weapons does the rival have :- "))
    c=int(input("Enter how many ships do you have :- "))
    cc=int(input("Enter how many ships does the rival have :- "))
    print()
    c=int(input("Enter how many ships do you have :- "))
    cc=int(input("Enter how many ships does the rival have :- "))
    you=sqrt(a)*sqrt(sqrt(w+1)*sqrt(t+1)*sqrt(b+1))
    rival=sqrt(aa)*sqrt(sqrt(ww+1)*sqrt(tt+1)*sqrt(bb+1))
    print()
    print("NOTE:- Ships dont affect war score")
    print()
    print("Your war score is :- ",round(you, 2))
    print("Your rival's war score is :- ",round(rival, 2))
    print()
    if you>rival:
        print("You have greater chance of winning because you have a higher war score")
        print("You have ",round(you-rival,2)," more war score than your rival")
    elif you<rival:
        print("You have greater chance of losing because you have a lower war score")
        print("You have ",round(rival-rival,2)," less war score than your rival")
    elif you==rival:
        print("You both have same war score")

def alliancewarscore():
    a=int(input("How many members do you have :- "))
    b=int(input("How many members does the enemy have :- "))
    with open('war_you.csv', 'w', newline='') as csvfile:
            fieldnames = ['nation', 'troops','air force','training','ships','weapons','war_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    for i in range(2,a+2):
        nation=input("Enter nation name :- ")
        troop=int(input("Enter how many troops do you have :- "))
        weapon=int(input("Enter how many weapons do you have :- "))
        train=int(input("Enter how much training do you have :- "))
        navy=int(input("Enter how many ships do you have :- "))
        plane=int(input("Enter how many planes do you have :- "))
        youscr=sqrt(troop)*sqrt(sqrt(weapon+1)*sqrt(train+1)*sqrt(plane+1))
        with open('war_you.csv',"a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nation': nation, 'troops': troop,'training':train,'air force':plane,'ships':navy,'weapons':weapon,'war_score':round(youscr,2)})
        screen_clear()
    print("Your alliance csv genrated")
    
    with open('war_enemy.csv', 'w', newline='') as csvfile:
            fieldnames = ['nation', 'troops','air force','training','ships','weapons','war_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    for o in range (2,b+2):
        nation=input("Enter nation name :- ")
        troop=int(input("Enter how many troops do you have :- "))
        weapon=int(input("Enter how many weapons do you have :- "))
        train=int(input("Enter how much training do you have :- "))
        navy=int(input("Enter how many ships do you have :- "))
        plane=int(input("Enter how many planes do you have :- "))
        enemyscr=sqrt(troop)*sqrt(sqrt(weapon+1)*sqrt(train+1)*sqrt(plane+1))
        with open('war_enemy.csv','a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nation': nation, 'troops': troop,'training':train,'air force':plane,'ships':navy,'weapons':weapon,'war_score':round(enemyscr,2)})
        screen_clear()
    print("enemy alliance csv genrated")
#Militray Tab End
        
#Economic Tab Start      
def indcost():
    a=int(input("How many factories do you have :- "))
    b=int(input("How many universities do you have :- "))
    wepon=int(input("How many weapon factories do you have :- "))
    t=int(input("How many factories/universities do you want to build :- "))
    x=a+b+wepon
    landcost=750*(t)
    region()
    while len(d):
        if c==d[0] or "1":
            for i in range(t):
                rmcost.append((50+(100*x))-((50+(100*x))*(25/100)))
                oilcost.append((25+(50*x))-((25+(50*x))*(25/100)))
                mgcost.append((2*x)-((2*x)*(25/100)))
                x=x+1
            print("Raw materials :- ",sum(rmcost))
            print("Oil :- ",sum(oilcost))
            print("Manufacutred Goods :- ",sum(mgcost))
            print("Land needed :- ",landcost,"kms")
            break
        else :
            for o in range(t):
                rmcost.append(50+(100*x))
                oilcost.append(25+(50*x))
                mgcost.append(2*x)
                x=x+1
            print("Raw materials :- ",sum(rmcost))
            print("Oil :- ",sum(oilcost))
            print("Manufacutred Goods :- ",sum(mgcost))
            print("Land needed :- ",landcost,"kms")
            break


def wellcost():
    a=int(input("How many wells do you have :- "))
    b=int(input("How many wells do you want to build :- "))
    landcost=350*b
    region()
    while len(d):
        if c==d[1] or "2":
            for i in range(b):
                cost.append((500+(a*50))-((500+(a*50))*(33/100)))
                a=a+1
            print("Cash needed :- ",sum(cost),"k")
            print("Land needed :- ",landcost,"kms")
            break
        else:
            for o in range(b):
                cost.append(500+(a*50))
                a=a+1
            print("Cash needed :- ",sum(cost),"k")
            print("Land needed :- ",landcost,"kms")
            break


def minecost():
    a=int(input("How many mines do you have :- "))
    b=int(input("How many mines do you want to build :- "))
    landcost=350*b
    region()
    while len(d):
        if c==d[2] or d[4] or d[5] or "3" or "5" or "6":
            for i in range(b):
                cost.append(250+(a*33))
                a=a+1
            print("Cash needed :- ",sum(cost),"k")
            print("Land needed :- ",landcost,"kms")
            break
        else:
            for o in range(b):
                cost.append(250+(a*50))
                a=a+1
            print("Cash needed:- ",sum(cost),"k")
            print("Land needed :- ",landcost,"kms")
            break
#Economic Tab End

def menu():
    x="yes"
    while x=="yes":
        screen_clear()
        print("""Menu :-
        Enter 1 to run factory/uni cost calculator
        Enter 2 to run oil wells cost calculator
        Enter 3 to run mines cost calculator
        Enter 4 to run plane cost calculator
        Enter 5 to run ship cost calculator
        Enter 6 to run training cost calulator
        Enter 7 to run war scrore calculator
        Enter 8 to run alliance war scrore calulator""")
        a=int(input("Enter your selection :- "))
        print()
        if a==1:
            indcost()
        elif a==2:
            wellcost()
        elif a==3:
            minecost()
        elif a==4:
            planecost()
        elif a==5:
            navycost()
        elif a==6:
            traincost()
        elif a==7:
            warscore()
        elif a==8:
            alliancewarscore()
        else :
            print("Enter vaild option!!!!!")
        x=input("do you want to run the program again yes/no:- ")


if __name__ == "__main__":
    menu()
    
    
    
    
    
    

            
            
            
            
        
    
