
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'B'
   destinations = ['L', 'V']
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
       _, g, l_visits, v_visits, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the destination city is L, update the l_visits count
           if city == 'L':
               l_visits += 1
           # If the destination city is V, update the v_visits count
           else:
               v_visits += 1


           # If we have visited both destination cities twice, return the path to reach the current city
           if l_visits == 2 and v_visits == 2:
               return city


           # If we have visited one destination city twice, continue to the next destination city
           continue


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind(city)][to_city_ind] == 1:
               to_city = ind_to_city(to_city_ind)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if (to_city, l_visits, v_visits) not in visited_costs or new_cost < visited_costs[(to_city, l_visits, v_visits)]:
                   visited_costs[(to_city, l_visits, v_visits)] = new_cost
                   h = heuristic(to_city, destinations, l_visits, v_visits)
                   heapq.heappush(queue, (new_cost + h, new_cost, l_visits, v_visits, to_city))
   return None


def heuristic(city, destinations, l_visits, v_visits):
   # An admissible and consistent heuristic for this problem is the sum of the distances to the nearest destination city, weighted by the number of visits left to each destination
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each move must be made at least once
   # It's consistent because moving to a city always reduces the heuristic cost of the successor node by a max of 1 (if the moved city is the nearest destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for dest in destinations:
       # Calculate the distance to the destination city
       distance = abs(city_to_ind(city) - city_to_ind(dest))
       # If the destination city is L, add the distance weighted by the number of visits left to L
       if dest == 'L':
           h += distance * (2 - l_visits)
       # If the destination city is V, add the distance weighted by the number of visits left to V
       else:
           h += distance * (2 - v_visits)
   return h


def city_to_ind(city):
   # Convert the city name to its index in the adjacency matrix
   return ord(city) - ord('A')


def ind_to_city(ind):
   # Convert the index in the adjacency matrix to the corresponding city name
   return chr(ind + ord('A'))


print(a_star())
