def printBoard(xState, zState):
    print(f"{get_symbol(xState, zState, 0)} | {get_symbol(xState, zState, 1)} | {get_symbol(xState, zState, 2)}")
    print("--|---|---")
    print(f"{get_symbol(xState, zState, 3)} | {get_symbol(xState, zState, 4)} | {get_symbol(xState, zState, 5)}")
    print("--|---|---")
    print(f"{get_symbol(xState, zState, 6)} | {get_symbol(xState, zState, 7)} | {get_symbol(xState, zState, 8)}")

def get_symbol(xState, zState, index):
    if xState[index] == 1:
        return 'X'
    elif zState[index] == 1:
        return 'O'
    return index

def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if xState[win[0]] and xState[win[1]] and xState[win[2]]:
            return 'X'
        elif zState[win[0]] and zState[win[1]] and zState[win[2]]:
            return 'O'
    return None

def check_draw(xState, zState):
    return all(xState[i] or zState[i] for i in range(9)) and not checkwin(xState, zState)

def is_valid_move(move):
    return move.isdigit() and 0 <= int(move) < 9

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe!")
    
    while True:
        printBoard(xState, zState)
        player = 'X' if turn == 1 else 'O'
        print(f"{player}'s chance")
        
        while True:
            value = input("Please enter a value (0-8): ")
            if not is_valid_move(value):
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
            index = int(value)
            if xState[index] or zState[index]:
                print("Invalid move. Cell already marked. Choose another position.")
                continue
            break
            
        if player == 'X':
            xState[index] = 1
        else:
            zState[index] = 1
        
        winner = checkwin(xState, zState)
        if winner:
            printBoard(xState, zState)
            print(f"{winner} won the match!")
            break
            
        if check_draw(xState, zState):
            printBoard(xState, zState)
            print("The match is a draw!")
            break
            
        turn = 1 - turn
