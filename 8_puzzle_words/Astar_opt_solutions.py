import heapq
import math
import numpy as np
import sys

def get_goal_board(target_words, h, w):
    words = target_words[:]
    words[0] = "_" + words[0]
    board = np.zeros((h, w)).tolist()
    for i in range(h):
        for j in range(w):
            board[i][j] = words[i][j]
    board[0][0] = "_"
    return board

def a_star(board, target_words):
   # Define the initial state of the board
   goal = get_goal_board(target_words, len(board), len(board[0]))
   goal = tuple(tuple(row) for row in goal)
   num_rows =  len(board)
   num_cols = len(board[0])

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   initial_state = tuple(tuple(row) for row in board)
   visited_costs[initial_state] = 0

   # Initialize a priority queue with the initial state and cost
   queue = [(heuristic(board, goal), 0, [], board)]

   while queue:
       # Pop the state with the lowest cost from the queue
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state
       if state == goal:
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       blank_row, blank_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           swap_row, swap_col = blank_row + d_row, blank_col + d_col
           # Check if the new position is valid, ie if the swap tile is a valid tile on the board
           if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_row][blank_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[blank_row][blank_col]
               new_state = tuple(tuple(row) for row in new_state)
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   direction = ''
                   if d_row == -1 and d_col == 1:
                       direction = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       direction = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       direction = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       direction = 'down-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal), g + 1, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # The heuristic function is the sum of the digonal distances of each charactor tile from the closest tile that has the same charactor 
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
            goal_positions = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]]
            min_distance_to_goal = math.inf
            for goal_row, goal_col in goal_positions:
                if max(abs(i - goal_row), abs(j - goal_col)) <  min_distance_to_goal:
                    min_distance_to_goal = max(abs(i - goal_row), abs(j - goal_col))
            h += min_distance_to_goal
   return h


def main():
    # Read the initial state from the command line
    board = eval(sys.argv[1])
    target_words = eval(sys.argv[2])
    print(a_star(board, target_words))

if __name__ == "__main__":
    main()


"""
Reasoning:

The problem can be modeled as a graph where each node represents a state of the board, and each edge represents an action that changes the state of the board. The initial state is the state where the board is arranged as specified in the problem, and the goal state is the state where the board is arranged such that row i spells the i-th word in the list, with the blank space being in the top left corner of the goal board. The actions must follow the rule specified in the problem, where the blank space can be swapped with any of its 4 diagonal neighboring tiles.

The A* search algorithm can be used to solve this problem. The states can be represented as tuples of the characters on the tiles in the board, the actions as the direction in which the blank space is swapped.


An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of each tile from the closest tile with the same character in the goal state. A character might be present in the board multiple times, thus if we only consider the first appearance of a character when calculating the heuristic, we might end up over estimating the cost.  However, by considering the closest appearance of the character int he goal board as its manhattan distance, we are guaranteed to never overestimated the cost of reaching the goal board. The heuristic relaxes the constraints that the blank space can only be swapped with its 4 diagonal neighboring tiles and presumes we can move the tiles to their goal position by swapping them with any of the other tiles. Thus the heuristic reports a lower estimate on the cost of reaching the goal state from any given state and is admissible. The heuristic is also consistent because the estimated cost from the current state to the goal is not greater than the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving one tile to an adjacent tile is always 1, which is exactly the decrease in the Manhattan distance.

"""
