
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 0)
   goal_state = (4, 8)
   # Define the map of the city as a 2d numpy array
   city_map = np.array([[np.inf, 15, np.inf, 18, 8, 6, 11, np.inf, 7],
                        [9, 10, 18, 9, 2, 16, 9, 8, np.inf],
                        [14, np.inf, np.inf, 10, 18, np.inf, 13, 12, 14],
                        [11, 18, 4, 11, 14, 2, 20, np.inf, 15],
                        [12, np.inf, np.inf, 8, 10, np.inf, np.inf, 10, 11],
                        [5, 19, 20, 15, 11, np.inf, 14, np.inf, 18],
                        [np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf, 9, np.inf],
                        [np.inf, np.inf, 18, np.inf, np.inf, 4, np.inf, 17, 13],
                        [np.inf, 7, 17, np.inf, np.inf, np.inf, np.inf, 7, 19]])
   num_rows, num_cols = city_map.shape
   # Define the districts of the city
   districts = [set(range(0, 3)), set(range(3, 5)), set(range(5, 9))]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, set())]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and len(visited_districts) == len(districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the workshop to move to is a valid coordinate within the bounds of the city map and the workshop is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != np.inf:
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + city_map[new_row][new_col]
               # Update the set of visited districts
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if new_row in district:
                       new_visited_districts.add(i)


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal position
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
