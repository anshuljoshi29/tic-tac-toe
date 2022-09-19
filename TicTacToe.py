import random

#creation of matrix for Tic tac toe table

table=["_","_","_",
        "_","_","_",
        "_","_","_"]


currentchar="X"
running=True
won=None

var=int(input("'1' for 1 vs 1\n'2' for computer\n="))


#table design
def gameBoard():
    print(table[0],"|",table[1],"|",table[2])
    print("--+---+--")
    print(table[3],"|",table[4],"|",table[5])
    print("--+---+--")
    print(table[6],"|",table[7],"|",table[8])

#enter the game 
def enter():
    ins=int(input("enter the location from 1 to 9="))
    if ins>=1 and ins<=9 and table[ins-1]=="_":
        table[ins-1]=currentchar
    else:
        print("enter valid number or empty area",gameBoard())
        enter()
     
#check if horizontal row is covered
def checkH():
    global won,table
    if table[0]==table[1]==table[2] and table[0]!="_":
        won=table[0]
        return True
    elif table[3]==table[4]==table[5] and table[3]!="_":
        won=table[3]
        return True
    elif table[6]==table[7]==table[8] and table[6]!="_":
        won=table[6]
        return True

#check if Diagonal row is covered
def checkD():
    global won,table
    if table[0]==table[4]==table[8] and table[0]!="_":
        won=table[0]
        return True
    elif table[2]==table[4]==table[6] and table[2]!="_":
        won=table[2]
        return True

#check if vertical row is covered
def checkV():
    global won,table
    if table[0]==table[3]==table[6] and table[0]!="_":
        won=table[0]
        return True

    elif table[1]==table[4]==table[7] and table[1]!="_":
        won=table[1]
        return True

    elif table[2]==table[5]==table[8] and table[2]!="_":
        won=table[2]
        return True

#switching between players
def switch():
    global currentchar
    if currentchar=="X":
        currentchar="O"
    else:
        currentchar="X"

#check if game leads to tie
def tie():
    global running
    if "_" not in table and check()!=True:
        print("it is tie")
        gameBoard()
        running=False

#check weather we got our winner
def check():
    global running
    if checkV() or checkD() or checkH():
        print("The winner is Hurraaayyyyy!",won)
        gameBoard()
        running=False
        return True


#simple computer AI
def computer():
    global running,currentchar
    if currentchar=="O":
        step=random.randint(1,9)
        if table[step-1]=="_":
            table[step-1]=currentchar
            currentchar="X"
        elif "_" not in table:
            running=False
        else:
            computer()
        


#game runner
while running:
    gameBoard()
    enter()
    check()
    tie()

    if var==2:
        currentchar="O"
        computer()
    else:
        switch()