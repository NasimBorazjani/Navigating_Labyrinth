
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                       [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'Q'
   destination_cities = ['V', 'F']
   num_cities = 12


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, destination_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, destination cities, and number of cities)
   adjacency_matrix, start_city, destination_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)


       # Check if the current city is one of the destination cities and has been visited twice
       if current_city in destination_cities and path.count(current_city) == 2:
           return path


       # Generate all possible actions from the current city, which includes moving to any city directly connected by a road
       for city in range(num_cities):
           # Check if there is a road from the current city to the next city and the next city has not been visited yet
           if adjacency_matrix[current_city][city] == 1 and city not in path:
               # Generate the new path
               new_path = path + [city]
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if city not in visited_costs or new_cost < visited_costs[city]:
                   visited_costs[city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(city, destination_cities), new_cost, new_path, city))
                  
   return None


def heuristic(city, destination_cities):
   # An admissible and consistent heuristic is the minimum distance from the current city to the nearest destination city
   # This heuristic relaxes the constraint that we need to visit each destination city exactly twice, as it only considers the distance to the nearest destination city, thus reporting a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving from one city to a neighboring city is always 1, which is exactly the decrease in the distance to the nearest destination city, if the neighboring city is closer to the destination city, otherwise the estimated cost of the successor node is the same or higher
   h = min([abs(city - ord(dest)) for dest in destination_cities])
   return h


print(a_star())
