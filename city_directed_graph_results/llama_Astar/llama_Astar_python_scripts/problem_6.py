
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
   ]
   # Define the start city and the destination cities
   start = 'N'
   destinations = ['D', 'F']
   num_cities = len(adjacency_matrix)


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each city in a list; no path performed to reach the start city
   queue = [(0, 0, 0, [], start)]


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, d_visits, f_visits, city, path = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the destination city is D
           if city == 'D':
               # If we have visited D exactly twice, return the path to reach this city
               if d_visits == 2:
                   return path + [city]
           # If the destination city is F
           else:
               # If we have visited F exactly twice, return the path to reach this city
               if f_visits == 2:
                   return path + [city]


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for next_city in range(num_cities):
           # Check if the next city is a valid action, ie there is a direct road from the current city to the next city
           if adjacency_matrix[city_to_index[city]][next_city] == 1:
               # Generate the new city
               new_city = index_to_city[next_city]
               # Update the number of visits to the destination cities
               new_d_visits = d_visits + (1 if new_city == 'D' else 0)
               new_f_visits = f_visits + (1 if new_city == 'F' else 0)
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if (new_city, new_d_visits, new_f_visits) not in visited_costs or new_cost < visited_costs[(new_city, new_d_visits, new_f_visits)]:
                   visited_costs[(new_city, new_d_visits, new_f_visits)] = new_cost
                   h = heuristic(new_city, destinations, adjacency_matrix)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_d_visits, new_f_visits, new_city, path + [city]))
   return None


def heuristic(city, destinations, adjacency_matrix):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of reaching the goal is the sum of the distances from the current city to the destination cities
   # It is consistent because moving to a city that is closer to a destination city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is closer to the destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for destination in destinations:
       h += abs(city_to_index[city] - city_to_index[destination])
   return h


city_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
index_to_city = {v: k for k, v in city_to_index.items()}


print(a_star())
