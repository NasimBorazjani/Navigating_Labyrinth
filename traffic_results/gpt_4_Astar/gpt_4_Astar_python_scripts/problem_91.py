
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (5, 2)
   goal_state = (8, 14)
   # Define the map of the city
   city_map = np.array([['x', 'x', '12', 'x', '18', '3', '2', '15', '6', '11', '13', 'x', '7', '17', 'x'],
                        ['13', 'x', '20', '13', '5', '2', 'x', 'x', '10', '12', '19', '19', '16', 'x', '17'],
                        ['12', '12', '7', 'x', 'x', 'x', '9', 'x', 'x', '10', '10', '18', '4', 'x', 'x'],
                        ['x', '14', '3', '13', '9', '2', '19', '19', 'x', 'x', 'x', '4', 'x', '2', '15'],
                        ['x', '14', '2', 'x', '3', 'x', '10', '11', 'x', '4', 'x', '12', '4', 'x', 'x'],
                        ['x', '9', '7', '16', 'x', 'x', '19', '17', '17', '14', '14', '12', '14', '19', '12'],
                        ['2', 'x', 'x', '7', '15', 'x', 'x', '13', 'x', '8', '1', '1', 'x', '14', '19'],
                        ['16', 'x', '14', 'x', 'x', '6', 'x', 'x', '16', 'x', 'x', '9', '10', '18', '4'],
                        ['3', 'x', 'x', '3', 'x', 'x', 'x', 'x', '9', '8', 'x', '9', '14', 'x', '14'],
                        ['x', 'x', 'x', '4', '19', 'x', '4', '15', 'x', 'x', 'x', '17', 'x', 'x', 'x'],
                        ['16', '17', 'x', 'x', '13', 'x', '18', '5', 'x', '14', 'x', 'x', 'x', 'x', 'x'],
                        ['2', 'x', '17', 'x', 'x', 'x', 'x', 'x', 'x', '12', '3', '8', 'x', '2', '9'],
                        ['x', 'x', '14', '7', '11', 'x', 'x', '10', '9', '3', '7', '16', 'x', '7', '1'],
                        ['x', '12', '14', '1', 'x', 'x', '3', '12', 'x', '7', 'x', 'x', '8', 'x', 'x'],
                        ['x', '2', 'x', '15', '2', 'x', '14', '16', '13', '19', '16', '1', '11', 'x', 'x']])
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts of the city
   districts = [range(0, 6), range(6, 8), range(8, 15)]
   # Define the directions in which Ben can move
   directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, [False, False, False])]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
       for direction in directions:
           new_state = (state[0] + direction[0], state[1] + direction[1])
           # Check if the new state is valid, ie within the bounds of the city and not a closed workshop
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the sum of the travel times, as the task is to minimize the total travel time
               new_cost = g + int(city_map[new_state[0]][new_state[1]])
               # Check if the new state is in a new district
               new_visited_districts = visited_districts[:]
               for i, district in enumerate(districts):
                   if new_state[0] in district:
                       new_visited_districts[i] = True
                       break


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Ben can only move to a neighboring workshop and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
