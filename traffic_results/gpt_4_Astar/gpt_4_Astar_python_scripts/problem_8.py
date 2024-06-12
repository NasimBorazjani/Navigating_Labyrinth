
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (2, 8)
   goal_state = (6, 3)
   # Define the map of the city
   city_map = [['x', 'x', 'x', 'x', '13', 'x', 'x', '3', '8'],
               ['x', '18', '19', '19', '2', '9', 'x', 'x', 'x'],
               ['15', 'x', '6', 'x', 'x', 'x', '13', '13', '4'],
               ['7', 'x', '4', '10', 'x', '11', '10', '17', 'x'],
               ['2', '7', 'x', 'x', '8', '16', '4', '1', '4'],
               ['x', 'x', 'x', '5', '16', '15', 'x', '17', '10'],
               ['x', 'x', 'x', '5', '14', '9', '3', '15', 'x'],
               ['x', '6', '4', 'x', 'x', 'x', '18', 'x', 'x'],
               ['17', 'x', '19', 'x', '1', '4', '8', 'x', '8']]
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts of the city
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               districts[i // 3].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset({0}))] = 0


   queue = [(0, 0, [], (initial_state, frozenset({0})))]


   while queue:
       _, g, actions, (state, visited_districts) = heapq.heappop(queue)


       if state == goal_state and visited_districts == frozenset({0, 1, 2}):
           return actions


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_visited_districts = visited_districts | {new_row // 3}
               new_cost = g + int(city_map[new_row][new_col])
               if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                   visited_costs[(new_state, new_visited_districts)] = new_cost
                   h = heuristic(new_state, goal_state, districts, new_visited_districts)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, new_visited_districts)))
   return None


def heuristic(state, goal, districts, visited_districts):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # Plus the sum of the minimum Manhattan distances from the current state to the nearest unvisited district
   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as the actual cost can never be less than the Manhattan distance
   # It is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the state is moved toward the goal state or an unvisited district
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   for district in districts:
       if district not in visited_districts:
           h += min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in district)
   return h


print(a_star())
