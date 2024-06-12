
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
   ]
   # Define the start city
   start = 'S'
   # Define the destination cities
   destinations = ['P', 'G']
   # Define the number of visits to each destination city
   visits_required = 2
   # Define the number of cities
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   queue = [(0, 0, [], (start, 0, 0))]
  
   return adj_matrix, start, destinations, visits_required, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, visits_required, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and the required number of visits has been made, return the actions taken
       if state[0] in destinations and state[1] == visits_required:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[2]][i] == 1:
               # Check if the new state is valid, ie if the city is not a destination city or the required number of visits has not been made
               if (state[0] not in destinations or state[1] < visits_required) and i not in [state[2] for _, _, _, (_, _, city) in actions]:
                   # Generate the new state
                   new_state = (state[0], state[1], i)
                   # The cost of the new state is the travel time to get to the new city in the adjacency matrix
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the Manhattan distance to the destination cities
                       h = heuristic(new_state, destinations)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(state[0], state[1], i)], new_state))
   return None




def heuristic(state, destinations):
   # The heuristic is the Manhattan distance to the destination cities
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the Manhattan distance
   h = 0
   for city in destinations:
       h += abs(state[2] - city)
   return h


print(a_star())
