import os
import subprocess
import time
import ast
import astunparse
import ast
import re
import importlib.util
from openai import OpenAI
import dataset
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import argparse

stream = False

Astar_intro_prompt = """The goal is to solve the problems given by implementing the A* search algorithm. The initialize function, which initializes the visited_costs dictionary and the priority queue and encodes all of the information about the initial state and other variables given in the problem (ie a given matrix, eligible actions, goal coordinate, initial state of the board, etc) must be encoded as a separate function.

"""
Astar_problmes = {
    1: """In the 8-puzzle game, you are given a grid with numbered square tiles arranged randomly and one tile missing. The goal is to arrange the tiles in descending order by sliding them into the empty space. The tiles can move in 4 directions: left, right, up, and down.  Given the initial state of the puzzle below, where the empty spot is represented as “_”, provide the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state. The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner. The solution should be a list of numbers in Python format, where each number represents the number on the tile that the empty spot is swapped with at each turn. Initial state of the puzzle: [[55, 43, 17], [97, 35, 9], [12, 25, '_']]

```python
import heapq


def initialize():
   # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
   initial_state = ((55, 43, 17), (97, 35, 9), (12, 25, '_'))
   goal_state = ((97, 55, 43), (35, 25, 17), (12, 9, '_'))   
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes swapping any of the tiles neighboring the empty spot, with the empty spot
       # Generate the coordinates of the tiles neighboring "_"
       empty_row, empty_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           swap_row, swap_col = empty_row + d_row, empty_col + d_col
           # Check if the swap is valid, ie if the coordinate of the tile to be swapped is a valid coordinate within the bounds of the board
           if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_swapped = new_state[swap_row][swap_col]
               # Do the swap
               new_state[empty_row][empty_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[empty_row][empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [number_to_be_swapped], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
   # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "_" when finding the goal position of each tile, thus ignore the "_" tile
           if state[i][j] != '_':
               # Get goal position of each tile
               goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the tile to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
```

""",
    2: """The game of 'Sort It' begins with 3 tubes, each filled with 4 balls of different colors. The goal is to sort the balls by color, with each tube containing balls of only one color. Only one ball can be moved at a time, taken from the top of one tube and placed on top of another. The capacity of each tube (maximum number of balls we can fit in each tube) is 6 balls. It is not allowed to place a ball in a tube that already has 6 balls. The solution should be a list of tuples, each containing, first, the index of the tube from which a ball is taken and, second, the index of the tube to which it is moved, indexing from 0. Given the initial state of the tubes, represented by the lists below (with the leftmost item being the color of the topmost ball in each tube), what is the shortest list of move tuples that will result in all the balls being correctly sorted? [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]


```python
import heapq
from collections import Counter


def initialize():
   # Define the initial state of the tubes, as a 2d tuple of color of the balls in tubes 0 to 2
   initial_state = (('Green', 'Red', 'Green', 'Red'), ('Blue', 'Blue', 'Red', 'Green'), ('Red', 'Blue', 'Green', 'Blue'))
  
   # Encoding other variables given in the problem statement
   num_tubes = 3
   capacity = 6


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the tubes, number of tubes, and capacity of each tube)
   initial_state, num_tubes, capacity, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where each tube only contains balls of 1 single color
       if all(len(set(tube)) <= 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from any of the 3 tubes to another tube
       for from_tube_ind in range(num_tubes):
           for to_tube_ind in range(num_tubes):
               # Check if the new state would be valid, ie from_tube and to_tube must not be the same tube
               # And from_tube must at least have 1 ball to move and the to_tube cannot be at capacity
               if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   # The ball to move is the topmost ball in the from_tube, at index 0
                   ball_to_move = new_state[from_tube_ind].pop(0)
                   # Add the ball to the top of the to_tube
                   new_state[to_tube_ind].insert(0, ball_to_move)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(from_tube_ind, to_tube_ind)], new_state))
   return None


def heuristic(tubes):
   # An admissible and consistent heuristic for this problem is the count of balls that are not the same color as the most frequent color in their tube
   # This heuristic relaxes the constraint that only the ball at the top of the tube can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched ball must be moved at least once
   # It's consistent because moving a ball from one tube to another reduces the heuristic cost of the successor node by a max of 1 (if the moved ball's color matches the most common color in the new tube but not in the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for tube in tubes:
       if tube:
           # If there are ties in the frequency of colors, the most_commonm_color must be match the color of the balls lower that are in the tube, as moving lower balls is costlier          
           reversed_tube = tube[:]
           reversed_tube = reversed_tube[::-1]
           # Get the most common color
           most_common_color = Counter(reversed_tube).most_common(1)[0][0]
           for ball in tube:
               if ball != most_common_color:
                   h += 1
   return h


print(a_star())
```

""",
    3: """Given 6 labeled water jugs with capacities 37, 133, 38, 72, 41, 23, 122 liters, we aim to fill 3 unlabeled buckets, numbered 1 to 3 and arranged in a line in ascending order, with 195, 224, 268 liters of water respectively. The amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed before it. Jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled. An action, represented as a tuple ('+', X, Y) or ('-', X, Y), involves adding to or removing water from the unlabeled bucket numbered Y, using the jug with capacity X. Determine the shortest sequence of actions needed to fill the buckets as specified, and present the solution as a list of action tuples in Python syntax.


```python
from heapq import heappush, heappop


def initialize():
   # Define the capacities of the jugs, the goal state, and initial state, with states having an immutable data type
   jugs = [37, 133, 38, 72, 41, 23, 122]
   goal_state = (195, 224, 268)
   initial_state = (0, 0, 0)
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return jugs, goal_state, initial_state, num_buckets, visited_costs, queue
  
def a_star():
  
   jugs, goal_state, initial_state, num_buckets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heappop(queue)


       # If the amount of water in the buckets in the current state equal the goal amounts, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes adding or subtracting water using any of the 6 jugs to any of the 3 buckets
       # Iterating through capacities of jugs and index of buckets as the action tuples must include the operation ('+' or '-'), capacity of the jug used, and the index of the bucket affected
       for jug in jugs:
           for bucket_ind in range(num_buckets):
               # Check if adding water using the current jug results in a valid state, ie the addition must not result in overflowing any of the buckets
               if (state[bucket_ind] + jug <= goal_state[bucket_ind]):
                   temp_state = list(state)[:]
                   temp_state[bucket_ind] += jug
                   # And the new state must maintain the constraint on the relative amount of water in the buckets based on their order
                   if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                       # Generate the new state
                       new_state = tuple(temp_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required  to fill the buckets with the designated amount of water
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, jugs)
                           # In the problem statement the buckets are indexed starting from 1, thus must add 1 to the bucket_ind
                           heappush(queue, (new_cost + h, new_cost,  actions + [('+', jug, bucket_ind+1)], new_state))
              
               # Check if removing water from the bucket results in a valid state. The buckest cannot have a negative amount of water
               if state[bucket_ind] - jug >= 0:
                   temp_state = list(state)[:]
                   temp_state[bucket_ind] -= jug
                   # The constraint on the relative amount of water in the buckets based on their order must hold after this action
                   if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                       new_state = tuple(temp_state)
                       new_cost = g + 1
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, jugs)
                           heappush(queue, (new_cost + h, new_cost, actions + [('-', jug, bucket_ind+1)], new_state))
   return None




def heuristic(buckets_state, buckets_goal, jugs):
   # The heuristic function can be a simulation of filling buckets greedily, using the next largest jug repeatedly as long as the amount of water in the bucket does not exceed the goal amount
   # This heuristic is admissible because it is greedy, always opting for the action that fills the buckets the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if water is removed from a bucket, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of water that can be added to the bucket is by using the largest jug that won't cause an overflow, which is exactly the jug used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the jugs by decreasing capacity
   jugs = sorted(jugs, reverse=True)
   # Iterate through the buckets
   for i in range(len(buckets_state)):
       bucket_fill = buckets_state[i]
       goal = buckets_goal[i]
       # Fill the bucket using the next largest jug as long as the bucket does not overflows
       for jug in jugs:
           while bucket_fill + jug < goal:
               bucket_fill += jug
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
```

""",
    4: """Using the provided matrix map of a city, where numbers represent travel time in minutes (all numbers are positive integers) and 'x' marks closed workshops, find the quickest route for Ben to travel from his current workshop at index (3, 8) to his destination workshop at index (6, 1), indexing from 0. Ben's car can move north, south, east, or west from a given crossroad, provided there's no x in that direction. Also, there are 3 districts in the city with district 1 covering rows 0 to 3, district 2 covering rows 4 to 5, and district 3 covering rows 6 to 8. Ben has to visit at least 1 workshop in each district on his path to the destination. The roads are bidirectional. The answer should be a list of tuples (in Python syntax) indicating the index of workshops on Ben's path. The start and end workshops must be included in the path.
[19 x 1 x 2 17 x x x]
[x x 14 x 11 x x 18 x]
[19 x 19 7 x 6 x x x]
[6 x x 3 x 8 10 x 16]
[3 7 x 14 x 10 9 6 15]
[13 x 6 1 x x x 12 14]
[x 8 5 16 14 x 10 5 16]
[18 4 9 1 11 9 9 18 13]
[x x 16 13 16 x 17 x 11]

```python
import heapq


def initialize():
   # Define the city, encoding travel times as integers and closed workshops as 'x'
   city = [[19, 'x', 1, 'x', 2, 17, 'x', 'x', 'x'],
           ['x', 'x', 14, 'x', 11, 'x', 'x', 18, 'x'],
           [19, 'x', 19, 7, 'x', 6, 'x', 'x', 'x'],
           [6, 'x', 'x', 3, 'x', 8, 10, 'x', 16],
           [3, 7, 'x', 14, 'x', 10, 9, 6, 15],
           [13, 'x', 6, 1, 'x', 'x', 'x', 12, 14],
           ['x', 8, 5, 16, 14, 'x', 10, 5, 16],
           [18, 4, 9, 1, 11, 9, 9, 18, 13],
           ['x', 'x', 16, 13, 16, 'x', 17, 'x', 11]]


   # Encoding other variables of the problem
   num_rows = 9
   num_cols = 9
   initial_coordinate = (3, 8)
   goal_coordinate = (6, 1)
   district_1_last_row = 3
   district_2_last_row = 5


   visited_costs = {}
   visited_costs[initial_coordinate] = 0
          
   # The information we must encode for each state includes Ben's current coordinate and wether or not he has visited any of the 3 districts on his path to the current workshop in the following format: (state_coordinate, visited_d1, visited_d1, visited_d2, visited_d3)
   # Since the initial coordinate is in district 1 (in row 3 which is the last row of district 1), we must set visited_d1 to True
   initial_state = (initial_coordinate, True, False, False)
   # Ben has already visited the initial_coordinate, so it must be added to his path
   queue = [(0, 0, [initial_coordinate], initial_state)]
  
   return city, num_rows, num_cols, initial_coordinate, goal_coordinate, district_1_last_row, district_2_last_row, visited_costs, initial_state, queue
  
def a_star():
  
   city, num_rows, num_cols, initial_coordinate, goal_coordinate, district_1_last_row, district_2_last_row, visited_costs, initial_state, queue = initialize()
  
   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_coord, visited_d1, visited_d2, visited_d3 = state


       # If Ben's current coordinate is the goal coordinate, and he has visited all 3 districts on his path to the goal coordinate, return his path
       if state_coord == goal_coordinate and visited_d1 and visited_d2 and visited_d3:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state_coord[0] + d_row, state_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new workshop is within the bounds of the city and it is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
               # To generate the new state, we must update the districts that Ben has visited
               # In the new state, the districts Ben visited will include all the districts from the current state, as well as the district where the new coordinate is located
               visited_d1_new = state[1]
               visited_d2_new = state[2]
               visited_d3_new = state[3]
               if 0 <= new_row <= district_1_last_row:
                   visited_d1_new = True
               elif district_1_last_row < new_row <= district_2_last_row:
                   visited_d2_new = True
               elif district_2_last_row < new_row <= num_rows - 1:
                   visited_d3_new = True
               # Generate the new state
               new_state = ((new_row, new_col), visited_d1_new, visited_d2_new, visited_d3_new)
               # Cost of the new state is the travel time to get to the new workshop in the city matrix
               new_cost = g + int(city[new_row][new_col])


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The coordinate of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state_coord, goal_coordinate), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraints that the travel time between different workshops is not the same, that we cannot travel through the workshops that are closed, and that Ben has to visit all 3 districts; ie It presumes we can move directly to any given coordinate toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one workshop to an adjacent workshop is the travel time between the workshops, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
```

""",
    5: """In the magic square problem, a 4x4 grid is filled with unique integers ranging from 29 to 54. Some numbers are already given, while others are unknown and represented as 'x'. The sums of columns must be None, 148, 196, None for columns 0 to 3 respectively, and the sums of rows must be None, 187, 149, None for rows 0 to 3 respectively, where None means that we do not have any constraints on the sum of the numbers in the row or column at that index. Also, the sum of the numbers in the diagonal from the top left to the bottom right corner of the grid should equal 166. The goal is to find unique integers in the given range to replace with ‘x’s in the grid below such that the sum of the specified rows, columns, and diagonal equals the given amounts and the sum of all of the numbers in the grid is as low as possible. The solution should be provided as a list of tuples in Python syntax. Each tuple should contain three numbers: the row index, the column index (both starting from 0), and the value of the unknown number at that position.\n\nGrid:\n [[47 x x 32]\n [x x x 49]\n [x 31 50 x]\n [x x 52 30]]

```python
import heapq
import math
import numpy as np


def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = (('47', 'x', 'x', '32'),
                   ('x', 'x', 'x', '49'),
                   ('x', '31', '50', 'x'),
                   ('x', 'x', '52', '30'))
   num_rows = 4
   num_cols = 4
   row_sums = [None, 187, 149, None]
   col_sums = [None, 148, 196, None]
   diagonal_sum = 166
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(29, 54))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check whether the current state is the goal state
       x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
       if not x_coords:
           # Convert the cells of the state to ints to calculate and compare the sum of the specific positions in the current state with the given goal sums
           state_array = np.array([[int(element) for element in row] for row in state])
           if (np.all([i == j for i, j in zip(np.sum(state_array, axis=0), col_sums) if j]) and
               np.all([i == j for i, j in zip(np.sum(state_array, axis=1), row_sums) if j]) and
               np.trace(state_array) == diagonal_sum):
               return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range
       else:
           first_x_coord = x_coords[0]
           # The number must be unique and not be present in any other cells of the grid
           used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
           for number in numbers:
               # Check if the new state, containing the new number, would be valid; ie the number must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new number
               sum_x_row_new_state = sum(int(cell) for cell in state[first_x_coord[0]] if cell != 'x') + number
               sum_x_col_new_state = sum(int(state[k][first_x_coord[1]]) for k in range(num_rows) if state[k][first_x_coord[1]] != 'x') + number
               sum_diag_new_state = sum(int(state[k][k]) for k in range(num_rows) if state[k][k] != 'x') + number
               if (number not in used_numbers and
                   # If the x is in one of the rows with a given sum, then the sum of the new row, with addition of the number, must not exceed the target sum
                   (row_sums[first_x_coord[0]] is None or sum_x_row_new_state <= row_sums[first_x_coord[0]]) and
                   # Similarly, if the x position is in a column or the diagonal with a goal sum
                   (col_sums[first_x_coord[1]] is None or sum_x_col_new_state <= col_sums[first_x_coord[1]]) and
                   (first_x_coord[0] != first_x_coord[1] or sum_diag_new_state <= diagonal_sum)):
              
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                   new_cost = g + number
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, row_sums, numbers)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_x_coord[0], first_x_coord[1], number)], new_state))
   return None




def heuristic(state, row_sums, numbers):
   # Relax the columns and diagonal sum constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the given and current row sums, for rows with a specified sum value that have at least one unknown number, filling other x with the smallest unique number
   # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the sum of the rows equals their goal sums and there are no unknown numbers to fill in the grid


   # Get numbers not used in the state currently
   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
   available_numbers = sorted(list(numbers - used_numbers))
   h = 0
   for i in range(len(state)):
       if row_sums[i] is not None:
           row_full = True
           sum_row = sum(int(cell) for cell in state[i] if cell != 'x')
           # Check to see if the row with a target some has any more xs
           for cell in state[i]:
               if cell == 'x':
                   row_full = False
          
           if not row_full:  
               h += row_sums[i] - sum_row
           # Otherwise the sum of a row must equal the target sum or there's no path to reach the goal state from this state. Return math.inf
           else:
               if sum_row != row_sums[i]:
                   return math.inf
      
       # For other rows, greedily fill the x positions with the smallest unique number in the range
       else:
           for cell in state[i]:
               if cell == 'x' and available_numbers:
                   h += available_numbers.pop(0)
   return h


print(a_star())
```

"""
}
Astar_inst_prompt = """Solve the below problem in the same format by encoding the problem states as a graph and implementing an A* search algorithm. Initialize visited_costs and the priority queue and encode all the variables given in the problem in the initialize function. The a_star function must be a generic, only encoding the A* algorithm, not any values or attributes given in the problem. Explain the rationale behind each line of code using comments. The solution must be reported in the instructed format, as a python list.

####
"""

Initialize_intro_prompt = """The goal is to implement the initialize function for the given A* algorithm. The initialize function must initialize the visited_costs dictionary and the priority queue and encode all of the information about the initial state and other variables given in the problem (ie a given matrix, eligible actions, goal coordinate, initial state of the board, etc)

"""
Initialize_problems = {
    1: """In the 8-puzzle game, you are given a grid with numbered square tiles arranged randomly and one tile missing. The goal is to arrange the tiles in descending order by sliding them into the empty space. The tiles can move in 4 directions: left, right, up, and down.  Given the initial state of the puzzle below, where the empty spot is represented as “_”, provide the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state. The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner. The solution should be a list of numbers in Python format, where each number represents the number on the tile that the empty spot is swapped with at each turn. Initial state of the puzzle: [[55, 43, 17], [97, 35, 9], [12, 25, '_']]

```python
import heapq  


def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes swapping any of the tiles neighboring the empty spot, with the empty spot
       # Generate the coordinates of the tiles neighboring "_"
       empty_row, empty_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           swap_row, swap_col = empty_row + d_row, empty_col + d_col
           # Check if the swap is valid, ie if the coordinate of the tile to be swapped is a valid coordinate within the bounds of the board
           if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_swapped = new_state[swap_row][swap_col]
               # Do the swap
               new_state[empty_row][empty_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[empty_row][empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [number_to_be_swapped], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
   # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "_" when finding the goal position of each tile, thus ignore the "_" tile
           if state[i][j] != '_':
               # Get goal position of each tile
               goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the tile to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
```

The target initialize function:
```python
def initialize():
   # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
   initial_state = ((55, 43, 17), (97, 35, 9), (12, 25, '_'))
   goal_state = ((97, 55, 43), (35, 25, 17), (12, 9, '_'))   
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, num_rows, num_cols, visited_costs, queue
```

""",
    2: """The game of 'Sort It' begins with 3 tubes, each filled with 4 balls of different colors. The goal is to sort the balls by color, with each tube containing balls of only one color. Only one ball can be moved at a time, taken from the top of one tube and placed on top of another. The capacity of each tube (maximum number of balls we can fit in each tube) is 6 balls. It is not allowed to place a ball in a tube that already has 6 balls. The solution should be a list of tuples, each containing, first, the index of the tube from which a ball is taken and, second, the index of the tube to which it is moved, indexing from 0. Given the initial state of the tubes, represented by the lists below (with the leftmost item being the color of the topmost ball in each tube), what is the shortest list of move tuples that will result in all the balls being correctly sorted? [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]


```python
import heapq
from collections import Counter


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the tubes, number of tubes, and capacity of each tube)
   initial_state, num_tubes, capacity, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where each tube only contains balls of 1 single color
       if all(len(set(tube)) <= 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from any of the 3 tubes to another tube
       for from_tube_ind in range(num_tubes):
           for to_tube_ind in range(num_tubes):
               # Check if the new state would be valid, ie from_tube and to_tube must not be the same tube
               # And from_tube must at least have 1 ball to move and the to_tube cannot be at capacity
               if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   # The ball to move is the topmost ball in the from_tube, at index 0
                   ball_to_move = new_state[from_tube_ind].pop(0)
                   # Add the ball to the top of the to_tube
                   new_state[to_tube_ind].insert(0, ball_to_move)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(from_tube_ind, to_tube_ind)], new_state))
   return None


def heuristic(tubes):
   # An admissible and consistent heuristic for this problem is the count of balls that are not the same color as the most frequent color in their tube
   # This heuristic relaxes the constraint that only the ball at the top of the tube can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched ball must be moved at least once
   # It's consistent because moving a ball from one tube to another reduces the heuristic cost of the successor node by a max of 1 (if the moved ball's color matches the most common color in the new tube but not in the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for tube in tubes:
       if tube:
           # If there are ties in the frequency of colors, the most_commonm_color must be match the color of the balls lower that are in the tube, as moving lower balls is costlier          
           reversed_tube = tube[:]
           reversed_tube = reversed_tube[::-1]
           # Get the most common color
           most_common_color = Counter(reversed_tube).most_common(1)[0][0]
           for ball in tube:
               if ball != most_common_color:
                   h += 1
   return h


print(a_star())
```

The target initialize function:
```python
def initialize():
   # Define the initial state of the tubes, as a 2d tuple of color of the balls in tubes 0 to 2
   initial_state = (('Green', 'Red', 'Green', 'Red'), ('Blue', 'Blue', 'Red', 'Green'), ('Red', 'Blue', 'Green', 'Blue'))
  
   # Encoding other variables given in the problem statement
   num_tubes = 3
   capacity = 6


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, visited_costs, queue
```

""",
    3: """Given 6 labeled water jugs with capacities 37, 133, 38, 72, 41, 23, 122 liters, we aim to fill 3 unlabeled buckets, numbered 1 to 3 and arranged in a line in ascending order, with 195, 224, 268 liters of water respectively. The amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed before it. Jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled. An action, represented as a tuple ('+', X, Y) or ('-', X, Y), involves adding to or removing water from the unlabeled bucket numbered Y, using the jug with capacity X. Determine the shortest sequence of actions needed to fill the buckets as specified, and present the solution as a list of action tuples in Python syntax.


```python
from heapq import heappush, heappop
  
def a_star():
  
   jugs, goal_state, initial_state, num_buckets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heappop(queue)


       # If the amount of water in the buckets in the current state equal the goal amounts, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes adding or subtracting water using any of the 6 jugs to any of the 3 buckets
       # Iterating through capacities of jugs and index of buckets as the action tuples must include the operation ('+' or '-'), capacity of the jug used, and the index of the bucket affected
       for jug in jugs:
           for bucket_ind in range(num_buckets):
               # Check if adding water using the current jug results in a valid state, ie the addition must not result in overflowing any of the buckets
               if (state[bucket_ind] + jug <= goal_state[bucket_ind]):
                   temp_state = list(state)[:]
                   temp_state[bucket_ind] += jug
                   # And the new state must maintain the constraint on the relative amount of water in the buckets based on their order
                   if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                       # Generate the new state
                       new_state = tuple(temp_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required  to fill the buckets with the designated amount of water
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, jugs)
                           # In the problem statement the buckets are indexed starting from 1, thus must add 1 to the bucket_ind
                           heappush(queue, (new_cost + h, new_cost,  actions + [('+', jug, bucket_ind+1)], new_state))
              
               # Check if removing water from the bucket results in a valid state. The buckest cannot have a negative amount of water
               if state[bucket_ind] - jug >= 0:
                   temp_state = list(state)[:]
                   temp_state[bucket_ind] -= jug
                   # The constraint on the relative amount of water in the buckets based on their order must hold after this action
                   if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                       new_state = tuple(temp_state)
                       new_cost = g + 1
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, jugs)
                           heappush(queue, (new_cost + h, new_cost, actions + [('-', jug, bucket_ind+1)], new_state))
   return None




def heuristic(buckets_state, buckets_goal, jugs):
   # The heuristic function can be a simulation of filling buckets greedily, using the next largest jug repeatedly as long as the amount of water in the bucket does not exceed the goal amount
   # This heuristic is admissible because it is greedy, always opting for the action that fills the buckets the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if water is removed from a bucket, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of water that can be added to the bucket is by using the largest jug that won't cause an overflow, which is exactly the jug used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the jugs by decreasing capacity
   jugs = sorted(jugs, reverse=True)
   # Iterate through the buckets
   for i in range(len(buckets_state)):
       bucket_fill = buckets_state[i]
       goal = buckets_goal[i]
       # Fill the bucket using the next largest jug as long as the bucket does not overflows
       for jug in jugs:
           while bucket_fill + jug < goal:
               bucket_fill += jug
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
```

The target initialize function:
```python
def initialize():
   # Define the capacities of the jugs, the goal state, and initial state, with states having an immutable data type
   jugs = [37, 133, 38, 72, 41, 23, 122]
   goal_state = (195, 224, 268)
   initial_state = (0, 0, 0)
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return jugs, goal_state, initial_state, num_buckets, visited_costs, queue
```

""",
    4: """Using the provided matrix map of a city, where numbers represent travel time in minutes (all numbers are positive integers) and 'x' marks closed workshops, find the quickest route for Ben to travel from his current workshop at index (3, 8) to his destination workshop at index (6, 1), indexing from 0. Ben's car can move north, south, east, or west from a given crossroad, provided there's no x in that direction. Also, there are 3 districts in the city with district 1 covering rows 0 to 3, district 2 covering rows 4 to 5, and district 3 covering rows 6 to 8. Ben has to visit at least 1 workshop in each district on his path to the destination. The roads are bidirectional. The answer should be a list of tuples (in Python syntax) indicating the index of workshops on Ben's path. The start and end workshops must be included in the path.
[19 x 1 x 2 17 x x x]
[x x 14 x 11 x x 18 x]
[19 x 19 7 x 6 x x x]
[6 x x 3 x 8 10 x 16]
[3 7 x 14 x 10 9 6 15]
[13 x 6 1 x x x 12 14]
[x 8 5 16 14 x 10 5 16]
[18 4 9 1 11 9 9 18 13]
[x x 16 13 16 x 17 x 11]

```python
import heapq
  
def a_star():
  
   city, num_rows, num_cols, initial_coordinate, goal_coordinate, district_1_last_row, district_2_last_row, visited_costs, initial_state, queue = initialize()
  
   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_coord, visited_d1, visited_d2, visited_d3 = state


       # If Ben's current coordinate is the goal coordinate, and he has visited all 3 districts on his path to the goal coordinate, return his path
       if state_coord == goal_coordinate and visited_d1 and visited_d2 and visited_d3:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state_coord[0] + d_row, state_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new workshop is within the bounds of the city and it is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
               # To generate the new state, we must update the districts that Ben has visited
               # In the new state, the districts Ben visited will include all the districts from the current state, as well as the district where the new coordinate is located
               visited_d1_new = state[1]
               visited_d2_new = state[2]
               visited_d3_new = state[3]
               if 0 <= new_row <= district_1_last_row:
                   visited_d1_new = True
               elif district_1_last_row < new_row <= district_2_last_row:
                   visited_d2_new = True
               elif district_2_last_row < new_row <= num_rows - 1:
                   visited_d3_new = True
               # Generate the new state
               new_state = ((new_row, new_col), visited_d1_new, visited_d2_new, visited_d3_new)
               # Cost of the new state is the travel time to get to the new workshop in the city matrix
               new_cost = g + int(city[new_row][new_col])


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The coordinate of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state_coord, goal_coordinate), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraints that the travel time between different workshops is not the same, that we cannot travel through the workshops that are closed, and that Ben has to visit all 3 districts; ie It presumes we can move directly to any given coordinate toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one workshop to an adjacent workshop is the travel time between the workshops, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())


```

The target initialize function:
```python


def initialize():
   # Define the city, encoding travel times as integers and closed workshops as 'x'
   city = [[19, 'x', 1, 'x', 2, 17, 'x', 'x', 'x'],
           ['x', 'x', 14, 'x', 11, 'x', 'x', 18, 'x'],
           [19, 'x', 19, 7, 'x', 6, 'x', 'x', 'x'],
           [6, 'x', 'x', 3, 'x', 8, 10, 'x', 16],
           [3, 7, 'x', 14, 'x', 10, 9, 6, 15],
           [13, 'x', 6, 1, 'x', 'x', 'x', 12, 14],
           ['x', 8, 5, 16, 14, 'x', 10, 5, 16],
           [18, 4, 9, 1, 11, 9, 9, 18, 13],
           ['x', 'x', 16, 13, 16, 'x', 17, 'x', 11]]


   # Encoding other variables of the problem
   num_rows = 9
   num_cols = 9
   initial_coordinate = (3, 8)
   goal_coordinate = (6, 1)
   district_1_last_row = 3
   district_2_last_row = 5


   visited_costs = {}
   visited_costs[initial_coordinate] = 0
          
   # The information we must encode for each state includes Ben's current coordinate and whether or not he has visited any of the 3 districts on his path to the current workshop in the following format: (state_coordinate, visited_d1, visited_d1, visited_d2, visited_d3)
   # Since the initial coordinate is in district 1 (in row 3 which is the last row of district 1), we must set visited_d1 to True
   initial_state = (initial_coordinate, True, False, False)
   # Ben has already visited the initial_coordinate, so it must be added to his path
   queue = [(0, 0, [initial_coordinate], initial_state)]
  
   return city, num_rows, num_cols, initial_coordinate, goal_coordinate, district_1_last_row, district_2_last_row, visited_costs, initial_state, queue
```

""",
    5: """In the magic square problem, a 4x4 grid is filled with unique integers ranging from 29 to 54. Some numbers are already given, while others are unknown and represented as 'x'. The sums of columns must be None, 148, 196, None for columns 0 to 3 respectively, and the sums of rows must be None, 187, 149, None for rows 0 to 3 respectively, where None means that we do not have any constraints on the sum of the numbers in the row or column at that index. Also, the sum of the numbers in the diagonal from the top left to the bottom right corner of the grid should equal 166. The goal is to find unique integers in the given range to replace with ‘x’s in the grid below such that the sum of the specified rows, columns, and diagonal equals the given amounts and the sum of all of the numbers in the grid is as low as possible. The solution should be provided as a list of tuples in Python syntax. Each tuple should contain three numbers: the row index, the column index (both starting from 0), and the value of the unknown number at that position.\n\nGrid:\n [[47 x x 32]\n [x x x 49]\n [x 31 50 x]\n [x x 52 30]]

```python
import heapq
import math
import numpy as np
  
def a_star():
  
   initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check whether the current state is the goal state
       x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
       if not x_coords:
           # Convert the cells of the state to ints to calculate and compare the sum of the specific positions in the current state with the given goal sums
           state_array = np.array([[int(element) for element in row] for row in state])
           if (np.all([i == j for i, j in zip(np.sum(state_array, axis=0), col_sums) if j]) and
               np.all([i == j for i, j in zip(np.sum(state_array, axis=1), row_sums) if j]) and
               np.trace(state_array) == diagonal_sum):
               return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range
       else:
           first_x_coord = x_coords[0]
           # The number must be unique and not be present in any other cells of the grid
           used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
           for number in numbers:
               # Check if the new state, containing the new number, would be valid; ie the number must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new number
               sum_x_row_new_state = sum(int(cell) for cell in state[first_x_coord[0]] if cell != 'x') + number
               sum_x_col_new_state = sum(int(state[k][first_x_coord[1]]) for k in range(num_rows) if state[k][first_x_coord[1]] != 'x') + number
               sum_diag_new_state = sum(int(state[k][k]) for k in range(num_rows) if state[k][k] != 'x') + number
               if (number not in used_numbers and
                   # If the x is in one of the rows with a given sum, then the sum of the new row, with addition of the number, must not exceed the target sum
                   (row_sums[first_x_coord[0]] is None or sum_x_row_new_state <= row_sums[first_x_coord[0]]) and
                   # Similarly, if the x position is in a column or the diagonal with a goal sum
                   (col_sums[first_x_coord[1]] is None or sum_x_col_new_state <= col_sums[first_x_coord[1]]) and
                   (first_x_coord[0] != first_x_coord[1] or sum_diag_new_state <= diagonal_sum)):
              
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                   new_cost = g + number
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, row_sums, numbers)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_x_coord[0], first_x_coord[1], number)], new_state))
   return None




def heuristic(state, row_sums, numbers):
   # Relax the columns and diagonal sum constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the given and current row sums, for rows with a specified sum value that have at least one unknown number, filling other x with the smallest unique number
   # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the sum of the rows equals their goal sums and there are no unknown numbers to fill in the grid


   # Get numbers not used in the state currently
   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
   available_numbers = sorted(list(numbers - used_numbers))
   h = 0
   for i in range(len(state)):
       if row_sums[i] is not None:
           row_full = True
           sum_row = sum(int(cell) for cell in state[i] if cell != 'x')
           # Check to see if the row with a target some has any more xs
           for cell in state[i]:
               if cell == 'x':
                   row_full = False
          
           if not row_full:  
               h += row_sums[i] - sum_row
           # Otherwise the sum of a row must equal the target sum or there's no path to reach the goal state from this state. Return math.inf
           else:
               if sum_row != row_sums[i]:
                   return math.inf
      
       # For other rows, greedily fill the x positions with the smallest unique number in the range
       else:
           for cell in state[i]:
               if cell == 'x' and available_numbers:
                   h += available_numbers.pop(0)
   return h


print(a_star())
```

The target initialize function:
```python
def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = (('47', 'x', 'x', '32'),
                   ('x', 'x', 'x', '49'),
                   ('x', '31', '50', 'x'),
                   ('x', 'x', '52', '30'))
   num_rows = 4
   num_cols = 4
   row_sums = [None, 187, 149, None]
   col_sums = [None, 148, 196, None]
   diagonal_sum = 166
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(29, 54))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue
```

"""
}
Initialize_inst_prompt = """
####

Initialize the visited_costs dictionary and the priority queue and encode all the variables given of only the last problem in the initialize function as the examples provided above. The value of variables must match the information encoded in the problem statement.

The target initialize function:
"""

def get_model_response(system_input, user_input, model_name, 
                       temp, max_tokens, llama_model, tokenizer,
                       openai_key):
    if model_name == "gpt4" or model_name == "gpt3.5":
        if model_name == "gpt4":
            model_name = "gpt-4"
        elif model_name == "gpt3.5":
            model_name = "gpt-3.5-turbo"
            
        client = OpenAI(
            api_key=openai_key,
        )
            
        response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": system_input + user_input
            }
        ],
        temperature=temp,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        response = response.choices[0].message.content
    
    elif "llama" in model_name:
        chat = [
        {"role": "system", "content": system_input},
        {"role": "user", "content": user_input},
        ]
        inputs = tokenizer.apply_chat_template(chat, return_tensors="pt").to("cuda")
        output = llama_model.generate(input_ids=inputs, max_new_tokens=max_tokens, temperature=temp)
        output = output[0].to("cpu")
        response = tokenizer.decode(output)
    
    return response
   

def get_llm_completion(problem, model_name, system_prompt, user_prompt,
                       python_file, max_tokens, openai_key,llama_model,
                       tokenizer, print_stats, write=True, temp=0):
    user_prompt = user_prompt.replace("####", '"' + problem + '"')
    
    # Try to get openai's response 5 times, then give up
    tries = 10
    while tries >= 0:
        try:
            response = get_model_response(system_prompt, user_prompt,
                                          model_name, temp, max_tokens,
                                          llama_model, tokenizer, openai_key)
            break
        except Exception as e:
            if print_stats:
                print(e)
            if tries == 0:
                raise 
            else:
                # Wait a few seconds before retrying 
                time.sleep(6) 
                if "maximum context length" in str(e):
                    num_tokens_context = re.findall(r'-?\b\d+\b', str(e))[3]
                    max_tokens = 8192 - int(num_tokens_context)
                tries -= 1
                continue

    try:
        code_begin_index = find_nth(response, "```python", 1) + 9
        code_end_index = find_nth(response, "```", 2) 
        if code_end_index == -1 or code_begin_index == -1:
            raise ValueError
        code_llm = response[code_begin_index:code_end_index]
                
        if write:
            f = open(python_file, "w")
            f.write(code_llm)
            f.close()    
    except ValueError:
        return None, response
    
    return code_llm, response
            

def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def run_code_solution(file_path, execution_time_limit):
    cmd = ['python', file_path]
    killed = False
    not_executed = False
    error_message = None
    stdout, stderr = None, None
    execution_time = None

    try:
        # Run the process with a timeout
        start_time = time.time()
        completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=execution_time_limit)
        end_time = time.time()
        stdout, stderr = completed_process.stdout, completed_process.stderr
        execution_time = end_time - start_time

    except subprocess.TimeoutExpired:
        killed = True
        error_message = f"LLM-generated code was killed because it exceeded the time limit."
    except Exception as e:
        not_executed = True
        error_message = f"LLM-generated code returned the following error: " + str(e)

    if not killed and not not_executed:
        if stderr:
            not_executed = True
            error_message = f"LLM-generated code returned the following error: " + stderr.decode('ascii')
        elif not stdout:
            error_message = f"LLM-generated code executed successfully but no output produced by the LLM code."

    solution = stdout.decode('ascii') if stdout else None
    if not error_message and solution:
        try:
            solution = ast.literal_eval(solution)
        except:
            error_message = f"Error while parsing the output of the LLM-generated code."

    return solution, killed, not_executed, error_message, execution_time

    
     
def final_record_instances(log_file, count_feasible, count_correct, 
                 count_optimal, count_incomplete, count_killed, 
                 count_not_executed, dict_llm_sol, dict_llm_compute_t,
     infeasible_ids, total_number_calls, num_problems, llm_relative_compute_t):
    #log problems that were not solved due to incorrect formatting
    f = open(log_file, "a")   
    f.write("\n" + "-"*50 + "\n")
    f.write("ID of problems with infeasible solution")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(infeasible_ids))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count feasible solutions")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_feasible) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count correct solutions")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_correct) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count correct solutions with optimum cost")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_optimal) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count program killed")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_killed) + " \ " + str(num_problems))
    
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count program not executed")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_not_executed) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count code generation incomplete")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_incomplete) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("""dict {id of the problem: \n
            llm correct solution, cost correct solution, excecution time of the llm code} \n""")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(dict_llm_sol))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("dict {id of the problem: computation time of llm code returning correct solutions / computation time of the optimal A* code for this problem")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(dict_llm_compute_t))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("Average normalized computation time across all problmes for which llm generated a code returning a correct answer")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(llm_relative_compute_t) + "%")
    
    #total number of calls to LLM
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("total number of calls to LLM")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(total_number_calls))

    
def final_record_Astar(log_file_Astar, max_temp, repeat_max,
                       model, num_problems_to_iterate, num_calls):
    f = open(log_file_Astar, "a") 
    
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("model used")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(model)) 
    
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("max tempreture in multiple try")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(max_temp))
    
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("max number of tries for each problem to get a valid code")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(repeat_max))
    
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("number of easier problems we iterated through, a sum of {} times, to get the A* code".format(repeat_max))
    f.write("\n" + "-"*50 + "\n")
    f.write(str(num_problems_to_iterate))
    
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("number of calls made to the model. If less than {} then equlas number of attempts to get a code that satisfies the given constraints".format(repeat_max))
    f.write("\n" + "-"*50 + "\n")
    f.write(str(num_calls))

   
def record(id, log_file, llm_solution, problem, code_llm, report):
    f = open(log_file, "a")
    f.write("ID: " + str(id) + "\n" + str(problem) + "\n")
    f.write(report + "\n")
    f.write(str(code_llm)+ "\n")
    f.write("llm code run result: " + str(llm_solution) + "\n\n\n\n")
    f.close()
    
    
def replace_function_in_script(script_path, function_name, new_function_code):
    try:
        with open(script_path, 'r') as file:
            original_code = file.read()
            module = ast.parse(original_code)

        for node in module.body:
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                new_function_node = ast.parse(new_function_code).body[0]
                index = module.body.index(node)
                module.body[index] = new_function_node
                break

        new_script_code = astunparse.unparse(module)

        # Check if the new script code is same as original code, if not then only write to file
        if original_code != new_script_code:
            with open(script_path, 'w') as file:
                file.write(new_script_code)
        
        invalid_format = False
        return invalid_format
    except:
        invalid_format = True
        return invalid_format
    
        
def remove_initialize_function(script):
    pattern = r"def initialize\([^)]*\):.*?(?=^def|\Z)"

    # Use re.findall() to find all matches
    initialize_function = re.findall(pattern, script, flags=re.DOTALL|re.MULTILINE)[0]

    # Use re.sub() to replace all matches with an empty string
    new_script = re.sub(pattern, '', script, flags=re.DOTALL|re.MULTILINE)

    return new_script, initialize_function


def import_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_Astar_code_1st_MSMT(problems, model_name,
                log_file_Astar, problem_action_type, 
                python_dir_name, repeat_max, 
                max_temp, num_problems_to_iterate, 
                execution_time_limit, system_astar_prompt,
                user_astar_prompt, max_tokens, print_stats,
                openai_key,llama_model, tokenizer):
    
    total_number_calls = 0
    repeated = 0
    eligible_code = False
    while repeated < repeat_max and not eligible_code:
        for problem in problems:
            id = int(problem["diff_sorted_id"])
            if id > num_problems_to_iterate:
                break
            if repeated < repeat_max and not eligible_code:
                
                temp = (max_temp * repeated)/repeat_max
                python_file = python_dir_name + '/Astar_problem_{}.py'.format(id)
                
                code_llm, response = get_llm_completion(problem["problem_statement"], model_name, 
                                                    system_astar_prompt, user_astar_prompt,
                                                    python_file, max_tokens, openai_key,
                                                    llama_model, tokenizer, print_stats, temp=temp)
                total_number_calls += 1
                repeated += 1

                if not code_llm:
                    message = "Incomplete generation by the LLM. Failed to extract the complete code"
                    record(id, log_file_Astar, None, problem, response, message)
                    if print_stats:
                        print("Id {}: {}".format(id, message))
                    continue
                
                (llm_solution, _, _, 
                 error_message, _) = run_code_solution(python_file, execution_time_limit)
    
                if error_message:
                    message = error_message
                
                elif not llm_solution:
                    message = "Program returned None"
                    
                elif (not type(llm_solution) is list or
                    not (all(isinstance(item, problem_action_type) for item in llm_solution))): 
                    message = "Incorrect solution type"

                else:
                    message = "Code passed constraints!! Complete code extractred, code is excutable and the type of the solution returned is correct!!"
                    eligible_code = True
                
                if print_stats:   
                    print("Id {}: {}".format(id, message))
                record(id, log_file_Astar, llm_solution, problem, response, message)
                
            else:
                return  response, code_llm, eligible_code, total_number_calls

    return  response, code_llm, eligible_code, total_number_calls


def get_final_solutions(problems, model_name, log_file_instances, problem_action_type,
                        problem_type, python_dir_name, user_initialize_prompt_appneded,
                        system_initialize_prompt, Astar_code, max_tokens_initialize, 
                        print_stats, openai_key,llama_model,tokenizer, execution_time_limit):
    if print_stats:
        print("Iterating through instances of the problems")
    count_feasible = 0
    count_correct = 0
    count_optimal = 0
    count_incomplete = 0
    count_killed = 0
    count_not_executed = 0
    dict_llm_sol = {}
    dict_llm_compute_t = {}
    infeasible_ids = []
    total_number_calls = 0
    
    check = import_from_path("check", './{}/check.py'.format(problem_type))
    
    #write the base Astar code for all instances
    for problem in problems:
        python_file = python_dir_name + '/problem_{}.py'.format(problem["diff_sorted_id"])
        f = open(python_file, "w")
        f.write(Astar_code)
        f.close()
        
    try:
        for problem in problems:
            id = problem["diff_sorted_id"]
            python_file = python_dir_name + '/problem_{}.py'.format(id)
            
            initialize_code_llm, response = get_llm_completion(problem["problem_statement"],
                                                    model_name, system_initialize_prompt, 
                                                    user_initialize_prompt_appneded, 
                                                    python_file, max_tokens_initialize,
                                                    openai_key,llama_model,tokenizer,
                                                    print_stats, write=False)
            total_number_calls += 1
            
            if not initialize_code_llm:
                count_incomplete += 1
                message = "Incomplete generation by the LLM. Failed to extract the complete code"
                record(id, log_file_instances, None, problem, response, message)
                if print_stats:
                    print("Id {}: {}".format(id, message))
                continue
            
            #replace the initialize function 
            invalid_format = replace_function_in_script(python_file, 'initialize', initialize_code_llm)
                
            if not invalid_format:

                (llm_solution, killed, not_executed, error_message,
                 execution_time) = run_code_solution(python_file, execution_time_limit)

                #incorrect solution type or code is not executable or format of the llm solution does not fit the expected format:
                if error_message:
                    if killed:
                        count_killed += 1
                    elif not_executed:
                        count_not_executed += 1
                    message = error_message
                    infeasible_ids.append(id)
                
                elif not llm_solution:
                    message = "Program returned None"
                    infeasible_ids.append(id)
                    
                elif (not type(llm_solution) is list or
                    not (all(isinstance(item, problem_action_type)
                             for item in llm_solution))): 
                    infeasible_ids.append(id)
                    message = "Incorrect solution type"

                else:
                    message = ""
                    #check feasibility and correctness and record cost of the solution for given problem
                    if check.is_feasible(*problem["is_feasible_args"], llm_solution):
                        count_feasible += 1
                        message += "LLM solution is feasible!! "
                    else:
                        message += "LLM solution is NOT feasible "
                        infeasible_ids.append(id)
                    
                    is_correct, cost = check.is_correct(*problem["is_correct_args"], llm_solution)
                    if is_correct:
                        count_correct += 1
                        message += "LLM solution is correct!! "
                        
                        if cost == problem["opt_solution"]:
                            count_optimal += 1
                            message += "LLM solution is optimal!!"
                        
                        else:
                            message += "LLM solution is NOT optimal "
                            
                        dict_llm_sol[id] = (llm_solution, cost, execution_time)
                        dict_llm_compute_t[id] = round(execution_time*100/problem["opt_solution_compute_t"])
                        message += f"Computation time of LLM code is {dict_llm_compute_t[id]}% of the optimum A* code computation time"

                    else:
                        message += "LLM solution is NOT correct "
                
                if print_stats:        
                    print("Id {}: {}".format(id, message))
                record(id, log_file_instances, llm_solution, problem, response, message)
            
            
            #incorrect code format
            else:
                infeasible_ids.append(id)
                message = "Got an exception when trying to replace the initialize function for this instance"
                record(id, log_file_instances, None, problem, response, message)
                print("Id {}: {}".format(id, message))
            
        return (count_feasible, count_correct, count_optimal, count_incomplete, 
        count_killed, count_not_executed, dict_llm_sol, dict_llm_compute_t,
        infeasible_ids, total_number_calls)
    
    except Exception as e:
        print(e)
        return (count_feasible, count_correct, count_optimal, count_incomplete, 
        count_killed, count_not_executed, dict_llm_sol, dict_llm_compute_t,
        infeasible_ids, total_number_calls)
          
    

def run_experiment(prompting_method, model_name, problem_type,
                   problems, execution_time_limit, system_astar_prompt,
                   user_astar_prompt, system_initialize_prompt, 
                   user_initialize_prompt, max_tokens_astar, 
                   max_tokens_initialize, problem_action_type, 
                   repeat_max, max_temp,num_problems_to_iterate, print_stats,
                   openai_key,llama_model, tokenizer, dir_name): 
        
    python_dir_Astar = dir_name + f"/{model_name}_{prompting_method}_1st_{problem_type}_python_scripts"
    if not os.path.exists(python_dir_Astar):
        os.makedirs(python_dir_Astar)
    log_file_Astar = dir_name + f"/{model_name}_{prompting_method}_1st_{problem_type}_log_file.txt"

    num_problems = len(problems)
    
    with open(log_file_Astar, 'w') as f:
        f.write("model: {} \n".format(model_name))
        f.close()
    
    (response_llm, code_llm, 
     eligible_code, total_number_calls) = get_Astar_code_1st_MSMT(problems, model_name,
                                                log_file_Astar, problem_action_type, 
                                                python_dir_Astar, repeat_max, 
                                                max_temp, num_problems_to_iterate, 
                                                execution_time_limit, system_astar_prompt,
                                                user_astar_prompt, max_tokens_astar,print_stats,
                                                openai_key,llama_model, tokenizer)
    
    final_record_Astar(log_file_Astar, max_temp, repeat_max,
                       model_name, num_problems_to_iterate,total_number_calls)
    
    if eligible_code:
        python_dir_instances = dir_name + f"/{model_name}_{prompting_method}_2nd_{problem_type}_python_scripts"
        if not os.path.exists(python_dir_instances):
            os.makedirs(python_dir_instances)
        log_file_instances = dir_name + f"/{model_name}_{prompting_method}_2nd_{problem_type}_log_file.txt"

    
        #add the Astar code and reasoning to the prompt
        response_llm_no_initialize, initialize_function = remove_initialize_function(response_llm)
        
        code_llm_begin_index = find_nth(response_llm_no_initialize, "```python", 1) 
        code_llm_end_index = find_nth(response_llm_no_initialize, "```", 2) + 3
        code_llm_no_initialize = response_llm_no_initialize[code_llm_begin_index: code_llm_end_index]
        
        hash_index = user_initialize_prompt.find('####')
        initialize_prompt_appneded = (user_initialize_prompt[:hash_index + 4] + 
                                      "\n" + code_llm_no_initialize + 
                                      f"\n An exmaple implementation of the target initialize function. Crucial: the value of variables must be updated according to the problem statement, the implemention above is with hypothetical values: \n```python\n{initialize_function}```\n" + 
                                      user_initialize_prompt[hash_index + 4:])
        
        f = open(log_file_instances, "w")
        f.write("model: {} \n".format(model_name))
        f.write("Astar code for this problem \n")
        f.write(code_llm + "\n\n")
        f.close() 
        
        (count_feasible, count_correct, count_optimal, count_incomplete, 
        count_killed, count_not_executed, dict_llm_sol, dict_llm_compute_t, infeasible_ids,
        total_number_calls) = get_final_solutions(problems, model_name, log_file_instances, problem_action_type,
                                                problem_type, python_dir_instances, initialize_prompt_appneded,
                                                system_initialize_prompt, code_llm, max_tokens_initialize, 
                                                print_stats, openai_key,llama_model,tokenizer, execution_time_limit)
        if dict_llm_compute_t:
            llm_avg_compute_t = sum(value for value in dict_llm_compute_t.values()) / len(dict_llm_compute_t)
        else:
            llm_avg_compute_t = None
    
        final_record_instances(log_file_instances, count_feasible, count_correct, 
                    count_optimal, count_incomplete, count_killed, 
                    count_not_executed, dict_llm_sol, dict_llm_compute_t,
                    infeasible_ids, total_number_calls, num_problems, llm_avg_compute_t)
    
    
    #did not produce an excutable code after repeat_max tries
    else:
        f = open(log_file_Astar, "a")
        f.write("\nExcessed the max repeat limit to get code that is excutable and produces a solution with correct format \n")
        f.write("Repeat_max was set to {}".format(repeat_max))
        f.close()
    

def main():
    parser = argparse.ArgumentParser(description="Evaluates a LLM on SearchBench problems using using MSMT A* prompting strategy.")

    parser.add_argument(
        '--model_name', 
        choices=['gpt4', 'gpt3.5', 'code_llama'], 
        default='gpt4', 
        help="The LLM to evaluate on SearchBench. Options: 'gpt4', 'gpt3.5 (Turbo)', 'code_llama (Phind_34B)'."
    )

    parser.add_argument(
        '--execution_time_limit', 
        type=int, 
        default=3200, 
        help="Maximum time allowed for the LLM generated code to finish executing, in seconds."
    )

    parser.add_argument(
        '--problem_types', 
        nargs='+', 
        choices=["8_puzzle", "8_puzzle_words", "coin_exchange", "water_jug", "color_sorting", "restricted_sorting", "magic_square", "consecutive_grid", "traffic", "city_directed_graph", "trampoline_matrix", "All"], 
        default="All",
        help="List of problem types in SearchBench to evaluate the model on. Use 'All' to evaluate on all problems in the dataset."
    )

    parser.add_argument(
        '--print_stats', 
        type=bool, 
        default=True,
        help="Flag to print the result of inference on each problem immediately after running the LLM generated code."
    )

    parser.add_argument(
        '--path_to_searchbench', 
        type=str, 
        default="SearchBench.jsonl", 
        help="Path to the JSONL file containing all of the problem instances. Default is 'SearchBench.jsonl'."
    )

    parser.add_argument(
        '--openai_key', 
        type=str, 
        help="Secret key for OpenAI API to run inference on GPT4 and GPT3.5. Pass an empty string if using Code Llama."
    )

    args = parser.parse_args()
    
    # List of all eligible problem types
    all_problem_types = ["8_puzzle", "8_puzzle_words", "coin_exchange",
                         "water_jug", "color_sorting", "restricted_sorting",
                         "magic_square", "consecutive_grid", "traffic", 
                         "city_directed_graph", "trampoline_matrix"]

    # If 'All' is in the problem_types, set it to all_problem_types
    if 'All' in args.problem_types:
        args.problem_types = all_problem_types
        
    prompting_method = "MSMT_A*"  
    max_tokens_astar = 1600
    max_tokens_initialize = 800
    repeat_max = 100
    max_temp = 0.6
    
    problem_types_action_type = {"8_puzzle": int, "8_puzzle_words":str,
                                "coin_exchange": int, "water_jug": tuple, 
                                "color_sorting": tuple, "restricted_sorting":tuple,
                                "magic_square": tuple, "consecutive_grid": tuple,
                                "traffic":tuple, "city_directed_graph":tuple, "trampoline_matrix":tuple}
    
    llama_model = None
    tokenizer = None
    if "llama" in args.model_name:    
        model_id = "Phind/Phind-CodeLlama-34B-v2"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        
        llama_model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )
        
        tokenizer.padding_side = "left"
        tokenizer.pad_token = tokenizer.eos_token
        llama_model.config.pad_token_id = llama_model.config.eos_token_id
        
    #setting directories and files to save results
    dir_name = f"results_{datetime.now().strftime('%Y')[2:]}-{datetime.now().strftime('%m-%d-%H-%M')}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name) 
    
    for problem_type in args.problem_types:
        problems = dataset.get_problem_types(False, [problem_type], 
                                             args.path_to_searchbench)
        problem_category = problems[0]["problem_category"]
        
        #1 -> implementation for 8_puzzle in puzzles category
        #2 -> implementation for color_sorting in the sorting category 
        #3 -> implementation for water_jug in the subset_sum category 
        #4 -> implementation for traffic in the pathfinding category 
        #5 -> implementation for magic_square in the underdetermined system category
        if problem_category == "puzzle":
            prompt_ids_Astar = [2, 3, 4, 5]
            prompt_ids_initalize = [2, 3, 4, 5]
        elif problem_category == "sorting":
            prompt_ids_Astar = [1, 3, 4, 5]
            prompt_ids_initalize = [1, 3, 4, 5]
        elif problem_category == "subset_sum":
            prompt_ids_Astar = [1, 2, 4, 5]
            prompt_ids_initalize = [1, 2, 4, 5]
        elif problem_category == "pathfinding":
            prompt_ids_Astar = [1, 2, 3, 5]
            # Encoding the intiilaize function for the pathfinding problems 
            # requires rewriting an nxn matrix which consumes a lot of tokens
            # in order to save more tokens for the genration, we provide 3 prompts for the 2nd stage of MSMT
            prompt_ids_initalize = [2, 3, 5]
        elif problem_category == "underdetermined_system":
            prompt_ids_Astar = [1, 2, 3, 4]
            prompt_ids_initalize = [1, 2, 3, 4]

        system_astar_prompt = Astar_intro_prompt
        user_astar_prompt = ''.join([Astar_problmes[id] for id in prompt_ids_Astar])
        user_astar_prompt += Astar_inst_prompt
        
        system_initialize_prompt = Initialize_intro_prompt
        user_initialize_prompt = ''.join(Initialize_problems[id] for id in prompt_ids_initalize)
        user_initialize_prompt += Initialize_inst_prompt
        
        num_problems_to_iterate = min(20, len(problems))
        
        problem_action_type = problem_types_action_type[problem_type]

        run_experiment(prompting_method, args.model_name, problem_type,
                   problems, args.execution_time_limit, system_astar_prompt,
                   user_astar_prompt, system_initialize_prompt, 
                   user_initialize_prompt, max_tokens_astar, 
                   max_tokens_initialize, problem_action_type, 
                   repeat_max, max_temp,num_problems_to_iterate, args.print_stats,
                   args.openai_key,llama_model, tokenizer, dir_name)


if __name__ == "__main__":
    main()  
