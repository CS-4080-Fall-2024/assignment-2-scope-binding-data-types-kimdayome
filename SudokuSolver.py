def is_valid(board, row, col, num):
    
    # check the conditions
    # 1. 'num' must not already be present in same row.
    # 2. 'num' must not already be present in same column.
    # 3. 'num' must not already be present in same 3x3 grid ***
    
    # check if 'num' is already in the same row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check if 'num' is already in the same column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Deciding the starting row and column of the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    
    # Check if 'num' is already in the 3x3 sub-grid
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True


def solve_sudoku(board):
    
    # Now in this function, by using the backtracking, it fills the empty cells of
    # the board which is marked as '.' with the numbers from 1 to 9
    for row in range(9): # outer loop starts with row = 0 first, looping through all rows
        # once all columns in a row are filled, the function moves to the next row
        for col in range(9): # jumping into inner loop ( 0 to 8 )
            if board[row][col] == ".": # checking every cell (if the cell is empty)
            # checking all the columns in the first row, and then outer loop move to the next row
            
                # if the cell isn't empty, skip this part
                # try placing numbers from 1 to 9
                for num in map(str, range(1, 10)):
                    # check if 'num' can be placed here
                    if is_valid(board, row, col, num):
                        # temp place 'num' in the current cell
                        board[row][col] = num
                        # after placing, now calling itself(recursive) function to solve the rest
                        if solve_sudoku(board):
                            # return true if the board is solved
                            return True
                        # backtrack, reset the cell if it didnt' work
                        board[row][col] = "."
                # return false
                return False
    return True


def print_board(board):
    # print each row of the Sudoku board, numbers separated by space
    for row in board:
        print(" ".join(row))


def main():
    # main function to initialize Sudoku board and call the solver
    # initial board that has empty cells represented by '.'
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    # print out
    if solve_sudoku(sudoku_board):
        print("Yay!! it's solved :) :")
        print_board(sudoku_board)
    else:
        print("No solution exists for given one :(")


# main
if __name__ == "__main__":
    main()
    
# solution approach reference used : https://www.geeksforgeeks.org/sudoku-problem-in-python/
# solution approach reference used 2 : https://www.aiappleseed.com/chatgpt-sudoku-solver.html
# solution approach reference used 3 : https://www.chegg.com/homework-help/questions-and-answers/python-code-solves-sudoku-puzzle-using-forward-checking-m-trying-understand-get-detailed-e-q121300764