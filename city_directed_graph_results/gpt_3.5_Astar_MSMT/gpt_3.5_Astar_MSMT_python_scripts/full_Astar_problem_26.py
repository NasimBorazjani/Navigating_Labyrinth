
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                       [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                       [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'I'
   target_cities = ['W', 'L']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to get to each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, etc)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the path taken
       if all(path.count(city) == 2 for city in target_cities):
           return path


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for city in range(num_cities):
           if adjacency_matrix[current_city][city] == 1:
               new_path = path + [city]
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if city not in visited_costs or new_cost < visited_costs[city]:
                   visited_costs[city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(city, target_cities), new_cost, new_path, city))
                  
   return None


def heuristic(city, target_cities):
   # An admissible and consistent heuristic is the number of target cities that have not been visited twice yet
   # This heuristic relaxes the constraint that each target city must be visited twice, allowing us to estimate a lower cost to reach the goal state
   # The heuristic is consistent because the cost of reaching a city is always 1, which is exactly the decrease in the number of target cities that have not been visited twice yet
   h = sum(2 - path.count(city) for city in target_cities)
   return h


print(a_star())
