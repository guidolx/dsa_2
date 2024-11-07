import os
import random

# Possible cell values (blocked = wall, explorable, visited, step of the path to the solution)
BLOCKED = 0
EXPLORABLE = 1
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


def available_directions(row, col,maze):
    directions = []
    # i is the index included in the tuple 
    # to match the character in the direction string.
    for i in range(4):
        # Find the next row based on the current row (row)
        # and the dr[] array
        next_row = row + dr[i]
        # Find the next column based on the current column
        # (col) and the dc[] array
        next_col = col + dc[i]

        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            directions.append((next_row,next_col,i))
    return directions



# Function to check if cell(row, col) 
# is inside the maze
# and unblocked (has value 1)
def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == EXPLORABLE

# Deterministic function to get all valid paths if any
def find_path(row, col, maze, dest_row,dest_col, solution, current_path):
    # If we reach the destination cell of the matrix, add
    # the current path to solution and return
    if row == dest_row and col == dest_col:
        solution.append(current_path)
        return
    # Mark the current cell as blocked
    maze[row][col] = BLOCKED

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
            visited.append((next_row, next_col))
            # Recursively call the find_path function for
            # the next cell
            find_path(next_row, next_col, maze, dest_row, dest_col, solution, current_path)
            # Remove the last direction when backtracking
            current_path = current_path[:-1]
            
            

    # Mark the current cell as unblocked
    maze[row][col] = EXPLORABLE

# Las Vegas based function to explore 
# the maze based on random choice 
# regarding the direction to take.
def find_path_lv(row, col, maze, dest_row,dest_col, solution):
    
    max = 400     
    stack = []
    count = 0
    stack.append((row,col))
    maze[row][col] = VISITED
    while len(stack) > 0 and count < max:
        directions = available_directions(row,col,maze)
        n = len(directions)
        cell = None
        if n > 0:    
            i = random.randint(0,len(directions) - 1)
            cell = directions.pop(i)
            stack.append(cell)
             # mark cell visited
            maze[cell[0]][cell[1]] = VISITED
            visited.append((cell[0], cell[1]))
        elif len(stack) > 0:
            cell = stack.pop()
        else:
            # no further direction available
            # no solution
            return
        
                          
        # If we reach the destination cell of the matrix, add
        # the current path to solution and return
        if cell[0] == dest_row and cell[1] == dest_col:
            solution.append('S')
            return
        row = cell[0]
        col = cell[1]
        count += 1
        

# Returns a copy of the maze in order 
# to preserve the state of the original maze
# for further runs. 
def copy_maze():
    return [row[:] for row in maze]

# Prints the paths, the maze and the cells visited.
# Walls are represented as squares and visited cells as dots.
def print_maze(maze, path_list,print_is_solved=False):
    if print_is_solved:
        print(f"Maze is solved = {solved} : " + "".join(result))
        
    maze_local = [row[:] for row in maze]
    row,col = start
    maze_local[row][col] = STEP
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
            maze_local[row][col] = STEP
            
    
    for r,c in visited:
        if maze_local[r][c] != STEP:
            maze_local[r][c] = VISITED
    
    maze_str = []
    for row in maze_local:
        s = ''.join(str(x) for x in row).replace('0','□').replace('1',' ').replace('2','·').replace('5','V')
        maze_str.append(s)

    for r in maze_str:
        print('\t' + r)
    
    
    print("\n\nVisited cells: " + str(len(visited)))
    #print(visited)


   

if __name__ == '__main__':
    n = len(maze)
    # List to store all the valid paths
    result = []
    # Store current path

    current_path = ""

    # print pristine maze 
    print_maze(maze,'')

    choice = int(input("Maze solver:\nPress 1 to run the Las Vegas algorithm \nPress 2 to run the recursive backtracking algorithm\nPress 3 to run the LV algoritm 10000 times\nPress 4 to run the deterministic algoritm 10000 times\n"))

    if choice == 1:
        maze_loc = copy_maze()
        find_path_lv(start[0], start[1], maze_loc, end[0], end[1], result)
        solved = len(result) > 0
        print_maze(maze_loc, result,True) 
    elif choice == 2:
        maze_loc = copy_maze()
        find_path(start[0], start[1], maze_loc, end[0], end[1], result, current_path)
        solved = len(result) > 0
        print_maze(maze_loc, result,True) 
    elif choice == 3:
        count = 0
        max = 10000
        solved_counter = 0
        visited = []
        for i in range(0,max):
            maze_loc = copy_maze()
            find_path_lv(start[0], start[1], maze_loc, end[0], end[1], result)
            if len(result) > 0:
               solved_counter += 1

        print(f'Success rate {((solved_counter/max)*100):.5f}%')  
    elif choice == 4:
        count = 0
        max = 10000
        solved_counter = 0
        visited = []
        for i in range(0,max):
            maze_loc = copy_maze()
            find_path(start[0], start[1], maze_loc, end[0], end[1], result, current_path)
            if len(result) > 0:
               solved_counter += 1

        print(f'Success rate {((solved_counter/max)*100):.5f}%')  
    
    
            