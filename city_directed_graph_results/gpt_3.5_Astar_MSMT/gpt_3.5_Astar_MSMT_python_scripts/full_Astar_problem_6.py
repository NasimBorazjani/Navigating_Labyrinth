
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
                       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'N'
   target_cities = ['D', 'F']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the target cities
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, etc)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()

   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If we have visited both target cities twice, return the path
       if path.count('D') == 2 and path.count('F') == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for city in range(num_cities):
           if adjacency_matrix[current_city][city] == 1 and city not in path:
               new_path = path + [city]
               new_cost = g + 1

               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if city not in visited_costs or new_cost < visited_costs[city]:
                   visited_costs[city] = new_cost
                   h = heuristic(new_path, target_cities)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_path, city))
                  
   return None

def heuristic(path, target_cities):
   # An admissible and consistent heuristic is the count of target cities that have not been visited twice
   # This heuristic relaxes the constraint that each target city must be visited twice, allowing the algorithm to explore paths that may not lead to the goal state but provide a lower bound on the cost to reach the goal
   # The heuristic is consistent because the cost of visiting a target city is 1, which is exactly the decrease in the heuristic estimate if the city is visited, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0
   h = 0
   for city in target_cities:
       if path.count(city) < 2:
           h += 1
   return h

print(a_star())
