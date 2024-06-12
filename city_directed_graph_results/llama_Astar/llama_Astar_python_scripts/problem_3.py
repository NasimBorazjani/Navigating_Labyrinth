
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
   ]
   # Define the start city and the destination cities
   start = 'M'
   destinations = ['A', 'R']
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
       _, g, a_visits, r_visits, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the destination city is A, update the count of visits to A
           if city == 'A':
               a_visits += 1
           # If the destination city is R, update the count of visits to R
           else:
               r_visits += 1


           # If we have visited both destination cities exactly twice, return the path to reach the current city
           if a_visits == 2 and r_visits == 2:
               return city


           # If we have not visited both destination cities exactly twice, continue the search
           else:
               # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
               for next_city in range(num_cities):
                   if adjacency_matrix[city_to_index[city]][next_city] == 1:
                       next_city_name = index_to_city[next_city]
                       # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal
                       new_cost = g + 1
                       # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                       if (next_city_name, a_visits, r_visits) not in visited_costs or new_cost < visited_costs[(next_city_name, a_visits, r_visits)]:
                           visited_costs[(next_city_name, a_visits, r_visits)] = new_cost
                           h = heuristic(next_city_name, a_visits, r_visits, destinations)
                           heapq.heappush(queue, (new_cost + h, new_cost, a_visits, r_visits, next_city_name))
   return None


def heuristic(city, a_visits, r_visits, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the remaining destination cities
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each move made is a direct road from one city to another
   # It is consistent because moving to a city always reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for destination in destinations:
       if destination != city:
           h += 1
   return h


city_to_index = {'O': 0, 'T': 1, 'I': 2, 'F': 3, 'A': 4, 'M': 5, 'X': 6, 'Y': 7, 'R': 8, 'G': 9}
index_to_city = {0: 'O', 1: 'T', 2: 'I', 3: 'F', 4: 'A', 5: 'M', 6: 'X', 7: 'Y', 8: 'R', 9: 'G'}


print(a_star())
