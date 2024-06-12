
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                       [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'D'
   target_cities = ['B', 'L']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If we have visited both target cities twice, return the path
       if path.count('B') == 2 and path.count('L') == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for city in range(num_cities):
           if adjacency_matrix[current_city][city] == 1 and city not in path:
               new_path = path + [city]
               new_cost = g + 1

               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if city not in visited_costs or new_cost < visited_costs[city]:
                   visited_costs[city] = new_cost
                   # Calculate the heuristic cost as the number of target cities not yet visited twice
                   h = 4 - new_path.count('B') - new_path.count('L')
                   heapq.heappush(queue, (new_cost + h, new_cost, new_path, city))
                  
   return None

print(a_star())
