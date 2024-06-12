
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
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
  
   # Encoding other variables given in the problem statement
   start_city = 'E'
   target_cities = ['W', 'X']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, and number of cities)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()

   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If we have visited both target cities twice, return the path
       if path.count(target_cities[0]) == 2 and path.count(target_cities[1]) == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1 and next_city not in path:
               new_path = path + [next_city]
               new_cost = g + 1

               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(next_city, target_cities), new_cost, new_path, next_city))
                  
   return None

def heuristic(city, target_cities):
   # An admissible and consistent heuristic is the number of target cities not yet visited twice
   # This heuristic relaxes the constraint that each target city must be visited twice, thus reporting a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of reaching a city is always 1, which is exactly the decrease in the number of target cities not yet visited twice, if the city is one of the target cities, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all target cities have been visited twice
   h = 0
   for target in target_cities:
       if city != target:
           h += 1
   return h

print(a_star())
