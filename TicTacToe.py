li = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
def print_board():
    for item in li:
        print item

flag = 0
def add_x(arg1):
    a = 0
    b = 0
    
    global flag
    flag = 0
    if arg1 != 'X' and arg1 != 'x' and arg1 != '0':
        for l1 in li:
            for l2 in l1:
                if l2 == arg1:
                    li[a][b] = 'X'
                    flag += 1
                    break
                else:
                    b+=1
                    continue
            b = 0
            a+=1
    else: 
        print 'Please enter a valid position.'
        p3 = raw_input()
        add_x(p3)
    if flag == 0:
        print 'Position not found. Please enter a valid position.'
        p4 = raw_input()
        add_x(p4)
    else:
        pass

def add_o(arg2):
    a = 0
    b = 0
    global flag
    flag = 0
    if arg2 != 'X' and arg2 != 'x' and arg2 != '0':
        for l1 in li:
            for l2 in l1:
                if l2 == arg2:
                    li[a][b] = '0'
                    flag += 1
                    break
                else:
                    b+=1
                    continue
            b = 0
            a+=1
    else: 
        print 'Please enter a valid position.'
        p5 = raw_input()
        add_o(p5)
    if flag == 0:
        print 'Position not found. Please enter a valid position.'
        p6 = raw_input()
        add_o(p6)
    else:
        pass

        
count = 0
def inc_count():
    global count
    count += 1


xl = ['X', 'X', 'X']
ol = ['0', '0', '0']
draw = 0


def check_winner():
    global draw
    xl = ['X', 'X', 'X']
    ol = ['0', '0', '0']
    for item in li:
        if item == xl:
            print 'Player 1 wins'
            draw += 1
        elif item == ol:
            print 'Player 2 wins'
            draw += 1
        else:
            continue


    nl1 = [li[0][0], li[1][0], li[2][0]]
    nl2 = [li[0][1], li[1][1], li[2][1]]
    nl3 = [li[0][2], li[1][2], li[2][2]]

    if nl1 == xl or nl2 == xl or nl3 == xl:
        print 'Player 1 wins.'
        draw += 1
    elif nl1 == ol or nl2 == ol or nl3 == ol:
        print 'Player 2 wins.'
        draw += 1

    nl1 = [li[0][0], li[1][1], li[2][2]]
    nl2 = [li[0][2], li[1][1], li[2][0]]

    if nl1 == xl or nl2 == xl:
        print 'Player 1 wins.'
        draw += 1
    elif nl1 == ol or nl2 == 0l:
        print 'Player 2 wins.'
        draw += 1


def check_draw():
    global draw
    if draw == 0:
        print "The game is draw between Player-1 and Player-2"



print 'Welcome to TicTacToe!'
play = 'y'
while play == 'y' or play == 'Y' or play == 'yes' or play == 'Yes' or  play == 'YES':
    
    print 'The Board is:'
    print_board()
    count = 0

    while count < 9:

        print 'Player-1: Select the position you want to insert a X'
        p1 = raw_input()
        add_x(p1)
        inc_count()
        print_board()
        check_winner()
        if draw > 0:
            break

        elif count == 9:
            break


        print 'Player-2: Select the position you want to insert a 0'
        p2 = raw_input()
        add_o(p2)
        inc_count()
        print_board()
        check_winner()
        if draw > 0:
            break

        elif count == 9:
            break


    check_draw()


    print "Do you want to play again? Enter 'y' for yes and 'n' for no. "
    play = raw_input()




