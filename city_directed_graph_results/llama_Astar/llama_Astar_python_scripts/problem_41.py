
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'E'
   destinations = ['A', 'Y']
   num_cities = len(adjacency_matrix)


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each city in a list; no path performed to reach the start city
   queue = [(0, 0, [], start)]


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the city is a destination city, check if we have visited it twice
           if actions.count(city) == 2:
               # If we have visited the destination city twice, return the path to reach the city
               return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind(city)][to_city_ind] == 1:
               # Generate the new city
               new_city = city_ind_to_city(to_city_ind)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal city
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_city, destinations), new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
   # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   h = 0
   for dest in destinations:
       h += city_distance(city, dest)
   return h


def city_distance(city1, city2):
   # The distance between two cities is the number of roads between them
   # The distance is the same for both directly connected cities
   return 1


def city_to_ind(city):
   # Convert the city name to its index in the adjacency matrix
   return ord(city) - ord('A')


def city_ind_to_city(ind):
   # Convert the city index in the adjacency matrix to its name
   return chr(ind + ord('A'))


print(a_star())
