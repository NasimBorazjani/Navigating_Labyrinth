
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = ('S', frozenset(['P', 'G']))
   goal_state = ('S', frozenset())
  
   # Encoding other variables given in the problem statement
   cities = ['C', 'V', 'A', 'G', 'Y', 'P', 'Z', 'S', 'J', 'I']
   adjacency_matrix = [[0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                       [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to get to each state in a list; no cities visited to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return path


       # Generate all valid actions from the current state, which includes moving to any of the cities directly connected to the current city
       # Generate the indices of the cities directly connected to the current city
       current_city_ind = cities.index(state[0])
       for next_city_ind, connected in enumerate(adjacency_matrix[current_city_ind]):
           if connected:
               next_city = cities[next_city_ind]
               # Check if the move is valid, ie if the city to be visited is a valid city within the bounds of the map
               # The city must be in the set of cities to be visited or it must be one of the destination cities and we have not visited it twice yet
               if next_city in state[1] or (next_city in ['P', 'G'] and path.count(next_city) < 2):
                   # The actions is valid, generate the new state
                   new_state = (next_city, state[1] - {next_city} if next_city in state[1] else state[1])
                   # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state 
                   new_cost = g + 1
              
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, path + [next_city], new_state))
                  
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the number of cities left to visit
   # The heuristic relaxes the constraint that we can only move to cities directly connected to the current city and presumes we can move to any of the cities left to visit directly from the current city
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of cities left to visit, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the number of cities left to visit would be 0 in the goal state.
   return len(state[1])


print(a_star())
