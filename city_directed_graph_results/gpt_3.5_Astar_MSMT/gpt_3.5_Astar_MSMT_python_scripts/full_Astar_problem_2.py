
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                       [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'D'
   target_cities = ['K', 'Q']
   num_cities = len(adjacency_matrix)
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0
   # Initialize a priority queue of cities not yet visited, with the start city as the first element
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
       for city in range(num_cities):
           if adjacency_matrix[current_city][city] == 1 and city not in path:
               # Generate the new path
               new_path = path + [city]
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if city not in visited_costs or new_cost < visited_costs[city]:
                   visited_costs[city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, new_path, city))
   return None


print(a_star())
