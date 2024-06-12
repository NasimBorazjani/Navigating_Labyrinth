
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (9, 1)
   goal_state = (7, 14)
   # Define the map of the city
   city_map = np.array([[17, 8, 'x', 3, 'x', 13, 'x', 'x', 14, 11, 'x', 'x', 'x', 'x', 'x'],
                        ['x', 'x', 'x', 7, 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 16, 'x', 13],
                        ['x', 'x', 2, 'x', 'x', 12, 10, 'x', 'x', 'x', 2, 'x', 'x', 5, 17],
                        [4, 3, 'x', 14, 'x', 'x', 16, 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x'],
                        [9, 'x', 18, 11, 19, 5, 'x', 'x', 'x', 'x', 'x', 'x', 3, 'x', 'x'],
                        ['x', 14, 'x', 4, 14, 12, 1, 'x', 13, 7, 10, 8, 8, 6, 9],
                        [7, 10, 'x', 18, 15, 8, 13, 14, 15, 'x', 'x', 'x', 13, 'x', 17],
                        [17, 7, 19, 15, 20, 19, 'x', 15, 13, 'x', 9, 'x', 11, 'x', 1],
                        ['x', 9, 6, 17, 14, 'x', 16, 'x', 19, 11, 'x', 14, 11, 'x', 'x'],
                        ['x', 18, 8, 2, 14, 2, 4, 'x', 4, 4, 4, 'x', 'x', 8, 19],
                        ['x', 'x', 5, 'x', 'x', 'x', 1, 5, 'x', 11, 'x', 'x', 1, 14, 'x'],
                        ['x', 'x', 'x', 'x', 5, 'x', 10, 'x', 'x', 'x', 'x', 10, 18, 'x', 19],
                        ['x', 'x', 2, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 6, 16],
                        ['x', 12, 1, 12, 'x', 'x', 15, 7, 18, 15, 13, 19, 'x', 2, 'x'],
                        ['x', 13, 8, 19, 5, 1, 'x', 13, 'x', 'x', 'x', 17, 'x', 3, 'x']])
   num_rows = city_map.shape[0]
   num_cols = city_map.shape[1]
   # Define the districts of the city
   districts = [range(0, 6), range(6, 9), range(9, 15)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset([initial_state]))] = 0


   queue = [(0, 0, [], (initial_state, frozenset([initial_state])))]


   while queue:
       _, g, actions, (state, visited) = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where Ben has reached his destination and visited at least 1 workshop in each district
       if state == goal_state and all(any(visited.intersection(set([(i, j) for j in range(num_cols)]))) for i in districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the new workshop is a valid coordinate within the bounds of the city and the workshop is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               new_visited = visited.union(set([new_state]))
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + int(city_map[new_state[0]][new_state[1]])


               if (new_state, new_visited) not in visited_costs or new_cost < visited_costs[(new_state, new_visited)]:
                   visited_costs[(new_state, new_visited)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], (new_state, new_visited)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current workshop to the goal workshop
   # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district and presumes Ben can move directly to the goal workshop
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal workshop, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
