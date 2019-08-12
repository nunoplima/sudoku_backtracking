import pandas as pd

def range_helper(n, idx):
    max = -float("inf")
    b = int(n ** 0.5)
    for i in range(b, -1, -1):
        if (idx + i) % b == 0:
            max = idx + i
            min = max - b
            break
    return min, max


def sudoku(coord, n):
    grid = [[None for i in range(n)] for j in range(n)]

    for each in coord: 
        row, col, num = each[0], each[1], each[2]
        grid[row][col] = num

    empty_spots = []
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if grid[row_idx][col_idx] is None:
                empty_spots.append((row_idx, col_idx))

    required_solved_slots = len(empty_spots)
    solved_slots = 0
    empty_spots_idx, candidate_num = 0, 1
    iterations = 0
    while solved_slots < required_solved_slots:
        iterations += 1
        print(solved_slots, required_solved_slots)
        [coord_row_i, coord_col_i] = empty_spots[empty_spots_idx] 
        
        print(f"\ncurrent cell: {coord_row_i}, {coord_col_i}\ncandidate number: {candidate_num}\nempty_spots_idx: {empty_spots_idx}\n{grid}\n\n")
 
        if candidate_num > n:
            print(f"candidate_num greater than: {n}\n------------------------------\n")
            empty_spots_idx = empty_spots_idx - 1 if empty_spots_idx > 0 else 0
            solved_slots = solved_slots - 1 if solved_slots > 0 else 0
            # we are going to backtrack, so current cell must be set to None
            grid[coord_row_i][coord_col_i] = None
            prev_row_idx = empty_spots[empty_spots_idx][0]
            prev_col_idx = empty_spots[empty_spots_idx][1]
            candidate_num = grid[prev_row_idx][prev_col_idx] + 1
            # candidate_num = 1
            continue

        current_row, current_col = grid[coord_row_i], [grid[r][coord_col_i] for r in range(n)]
        print(f"current row: {current_row}")
        print(f"current column: {current_col}\n")

        r_min_range, r_max_range = range_helper(n, coord_row_i)
        c_min_range, c_max_range = range_helper(n, coord_col_i)
        # plot the inner grid with the range values from the helper fn
        inner_grid = [row[c_min_range: c_max_range] for row in grid[r_min_range: r_max_range]]
        # join inner lists in inner_grid
        plain_inner_grid = [inner for outer in inner_grid for inner in outer]
        
        if candidate_num not in plain_inner_grid and candidate_num not in current_row and candidate_num not in current_col:
            print(f"candidate_num: {candidate_num} fits in coord ({coord_row_i}, {coord_col_i})\n\n")
            grid[coord_row_i][coord_col_i] = candidate_num
            solved_slots += 1
            empty_spots_idx += 1
            candidate_num = 1      

        else:
            print(f"candidate_num: {candidate_num} doesn't fit in coord ({coord_row_i}, {coord_col_i})\n\n")
            candidate_num += 1
    
    sudoku = pd.DataFrame(grid)
    
    return sudoku, iterations

            
# print(sudoku([[1, 2, 1], [2, 0, 4], [3, 1, 2], [3, 3, 3]], 4))

# -> 26710 
print(sudoku([
    [0, 0, 8], [0, 5, 2], [0, 6, 6],  
    [1, 1, 6], [1, 3, 3], [1, 4, 8], [1, 6, 1],
    [2, 7, 2], [2, 8, 3], 
    [3, 4, 7], [3, 5, 3], [3, 8, 2],
    [4, 3, 4], [4, 5, 5], [4, 7, 7],
    [5, 0, 1], [5, 2, 4], [5, 4, 9], [5, 7, 6],
    [6, 0, 4], [6, 1, 1], [6, 3, 8],
    [7, 2, 6], [7, 7, 9], 
    [8, 2, 7], [8, 3, 5], [8, 8, 8]
    ], 9))


# 10  -> 141667
# print(sudoku([
#     [0, 3, 4],  
#     [1, 4, 2], [1, 5, 1], [1, 6, 8],
#     [2, 2, 7], [2, 3, 5],
#     [3, 0, 2], [3, 1, 6], [3, 4, 9],
#     [4, 0, 1], [4, 5, 8], [4, 6, 2],
#     [5, 1, 5], [5, 4, 7], [5, 8, 3],
#     [6, 7, 1], [6, 8, 2],
#     [7, 0, 8], [7, 3, 6], [7, 6, 5], [7, 8, 4],
#     [8, 5, 5], [8, 6, 9], [8, 8, 8] 
#     ], 9))

# 128 -> 67749
# print(sudoku([
#     [0, 4, 9],  
#     [1, 4, 2], [1, 5, 8], [1, 6, 6], [1, 8, 1],
#     [2, 1, 7], [2, 6, 8], [2, 7, 9],
#     [3, 4, 6], [3, 5, 9], [3, 8, 3],
#     [4, 0, 4], [4, 2, 2], [4, 6, 9], [4, 8, 8],
#     [5, 0, 3], [5, 3, 4], [5, 4, 1],
#     [6, 1, 1], [6, 2, 4], [6, 7, 6],
#     [7, 0, 6], [7, 2, 3], [7, 3, 5], [7, 4, 4],
#     [8, 4, 8]
#     ], 9))



# 32 -> ~600000
# print(sudoku([
#     [0, 4, 5], [0, 7, 8], 
#     [1, 3, 6], [1, 5, 7],
#     [2, 0, 5], [2, 1, 3], [2, 6, 4],
#     [3, 2, 6], [3, 7, 7],
#     [4, 5, 3], [4, 8, 2],
#     [5, 3, 4], [5, 5, 8],
#     [6, 0, 9], [6, 2, 8], [6, 3, 2],
#     [7, 4, 4], [7, 8, 1],
#     [8, 0, 3], [8, 2, 2], [8, 5, 1], [8, 8, 7]
#     ], 9))

# 120 -> 65522
# print(sudoku([
#     [0, 0, 8], [0, 1, 2], [0, 4, 6], [0, 8, 1], 
#     [1, 2, 6], [1, 6, 9],
#     [2, 2, 9], [2, 5, 3], [2, 6, 8], [2, 7, 5],
#     [3, 1, 9], [3, 2, 2], [3, 3, 7], [3, 5, 8],
    
#     [5, 3, 6], [5, 5, 5], [5, 6, 1], [5, 7, 2],
#     [6, 1, 5], [6, 2, 8], [6, 3, 1], [6, 6, 2],
#     [7, 2, 3], [7, 6, 6],
#     [8, 0, 7], [8, 4, 8], [8, 7, 1], [8, 8, 5]
#     ], 9))