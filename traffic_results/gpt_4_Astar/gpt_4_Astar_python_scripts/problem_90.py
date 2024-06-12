
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (6, 0)
   goal_state = (4, 13)
   # Define the map of the city
   city_map = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '15', 'x', 'x', '19', '1'],
               ['x', '12', 'x', '19', 'x', 'x', '13', 'x', '14', '13', '8', 'x', '1', '6'],
               ['x', '17', 'x', '19', '5', '4', 'x', 'x', '12', 'x', 'x', '10', '14', 'x'],
               ['x', '18', 'x', '1', 'x', '14', 'x', 'x', '12', 'x', '11', '4', '4', '7'],
               ['2', '15', 'x', 'x', 'x', '14', 'x', '16', '5', '2', '4', 'x', '10', '2'],
               ['8', '2', '15', '18', '19', '6', '13', '7', '6', 'x', 'x', 'x', '1', 'x'],
               ['5', 'x', '11', '2', '8', '8', 'x', '1', '10', '8', '13', '7', '12', '18'],
               ['x', '18', '8', '19', 'x', 'x', '16', '11', '2', 'x', '9', 'x', '9', '8'],
               ['4', '10', 'x', '12', '12', '13', '13', '2', '13', 'x', 'x', 'x', '8', '18'],
               ['1', 'x', 'x', 'x', '5', '12', '18', '16', '5', '17', 'x', '16', '11', '18'],
               ['19', 'x', 'x', 'x', 'x', '1', 'x', 'x', 'x', 'x', '10', '19', 'x', 'x'],
               ['x', '14', 'x', 'x', 'x', '15', '16', '9', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['6', 'x', '16', '18', '6', 'x', '18', 'x', '5', 'x', 'x', 'x', '6', '1'],
               ['x', 'x', 'x', '17', '4', 'x', '6', 'x', 'x', '19', '17', 'x', '19', '15']]
   # Define the districts
   districts = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3]
   # Define the directions
   directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       if state == goal_state and len(visited_districts) == 3:
           return actions


       for direction in directions:
           new_state = (state[0] + direction[0], state[1] + direction[1])
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and
               city_map[new_state[0]][new_state[1]] != 'x'):
               new_visited_districts = visited_districts | {districts[new_state[0]]}
               new_cost = g + int(city_map[new_state[0]][new_state[1]])
               if (new_state, new_visited_districts) not in visited_costs or new_cost < visited_costs[(new_state, new_visited_districts)]:
                   visited_costs[(new_state, new_visited_districts)] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the shortest path between two points in a grid with 4 possible directions of movement is the Manhattan distance
   # The heuristic is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the state is moved toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
