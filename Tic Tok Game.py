board = [1,2,3,4,5,6,7,8,9]



player = 1
total_moves = 0
end_check=0


def draw():
    print(" --------------")
    print("|" , board[0], "|",board[1],"|",board[2],"|")
    print("|" , board[3], "|",board[4],"|",board[5],"|")
    print("|" , board[6], "|",board[7],"|",board[8],"|")
    print(" --------------")

def check():

    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[3] == 'X' and board[4] == 'X' and board[5] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[6] == 'X' and board[7] == 'X' and board[8] == 'X' :
        print("Player 1 Win !!")
        return 1
    
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X' :
        print("Player 1 Win !!")
        return 1

    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X' :
        print("Player 1 Win !!")
        return 1

    #-----player 2----

    if board[0] == 'O' and board[1] ==  'O' and board[2] ==  'O' :
        print("Player 2 Win !!")
        return 1

    if board[3] ==  'O'  and board[4] ==  'O' and board[5] ==  'O'  :
        print("Player 2 Win !!")
        return 1

    if board[6] ==  'O' and board[7] ==  'O' and board[8] ==  'O'  :
        print("Player 2 Win !!")
        return 1
    
    if board[0] ==  'O' and board[3] == 'O' and board[6] == 'O' :
        print("Player 2 Win !!")
        return 1

    if board[1] == 'O' and board[4] == 'O' and board[7] == 'O' :
        print("Player 2 Win !!")
        return 1

    if board[2] == 'O' and board[5] == 'O' and board[8] == 'O' :
        print("Player 2 Win !!")
        return 1

    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O' :
        print("Player 2 Win !!")
        return 1

    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O' :
        print("Player 2 Win !!")
        return 1
    return 0

while True:
    draw()
    end_check = check()
    if total_moves ==9 or end_check ==1:
        break

    while True:
        if player == 1:
            n1 = int(input("Player 1= " ))
            if n1 in board:
                board[n1-1] = 'X'
                player = 2
                break

            else:
                print("Invalid input try again")
                continue

        else:
            n2 = int(input("Player 2 ="))
            if n2 in board:
                board[n2-1] = 'O'
                player = 1
                break

            else:
                print("Invalid input")
                continue

    total_moves += 1
    print()
            
                
    
    
