
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 8)
   goal_state = (8, 0)
   # Define the map of the city
   city_map = [['x', 14, 15, 10, 'x', 14, 'x', 'x', 18, 6, 'x', 'x', 4],
               [6, 'x', 'x', 'x', 1, 'x', 15, 'x', 'x', 2, 'x', 17, 'x'],
               ['x', 4, 'x', 17, 3, 14, 4, 2, 'x', 3, 'x', 11, 'x'],
               [6, 6, 'x', 19, 'x', 13, 'x', 11, 13, 6, 3, 'x', 'x'],
               [3, 10, 11, 'x', 'x', 4, 4, 1, 19, 'x', 'x', 'x', 17],
               [8, 'x', 'x', 8, 11, 18, 17, 19, 18, 'x', 1, 1, 'x'],
               [14, 14, 1, 19, 6, 'x', 19, 19, 18, 9, 'x', 12, 18],
               [17, 6, 8, 'x', 1, 14, 19, 13, 'x', 'x', 9, 'x', 3],
               [16, 4, 'x', 'x', 'x', 9, 5, 'x', 'x', 'x', 18, 'x', 'x'],
               ['x', 'x', 10, 'x', 18, 'x', 1, 'x', 'x', 12, 9, 8, 3],
               ['x', 13, 17, 'x', 'x', 'x', 5, 8, 1, 'x', 1, 10, 'x'],
               [10, 11, 'x', 12, 'x', 6, 11, 'x', 9, 9, 15, 'x', 10],
               [5, 15, 1, 'x', 8, 5, 'x', 6, 'x', 9, 18, 'x', 'x']]
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               districts[i // 4].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset([initial_state]))] = 0


   queue = [(0, 0, [initial_state], initial_state, frozenset([initial_state]))]


   while queue:
       _, g, path, state, visited = heapq.heappop(queue)


       if state == goal_state and all(district & visited for district in districts):
           return path


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_visited = visited | {new_state}
               new_cost = g + city_map[new_row][new_col]
               if (new_state, new_visited) not in visited_costs or new_cost < visited_costs[(new_state, new_visited)]:
                   visited_costs[(new_state, new_visited)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, path + [new_state], new_state, new_visited))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that the car can only move to a neighboring crossroad and presumes the car can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
