
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 9)
   goal_state = (6, 1)
   # Define the map of the city
   city_map = np.array([['x', 'x', 'x', '4', '6', 'x', '9', '15', '11', '2'],
                        ['19', 'x', '14', '3', '10', '18', 'x', 'x', 'x', '1'],
                        ['x', '9', 'x', '11', '7', '14', 'x', 'x', '16', '18'],
                        ['x', '5', '4', '5', '2', '4', '7', '5', '19', '14'],
                        ['x', '3', '20', 'x', '5', '16', 'x', 'x', '1', '9'],
                        ['x', '3', '15', '9', '4', 'x', 'x', 'x', 'x', '4'],
                        ['11', '18', '19', '8', '17', '9', 'x', '10', '10', '19'],
                        ['x', 'x', 'x', '17', '7', 'x', 'x', '7', '12', '8'],
                        ['x', 'x', '11', '19', 'x', '13', '10', '13', 'x', 'x'],
                        ['18', 'x', 'x', 'x', '6', '10', '7', 'x', '8', 'x']])
   num_rows = 10
   num_cols = 10
   # Define the districts of the city
   districts = [range(0, 4), range(4, 6), range(6, 10)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, [False, False, False])]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new cell must be within the bounds of the city map and not be a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + int(city_map[new_row][new_col])
               # Update the visited districts
               new_visited_districts = visited_districts[:]
               for i, district in enumerate(districts):
                   if new_row in district:
                       new_visited_districts[i] = True


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that the car can only move to a neighboring cell and presumes the car can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if the car is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the car from its goal position would be 0 in the goal state.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
