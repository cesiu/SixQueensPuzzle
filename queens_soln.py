# Finds a truce of six queens on a 6x6 board.
# author: Christopher Siu

mboard = [[0,0,0,0,0,0],\
          [0,0,0,0,0,0],\
          [0,0,0,0,0,0],\
          [0,0,0,0,0,0],\
          [0,0,0,0,0,0],\
          [0,0,0,0,0,0]]

def valid(board):
    # Check rows
    for i in range(6):
        if board[i].count(1) > 1:
            return False

    # Check columns:
    for j in range(6):
        count = 0
        for i in range(6):
            count += board[i][j]
        if count > 1:
            return False

    # Check diagonals:
    for diff in range(-5, 6):
        count = 0
        for j in range(6):
            i = j + diff
            if 0 <= i < 6:
                count += board[i][j]
        if count > 1:
            return False
    for diff in range(11):
        count = 0
        for i in range(6):
            j = diff - i
            if 0 <= j < 6 and 0 <= i <= 6:
                count += board[i][j]
        if count > 1:
            return False
    return True

def print_board(board):
    for row in board:
        print row
    print ""

# Start at the first spot.
i = 0
j = 0
num_queens = 0

# While the coordinates are valid:
while i < 6 and j < 6:
    # If there're six queens on the board, we've found a solution.
    if num_queens == 6:
        print "Solution:"
        print_board(mboard)
        break

    # Put a queen at the current spot.
    mboard[i][j] = 1
    print "Trying..."
    print_board(mboard)

    # If the board is invalid:
    if not valid(mboard) or i == 5 and j == 5 and num_queens < 6:
        # Remove the queen.
        mboard[i][j] = 0
        # If we've gotten to the last square:
        if i == 5 and j == 5:
            print "Backtracking..."
            # Backtrack to the last queen:
            while mboard[i][j] != 1:
                j -= 1
                if j < 0:
                    j = 5
                    i -= 1
            # If we've backtracked to off of the board, there's no solution.
            if i == -1:
                print "No solution."
                break
            # Remove that queen.
            mboard[i][j] = 0
            num_queens -= 1
            print_board(mboard)
    else:
        num_queens += 1
    # Move to the next square.
    j += 1
    if j > 5:
        j = 0
        i += 1

