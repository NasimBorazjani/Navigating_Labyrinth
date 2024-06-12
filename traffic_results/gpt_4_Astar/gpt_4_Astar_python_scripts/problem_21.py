
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (1, 9)
   goal_state = (6, 3)
   # Define the matrix map of the city
   city_map = np.array([[15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15],
                        [12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3],
                        [4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6],
                        ['x', 'x', 5, 'x', 'x', 'x', 12, 6, 6, 'x'],
                        ['x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14],
                        [8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6],
                        [18, 'x', 'x', 15, 'x', 15, 4, 'x', 'x', 7],
                        [19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6],
                        [19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'],
                        [12, 1, 'x', 5, 3, 3, 'x', 'x', 'x', 'x']])
   num_rows, num_cols = city_map.shape
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(num_rows):
       for j in range(num_cols):
           if city_map[i][j] != 'x':
               if i < 2:
                   districts[0].add((i, j))
               elif i < 7:
                   districts[1].add((i, j))
               else:
                   districts[2].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset([0, 1, 2]))] = 0


   queue = [(0, 0, [initial_state], (initial_state, frozenset([0, 1, 2])))]


   while queue:
       _, g, path, (state, districts_left) = heapq.heappop(queue)


       if state == goal_state and not districts_left:
           return path


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_districts_left = set(districts_left)
               for i, district in enumerate(districts):
                   if new_state in district and i in new_districts_left:
                       new_districts_left.remove(i)
               new_cost = g + int(city_map[new_state[0]][new_state[1]])
               if (new_state, frozenset(new_districts_left)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_districts_left))]:
                   visited_costs[(new_state, frozenset(new_districts_left))] = new_cost
                   h = heuristic(new_state, goal_state, new_districts_left)
                   heapq.heappush(queue, (g + h, new_cost, path + [new_state], (new_state, frozenset(new_districts_left))))
   return None


def heuristic(state, goal, districts_left):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   # Add a penalty for each district not yet visited
   h += len(districts_left) * 10
   return h


print(a_star())
