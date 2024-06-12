
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 8)
   goal_state = (3, 0)
   # Define the map of the city
   city_map = [['x', 'x', 'x', 'x', 'x', '8', 'x', '15', '18', '10'],
               ['4', '5', '10', '6', '20', '2', '12', 'x', 'x', 'x'],
               ['19', '6', '19', '7', '6', '2', 'x', '15', 'x', '14'],
               ['16', '17', 'x', '2', '3', '7', '4', 'x', '18', '6'],
               ['x', '2', '1', '19', '7', '10', '18', '5', '3', '19'],
               ['8', '5', 'x', '1', 'x', '10', '17', 'x', '13', '5'],
               ['18', '1', '3', '4', 'x', 'x', '8', 'x', '5', 'x'],
               ['15', 'x', 'x', '13', 'x', '11', 'x', '2', 'x', 'x'],
               ['4', 'x', 'x', '4', '1', 'x', 'x', 'x', 'x', 'x'],
               ['x', '10', '8', 'x', 'x', '7', '19', 'x', 'x', 'x']]
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
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
               for i in districts_left:
                   if new_state in districts[i]:
                       new_districts_left.remove(i)
               new_cost = g + int(city_map[new_row][new_col])
               if (new_state, frozenset(new_districts_left)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_districts_left))]:
                   visited_costs[(new_state, frozenset(new_districts_left))] = new_cost
                   h = heuristic(new_state, goal_state, new_districts_left, districts)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_districts_left)))
   return None


def heuristic(state, goal, districts_left, districts):
   # The heuristic function can be the Manhattan distance from the current state to the goal state, plus the sum of the minimum Manhattan distances from the current state to the nearest workshop in each district that has not been visited yet
   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that the car can move directly to the goal state or the nearest workshop in each district, without considering the workshops that are closed or the constraint that the car can only move in 4 directions
   # The heuristic is consistent because the cost of moving from one state to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward the goal state or the nearest workshop in each district, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0 and all districts have been visited
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   for i in districts_left:
       h += min(abs(state[0] - workshop[0]) + abs(state[1] - workshop[1]) for workshop in districts[i])
   return h


print(a_star())
