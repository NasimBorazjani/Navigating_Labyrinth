
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 0)
   goal_state = (3, 9)
   # Define the map of the city
   city_map = [['x', 16, 15, 14, 2, 12, 3, 'x', 7, 7],
               [11, 'x', 'x', 'x', 4, 10, 5, 'x', 'x', 'x'],
               [12, 'x', 3, 'x', 'x', 19, 'x', 13, 'x', 'x'],
               [16, 15, 13, 'x', 12, 'x', 'x', 1, 'x', 7],
               [2, 6, 'x', 5, 'x', 14, 7, 'x', 8, 18],
               [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
               [11, 1, 10, 11, 'x', 'x', 19, 6, 2, 18],
               [7, 'x', 10, 15, 'x', 'x', 'x', 'x', 18, 17],
               ['x', 6, 'x', 'x', 'x', 5, 'x', 7, 12, 20],
               ['x', 'x', 2, 15, 'x', 17, 'x', 'x', 10, 11]]
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               if i < 4:
                   districts[0].add((i, j))
               elif i < 6:
                   districts[1].add((i, j))
               else:
                   districts[2].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset([0, 1, 2]))] = 0


   queue = [(0, 0, [initial_state], initial_state, frozenset([0, 1, 2]))]


   while queue:
       _, g, path, state, districts_left = heapq.heappop(queue)


       if state == goal_state and not districts_left:
           return path


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_districts_left = districts_left.copy()
               for i, district in enumerate(districts):
                   if new_state in district:
                       new_districts_left.discard(i)
               new_cost = g + city_map[new_row][new_col]


               if (new_state, new_districts_left) not in visited_costs or new_cost < visited_costs[(new_state, new_districts_left)]:
                   visited_costs[(new_state, new_districts_left)] = new_cost
                   h = heuristic(new_state, goal_state, new_districts_left, districts)
                   heapq.heappush(queue, (g + h, new_cost, path + [new_state], new_state, new_districts_left))
   return None


def heuristic(state, goal, districts_left, districts):
   # The heuristic function can be the Manhattan distance from the current state to the goal state, plus the sum of the minimum Manhattan distances from the current state to the nearest workshop in each district that has not been visited yet
   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that the car can move in a straight line to the goal state and the nearest workshops in the districts, which is not possible if there are obstacles in the way
   # The heuristic is consistent because the cost of moving from one state to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance if the car moves toward the goal state or the nearest workshop in a district, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0 and all districts have been visited
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   for district_left in districts_left:
       h += min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in districts[district_left])
   return h


print(a_star())
