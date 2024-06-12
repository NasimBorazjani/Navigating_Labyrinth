
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 1)
   goal_state = (5, 8)
   # Define the map of the city
   city_map = np.array([[4, 13, 'x', 9, 'x', 'x', 'x', 'x', 'x'],
                        [1, 11, 'x', 16, 5, 7, 12, 16, 'x'],
                        [12, 11, 'x', 14, 'x', 'x', 12, 'x', 3],
                        [9, 11, 'x', 9, 10, 'x', 8, 'x', 'x'],
                        [20, 2, 'x', 1, 16, 12, 18, 17, 10],
                        [10, 13, 4, 15, 13, 2, 20, 3, 15],
                        ['x', 6, 13, 1, 8, 20, 14, 11, 3],
                        [14, 'x', 9, 'x', 'x', 13, 19, 10, 'x'],
                        [12, 'x', 18, 1, 'x', 'x', 9, 'x', 'x']])
   num_rows, num_cols = city_map.shape
   # Define the districts of the city
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               if i < 3:
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
   # The heuristic function can be the Manhattan distance from the current state to the goal state, plus the sum of the minimum Manhattan distances from the current state to the nearest workshop in each district that has not been visited yet
   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that the car can move directly to the goal state or the nearest workshop in each district, without considering the constraints of the city map or the order of visiting the districts
   # The heuristic is consistent because the cost of moving from one state to another is always equal to or greater than the Manhattan distance between the two states, and the heuristic cost of the goal state is 0
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   for district in districts_left:
       h += min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in districts[district])
   return h


print(a_star())
