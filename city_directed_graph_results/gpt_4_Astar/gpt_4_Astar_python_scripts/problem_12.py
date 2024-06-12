
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = ('B', ('B',), ('L', 'V'), 0)
   goal_state = ('B', ('B', 'L', 'V', 'L', 'V'), (), 0)
  
   # Encoding the adjacency matrix as a dictionary of lists
   adjacency_matrix = {'S': ['T', 'B', 'P'],
                       'T': ['V'],
                       'R': ['S', 'T', 'P', 'N'],
                       'A': ['S', 'R', 'V', 'N'],
                       'L': ['A', 'V', 'I', 'N'],
                       'B': ['S', 'I'],
                       'V': ['S', 'T', 'R', 'A', 'B', 'P', 'N'],
                       'I': ['L'],
                       'P': ['I'],
                       'N': ['L', 'B']}
  
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
  
       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions
  
       # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
       current_city, visited_cities, remaining_cities, num_visits = state
       for next_city in adjacency_matrix[current_city]:
           # Check if the new state would be valid, ie the next city must not have been visited before, unless it is one of the destination cities and it has not been visited twice already
           if (next_city not in visited_cities or (next_city in remaining_cities and visited_cities.count(next_city) < 2)):
               # Generate the new state
               new_visited_cities = visited_cities + (next_city,)
               new_remaining_cities = tuple(city for city in remaining_cities if city != next_city or new_visited_cities.count(city) < 2)
               new_num_visits = num_visits + 1
               new_state = (next_city, new_visited_cities, new_remaining_cities, new_num_visits)
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the number of remaining cities to be visited
   # The heuristic relaxes the constraint that we can only move to a city directly connected to the current city and presumes we can move to any of the remaining cities directly from the current city
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining cities, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the number of remaining cities would be 0 in the goal state.
   return len(state[2])


print(a_star())
