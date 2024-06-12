
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'N'
   target_cities = ['H', 'M']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the target cities
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the path
       if path.count('H') == 2 and path.count('M') == 2:
           return path


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1 and next_city != current_city:
               # Check if the new city is a target city and we have visited it less than twice
               if num_cities[next_city] in target_cities and path.count(num_cities[next_city]) < 2:
                   new_path = path + [num_cities[next_city]]
               else:
                   new_path = path
               # Calculate the new cost to reach the next city
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if num_cities[next_city] not in visited_costs or new_cost < visited_costs[num_cities[next_city]]:
                   visited_costs[num_cities[next_city]] = new_cost
                   # The heuristic is the number of target cities that have not been visited twice
                   h = 4 - new_path.count('H') - new_path.count('M')
                   heapq.heappush(queue, (new_cost + h, new_cost, new_path, num_cities[next_city]))
   return None

print(a_star())
