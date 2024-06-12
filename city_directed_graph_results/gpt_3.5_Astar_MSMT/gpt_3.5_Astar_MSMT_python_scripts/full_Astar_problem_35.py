
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                       [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   cities = ['A', 'V', 'N', 'Q', 'P', 'S', 'M', 'E', 'L', 'H', 'W', 'G']
   start_city = 'G'
   destination_cities = ['L', 'P']
   num_destinations = 2


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of states not yet visited, with the start city as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list; no actions performed to reach the start city
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, destination_cities, num_destinations, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, cities, start city, and destination cities)
   adjacency_matrix, cities, start_city, destination_cities, num_destinations, visited_costs, queue = initialize()


   while queue:
       _, g, actions, city = heapq.heappop(queue)


       # If we have visited all destination cities twice, return the path taken
       if all(city in destination_cities for city in visited_costs if visited_costs[city] >= 2):
           return actions


       # Generate all possible actions from the current state, which includes moving to any city connected by a one-way road
       city_index = cities.index(city)
       for next_city_index, connected in enumerate(adjacency_matrix[city_index]):
           if connected == 1:
               next_city = cities[next_city_index]
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the destination cities twice
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(next_city, destination_cities), new_cost, actions + [next_city], next_city))
                  
   return None


def heuristic(city, destination_cities):
   # An admissible and consistent heuristic is the number of destination cities not yet visited twice
   # This heuristic relaxes the constraint that we need to visit the destination cities twice, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent because the cost of visiting an unvisited destination city is 1, which is exactly the decrease in the heuristic estimate for the successor node, and the heuristic estimate for the goal state is 0, as all destination cities have been visited twice
   h = sum(1 for dest_city in destination_cities if city != dest_city or visited_costs.get(city, 0) < 2)
   return h


print(a_star())
