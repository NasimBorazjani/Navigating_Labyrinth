
import heapq
from collections import defaultdict


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = 'Q'
   goal_state = ('K', 'Y')
   # Define the adjacency matrix as a dictionary of lists, where the keys are the cities and the values are the cities directly connected to the key city
   adjacency_matrix = {'G': ['R', 'H'], 'J': ['G', 'Y', 'Q', 'K'], 'Y': ['G', 'R', 'F', 'N'], 'Q': ['F', 'H'], 'C': ['G', 'J', 'K'], 'D': ['G', 'Y', 'Q', 'F'], 'R': ['J', 'Y', 'Q', 'D', 'H'], 'F': ['D', 'R'], 'K': ['G', 'R', 'F', 'H', 'N'], 'H': ['J', 'Y', 'Q', 'C'], 'N': ['J', 'Y', 'C', 'D', 'F']}
   # Define the number of times each city must be visited
   visits = defaultdict(int)
   visits['K'] = 2
   visits['Y'] = 2


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(visits[city] == visited.count(city) for city in goal_state):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
       for city in adjacency_matrix[state]:
           # Check if the new state would be valid, ie the city must not have been visited more than the required number of times
           if visited.count(city) < visits[city]:
               # Generate the new state
               new_state = city
               new_visited = visited | {new_state}
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state, new_visited) not in visited_costs or new_cost < visited_costs[(new_state, new_visited)]:
                   visited_costs[(new_state, new_visited)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, visits, new_visited), new_cost, actions + [new_state], new_state, new_visited))
   return None


def heuristic(state, goal_state, visits, visited):
   # An admissible and consistent heuristic is the number of cities in the goal state that have not been visited the required number of times
   # The heuristic relaxes the constraint that we can only move to cities directly connected to the current city and presumes we can move to any of the goal cities directly from the current city
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the heuristic cost, if the city is a goal city and has not been visited the required number of times, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all the goal cities have been visited the required number of times in the goal state.
   h = 0
   for city in goal_state:
       if visited.count(city) < visits[city]:
           h += 1
   return h


print(a_star())
