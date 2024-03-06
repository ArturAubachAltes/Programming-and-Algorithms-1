def check_winner(matrix, X):

    rows = len(matrix)
    cols = rows

    # Check rows
    for row in range(rows):
        for col in range(cols - X + 1):
            if matrix[row][col] != 0:
                player = matrix[row][col]
                win = True
                for i in range(1, X):
                    if matrix[row][col + i] != player:
                        win = False
                        break
                if win:
                    return player

    # Check columns
    for col in range(cols):
        for row in range(rows - X + 1):
            if matrix[row][col] != 0:
                player = matrix[row][col]
                win = True
                for i in range(1, X):
                    if matrix[row + i][col] != player:
                        win = False
                        break
                if win:
                    return player

    # Check diagonals
    for row in range(rows - X + 1):
        for col in range(cols - X + 1):
            if matrix[row][col] != 0:
                player = matrix[row][col]
                win = True
                for i in range(1, X):
                    if matrix[row + i][col + i] != player:
                        win = False
                        break
                if win:
                    return player

    for row in range(X - 1, rows):
        for col in range(cols - X + 1):
            if matrix[row][col] != 0:
                player = matrix[row][col]
                win = True
                for i in range(1, X):
                    if matrix[row - i][col + i] != player:
                        win = False
                        break
                if win:
                    return player
    # If no player wins
    return False
