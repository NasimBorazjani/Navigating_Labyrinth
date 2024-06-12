
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adj_matrix = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                 [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                 [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0]]
  
   # Define the cities and the starting city
   cities = ['O', 'Z', 'J', 'K', 'E', 'M', 'T', 'W', 'N', 'Q', 'U', 'Y']
   start_city = 'O'
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the starting city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], start_city)]
  
   return adj_matrix, cities, start_city, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix representing city connections, the cities, and the starting city)
   adj_matrix, cities, start_city, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the actions taken
       if actions.count('N') == 2 and actions.count('T') == 2:
           return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for i, connected in enumerate(adj_matrix[cities.index(current_city)]):
           if connected == 1:
               new_city = cities[i]
               # We can only visit each city once, apart from N and T, thus we need to check if the new city has not been visited yet
               if new_city not in actions or new_city in ['N', 'T']:
                   # Generate the new state
                   new_actions = actions + [new_city]
                   new_cost = g + 1
                  
                   if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                       visited_costs[new_city] = new_cost
                       # The heuristic is 0 as we are not estimating the cost to reach the goal state, only minimizing the number of actions taken
                       heapq.heappush(queue, (0, new_cost, new_actions, new_city))
                  
   return None


print(a_star())
