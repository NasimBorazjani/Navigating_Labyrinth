
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 10)
   goal_state = (3, 0)
   # Define the map of the city
   city_map = np.array([[19, 7, 11, 'x', 3, 18, 8, 'x', 'x', 'x', 'x'],
                        [12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19],
                        [11, 10, 10, 18, 15, 'x', 12, 'x', 4, 17, 10],
                        [4, 3, 3, 7, 'x', 19, 'x', 'x', 'x', 12, 9],
                        ['x', 'x', 6, 19, 'x', 4, 14, 'x', 9, 4, 15],
                        [4, 7, 6, 5, 8, 'x', 15, 3, 'x', 16, 3],
                        [13, 'x', 'x', 1, 9, 1, 9, 'x', 'x', 'x', 'x'],
                        [2, 13, 5, 9, 5, 'x', 6, 'x', 18, 'x', 3],
                        [19, 'x', 2, 9, 4, 13, 'x', 'x', 'x', 16, 6],
                        ['x', 'x', 'x', 12, 'x', 7, 9, 3, 9, 8, 1],
                        ['x', 10, 'x', 12, 3, 6, 'x', 4, 12, 4, 'x']])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               if i < 4:
                   districts[0].add((i, j))
               elif i < 5:
                   districts[1].add((i, j))
               else:
                   districts[2].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset([0, 1, 2]))] = 0


   queue = [(0, 0, [], initial_state, frozenset([0, 1, 2]))]


   while queue:
       _, g, actions, state, districts_left = heapq.heappop(queue)


       if state == goal_state and not districts_left:
           return actions


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_districts_left = districts_left.copy()
               for i, district in enumerate(districts):
                   if new_state in district and i in new_districts_left:
                       new_districts_left.remove(i)
               new_cost = g + city_map[new_row][new_col]


               if (new_state, new_districts_left) not in visited_costs or new_cost < visited_costs[(new_state, new_districts_left)]:
                   visited_costs[(new_state, new_districts_left)] = new_cost
                   h = heuristic(new_state, goal_state, new_districts_left, districts)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_districts_left))
   return None


def heuristic(state, goal, districts_left, districts):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state, plus the sum of the minimum Manhattan distances from the current state to the nearest workshop in each district that has not been visited yet
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that Ben can move directly to the goal state or the nearest workshop in each district that has not been visited yet, without considering the workshops in the path
   # The heuristic is consistent because the cost of moving from one state to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state or the nearest workshop in each district that has not been visited yet
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   for district_left in districts_left:
       h += min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in districts[district_left])
   return h


print(a_star())
