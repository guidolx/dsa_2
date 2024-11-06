import os
import random


BLOCK = 0
FREE = 1
VISITED = 5
STEP = 2

# Initialize a string direction which represents all the directions.
direction = "DLRU"

# Arrays to represent change in rows and columns
# cell values match the values in direction 
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

# Start and Destination Cell Coordinates
start = (0,9)
end = (20,11)

# all visited cells
visited = []

# maze
# Value 1 represents a cell that is walkable
# Value 0 represents a blocked cell (wall)
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
] 


def available_directions(row, col):
    directions = []
    for i in range(4):
        # Find the next row based on the current row (row)
        # and the dr[] array
        next_row = row + dr[i]
        # Find the next column based on the current column
        # (col) and the dc[] array
        next_col = col + dc[i]

        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            directions.append((next_row,next_col))
    return directions



# Function to check if cell(row, col) 
# is inside the maze
# and unblocked (has value 1)
def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == FREE

# Function to get all valid paths
def find_path(row, col, maze, dest_row,dest_col, solution, current_path):
    # If we reach the destination cell of the matrix, add
    # the current path to solution and return
    if row == dest_row and col == dest_col:
        solution.append(current_path)
        return
    # Mark the current cell as blocked
    maze[row][col] = BLOCK

    for i in range(4):
        # Find the next row based on the current row (row)
        # and the dr[] array
        next_row = row + dr[i]
        # Find the next column based on the current column
        # (col) and the dc[] array
        next_col = col + dc[i]

        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            current_path += direction[i]
            # Recursively call the find_path function for
            # the next cell
            discard = find_path(next_row, next_col, maze, dest_row, dest_col, solution, current_path)
            # Remove the last direction when backtracking
            current_path = current_path[:-1]
            # keep the cell in the visited list
            if discard == False:
                visited.append((next_row, next_col))
            

    # Mark the current cell as unblocked
    maze[row][col] = FREE

# Function to get all valid paths with random moves
def find_path_lv(row, col, maze, dest_row,dest_col, solution, current_path, count):
    
    max = 400     
    stack = []
    count = 0
    stack.append((row,col))
    maze[row][col] = VISITED
    while len(stack) > 0 and count < max:
        directions = available_directions(row,col)
        n = len(directions)
        cell = None
        if n > 0:    
            i = random.randint(0,len(directions) - 1)
            cell = directions.pop(i)
            stack.append(cell)
        elif len(stack) > 0:
            cell = stack.pop()
        else:
            # no further direction available
            # no solution
            return
        
        
        # mark cell visited
        maze[cell[0]][cell[1]] = VISITED

        # If we reach the destination cell of the matrix, add
        # the current path to solution and return
        if cell[0] == dest_row and cell[1] == dest_col:
            solution.append(current_path)
            return
        row = cell[0]
        col = cell[1]
        count += 1
        

def print_maze(path_list):
    maze_local = [row[:] for row in maze]
    row,col = start
    maze_local[row][col] = 2
    for path in path_list:
        for step in path:
            if step == 'D':
                row = row + 1
            elif step == 'U':
                row = row - 1
            elif step == 'L':
                col = col - 1
            elif step == 'R':
                col = col + 1
            maze_local[row][col] = 2
    
    for r,c in visited:
        maze_local[r][c] = 5
    
    maze_str = []
    for row in maze_local:
        s = ''.join(str(x) for x in row).replace('0','□').replace('1',' ').replace('2','·').replace('5','V')
        maze_str.append(s)

    for r in maze_str:
        print('\t' + r)

   

if __name__ == '__main__':
    n = len(maze)
    # List to store all the valid paths
    result = []
    # Store current path

    current_path = ""

    choice = int(input("Maze solver:\nPress 1 to run the Las Vegas algorithm \nPress 2 to run the recursive backtracking algorithm "))

    if choice == 1:
        find_path_lv(start[0], start[1], maze, end[0], end[1], result, current_path,0)
    else:
        find_path(start[0], start[1], maze, end[0], end[1], result, current_path)
    
    solved = len(result) > 0
    print("Maze solved {solved} : ".join(result))
    print_maze(result) 

            