import os
from matplotlib.image import imread

def extract_maze_from_image():
    result = []
    image = imread(os.getcwd() + '/assignment/task_1_maze_solver/maze-2.png')
    j = 1
    for row in image:
        if j % 10 == 0:
            cr = []
            result.append(cr)
        i = 1
        for pixel in row:
            if i % 10 == 0 and j % 10 == 0:
                if pixel[0] == 0: cr.append('1')
                elif pixel[0] == 1: cr.append(' ')
            i = i + 1
        j = j + 1
    for row in result:
        #print(''.join(row))
        print(row)
 