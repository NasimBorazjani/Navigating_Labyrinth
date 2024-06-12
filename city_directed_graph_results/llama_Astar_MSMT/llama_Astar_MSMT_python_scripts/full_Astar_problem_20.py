
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                      [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]
   start = 'F'
   destinations = {'I': 2, 'N': 2}
   cities = 'FIYRXQMSCDN'
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[(start, destinations.copy())] = 0


   queue = [(0, 0, [start], (start, destinations.copy()))]
  
   return adjacency_matrix, start, destinations, cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start, destinations, cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # If we have visited all cities and met the visiting conditions for the destinations, return the path
       if len(path) == num_cities:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           city = cities[i]
           if city not in path:
               # Check if visiting the city would meet the visiting conditions for the destinations
               if city in destinations and destinations[city] > 0:
                   destinations[city] -= 1
               # Generate the new state
               new_state = (city, destinations.copy())
               # Cost of the new state is the travel time to get to the new city in the adjacency matrix
               new_cost = g + adjacency_matrix[cities.index(path[-1])][i]


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, destinations), new_cost, path + [city], new_state))
   return None




def heuristic(state, destinations):
   # The heuristic function can be a simple count of the remaining destinations to visit
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost of the next node is higher if we visit a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of times we can visit a destination city is 2
   h = sum(value for city, value in destinations.items() if city not in state[0])
   return h


print(a_star())
