
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'targetsWithMostArrows' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER size
#  2. STRING targets
# Aryan Jeena - ACSL Intermediate Contest 4


def targetsWithMostArrows(size, targets):
        # Create the grid
        grid = [[' ' for _ in range(size)] for _ in range(size)]

        # Input targets into the grid
        target_list = targets.split()
        for target in target_list:
            row = int(target[0])
            col = int(target[1])
            grid[row][col] = 'T'
    
    
        # Iterate from each perimeter square
        directions = [
            (1, 0),     # Straight down
            (0, 1),     # Straight right
            (-1, 0),    # Straight up
            (0, -1),    # Straight left
            (1, 1),     # Diagonally down and to the right (Southeast)
            (1, -1),    # Diagonally down and to the left (Southwest)
            (-1, 1),    # Diagonally up and to the right (Northeast)
            (-1, -1)    # Diagonally up and to the left (Northwest)
        ]
    
        target_counts = {target: 0 for target in target_list}
    
        for row in range(size):
            for col in range(size):
                if row == 0 or row == size - 1 or col == 0 or col == size - 1:
                    for direction in directions:
                        current_row = row
                        current_col = col
    
                        while (
                            current_row >= 0
                            and current_row < size
                            and current_col >= 0
                            and current_col < size
                        ):
                            if grid[current_row][current_col] == 'T':
                                target_counts[str(current_row) + str(current_col)] += 1
                                break
    
                            current_row += direction[0]
                            current_col += direction[1]
    
        # Find the maximum count
        max_count = max(target_counts.values())
    
        # Find all targets with the maximum count
        max_targets = [target for target, count in target_counts.items() if count == max_count]
    
        # Sort the maximum targets by numerical value
        max_targets.sort(key=lambda x: int(x))
    
        # Output information for each target
        for target in target_list:
            count = target_counts[target]
    
        result = ' '.join(max_targets)
        print (result)
        
usersize = input("Please enter an integer size for the sides of the square grid: ")
usertargets = input("Please enter a string of targets with its coordinates represented as xy with spaces between each individual target: ")

targetsWithMostArrows(int(usersize),usertargets)