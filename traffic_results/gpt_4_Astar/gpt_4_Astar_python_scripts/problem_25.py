
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (2, 9)
   goal_state = (5, 2)
   # Define the map of the city
   city_map = [['x', 'x', 6, 'x', 'x', 'x', 'x', 15, 'x', 'x'],
               ['x', 17, 13, 13, 'x', 12, 'x', 3, 10, 2],
               ['x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2],
               ['x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'],
               ['x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'],
               [3, 'x', 3, 17, 8, 'x', 1, 'x', 16, 'x'],
               ['x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4],
               ['x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'],
               ['x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'],
               [1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5]]
   # Define the districts
   districts = [0, 0, 0, 1, 1, 2, 2, 2, 2, 2]
   # Define the number of rows and columns in the city map
   num_rows = len(city_map)
   num_cols = len(city_map[0])


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       if state == goal_state and len(visited_districts) == 3:
           return actions


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_visited_districts = visited_districts | {districts[new_row]}
               new_cost = g + city_map[new_row][new_col]
               if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                   visited_costs[(new_state, new_visited_districts)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path from one point to another in a grid is the Manhattan distance
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the move is toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
