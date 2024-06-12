
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = ('E', 0, 0)
   goal_state = ('E', 2, 2)
  
   # Encoding other variables given in the problem statement
   cities = ['U', 'W', 'A', 'J', 'K', 'H', 'E', 'X', 'R', 'T']
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                       [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
                       [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]]
   visited_cities = set()


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
       current_city = state[0]
       current_city_index = cities.index(current_city)
       for i in range(len(cities)):
           # Check if the city is directly connected to the current city
           if adjacency_matrix[current_city_index][i] == 1:
               new_city = cities[i]
               # Check if the new city is a destination city
               if new_city in ['W', 'X']:
                   # If the new city is a destination city, increment the count of visits to that city
                   new_state = (new_city, state[1] + (new_city == 'W'), state[2] + (new_city == 'X'))
               else:
                   # If the new city is not a destination city, check if it has been visited before
                   if new_city in visited_cities:
                       continue
                   else:
                       visited_cities.add(new_city)
                       new_state = (new_city, state[1], state[2])
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_city], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the number of visits remaining to the destination cities
   # The heuristic relaxes the constraint that we can only visit each city once and presumes we can visit the destination cities directly from the current city
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic estimate, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the number of visits remaining to the destination cities would be 0 in the goal state.
   h = 0
   h += goal[1] - state[1]
   h += goal[2] - state[2]
   return h


print(a_star())
