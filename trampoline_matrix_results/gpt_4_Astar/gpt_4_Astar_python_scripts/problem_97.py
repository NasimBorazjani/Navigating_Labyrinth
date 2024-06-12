
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the puzzle, represented as 2d tuples
   initial_state = ((4, 14), 0)
   goal_state = (11, 0)
   num_rows = 15
   num_cols = 15
   # Define the grid of the trampoline park
   grid = np.array([[1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
                    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]])
   # Define the possible moves from a trampoline
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[0] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes moving to any of the 8 neighboring trampolines
       for move in moves:
           new_state = (state[0][0] + move[0], state[0][1] + move[1])
           # Check if the move is valid, ie if the coordinate of the new trampoline is a valid coordinate within the bounds of the grid and the trampoline is not broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               grid[new_state[0]][new_state[1]] == 0):
               # The actions is valid, generate the new state
               # The new state must also include the number of diagonal moves made so far, as we have a constraint on the number of diagonal moves
               diagonal_moves = state[1]
               if move in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                   diagonal_moves += 1
               new_state = (new_state, diagonal_moves)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state not in visited_costs or new_cost < visited_costs[new_state]) and diagonal_moves <= 5:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state[0], goal_state), new_cost, actions + [new_state[0]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex can only move to neighboring trampolines and presumes Alex can move directly to the goal position
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
