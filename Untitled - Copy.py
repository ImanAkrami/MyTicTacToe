
# coding: utf-8

# In[64]:


############# NEEDED VARIABLES and preperations
#defining player names, will be changed after input
global fplayer
fplayer = ''
global splayer
splayer = ''
finished = 0
# defining a global variable called "winner" to show who is winner
global winner
winner = 0
# DRAW counter: it takes 9 turn and no win to draw, so if there is 9 moves and no winner it is a draw
global drawcounter
drawcounter = 1

############### creating the matrix need for game, with 0 value and MAPPING it
x = 3
y = 3
matrix = [[0 for n in range(x)] for m in range(y)]
#MAPPING 
x1 = matrix[0][0]
global x2
x2 = matrix[0][1]
x3 = matrix[0][2]
x4 = matrix[1][0]
x5 = matrix[1][1]
x6 = matrix[1][2]
x7 = matrix[2][0]
x8 = matrix[2][1]
x9 = matrix[2][2]
############## VISUALS OF MATRIX
def vmatrix ():
    print '*********'
    print  x1,'|',x2,'|',x3
    print  x4,'|',x5,'|',x6
    print  x7,'|',x8,'|',x9
    print '*********'
##############charachter checker and output, and being used checker
# 1st check if charachter is valid and second one returns the input value
def validchar (char):
    if char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
        return True
    else:
        return False
def userinputting():
        x = None
        global input
        input = ''
        while x != True:
            input = raw_input('Please Enter a a charachter between 1 to 9\n')
            x = validchar(input)
        else:
            print 'You entered', input,'\n'
            return input
# this one checks if input is full or not
def isfull (xn):
    if xn == 0:
        return False
    else:
        return True
############# WINNER FUNCTION
def winend():
# this function checks if anyone has won and if so, return the 
# checking if the first player won
    global drawcounter,x1,x2,x3,x4,x5,x6,x7,x8,x9,xx
    global winner
    if x1 == 1 and x2 == 1 and x3 == 1:
        winner = 1
    elif x4 == 1 and x5 == 1 and x6 == 1:
        winner = 1
    elif x7 == 1 and x8 == 1 and x9 == 1:
        winner = 1
    elif x1 == 1 and x4 == 1 and x7 == 1:
        winner = 1
    elif x2 == 1 and x5 == 1 and x8 == 1:
        winner = 1
    elif x3 == 1 and x6 == 1 and x9 == 1:
        winner = 1
    elif x1 == 1 and x5 == 1 and x9 == 1:
        winner = 1
    elif x3 == 1 and x5 == 1 and x7 == 1:
        winner = 1
# checking if the second player won
    elif x1 == 2 and x2 == 2 and x3 == 2:
        winner = 2
    elif x4 == 2 and x5 == 2 and x6 == 2:
        winner = 2
    elif x7 == 2 and x8 == 2 and x9 == 2:
        winner = 2
    elif x1 == 2 and x4 == 2 and x7 == 2:
        winner = 2
    elif x2 == 2 and x5 == 2 and x8 == 2:
        winner = 2
    elif x3 == 2 and x6 == 2 and x9 == 2:
        winner = 2
    elif x1 == 2 and x5 == 2 and x9 == 2:
        winner = 2
    elif x3 == 2 and x5 == 2 and x7 == 2:
        winner = 2
    else:
        print 'The game continues...'
        pass
######### This is the function for game start and getting player names.
def gamestart():
    ##### Name variables
    global fplayer
    fplayer = ''
    global splayer
    splayer = ''

    print 'Hello , This is a tic tac toe game. this is how game squares are numbered:'
    print '**********'
    print '1 | 2 | 3'
    print '4 | 5 | 6'
    print '7 | 8 | 9'
    print '**********\n'

    while len(fplayer) == 0:
        fplayer = raw_input('First player, please enter your name:\n')
    else:
        print 'first player is ',fplayer
    while len(splayer) == 0:
        splayer = raw_input('second player, please enter your name:\n')
    else:
        print 'second player is ',splayer
############ Value SETTER funcution
def setter():
    global drawcounter,x1,x2,x3,x4,x5,x6,x7,x8,x9,xx
    print fplayer+"'"+"s"," turn"
    userinputting()
    if drawcounter == 1 or drawcounter == 3 or drawcounter == 5 or drawcounter == 7:
        xx = 1
    elif drawcounter == 2 or drawcounter == 4 or drawcounter == 6 or drawcounter == 8:
        xx = 2
    else:
        print 'Game ended'
        drawcounter = 9
####
    if input == '1':
        if isfull(x1) == False:
            x1 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '2':
        if isfull(x2) == False:
            x2 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '3':
        if isfull(x3) == False:
            x3 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '4':
        if isfull(x4) == False:
            x4 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '5':
        if isfull(x5) == False:
            x5 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '6':
        if isfull(x6) == False:
            x6 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '7':
        if isfull(x7) == False:
            x7 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '8':
        if isfull(x8) == False:
            x8 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    elif input == '9':
        if isfull(x9) == False:
            x9 = xx
            drawcounter += 1
        else:
            print 'that cell is already full!'
    else:
        print 'error'
    winend()
##########################################################
##########################################################
##################   STARTS HERE #########################
global winner,drawcounter
gamestart()
while not (winner == 1 or winner == 2) and drawcounter < 10:
    setter()
    vmatrix()
    winend()
else:
    if winner == 1:
        print fplayer,' has won!'
        vmatrix()
    elif winner == 2:
        print splayer,' has won!'
        vmatrix()
    else:
        print 'the game is a draw!'
        vmatrix()


# ###### x1 = 1
# x2 = 1
# x3 = 1
# winend()
# winner

# In[49]:


x1 == 1 and x4 == 1 and x7 == 1


# In[ ]:




