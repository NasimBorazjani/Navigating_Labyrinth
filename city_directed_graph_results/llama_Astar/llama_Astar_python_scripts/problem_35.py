
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'G'
   destinations = ['L', 'P']
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
               to_city = city_from_ind(to_city_ind)
               # Check if the new city would be valid, ie we have not visited the city before
               if to_city not in actions:
                   # Generate the new city
                   new_city = to_city
                   # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal city
                   new_cost = g + 1


                   # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                   if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                       visited_costs[new_city] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_city, destinations), new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the goal cities
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
   # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a goal city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for destination in destinations:
       if city != destination:
           h += 1
   return h


def city_to_ind(city):
   # Convert the city name to its index in the adjacency matrix
   return ord(city) - ord('A')


def city_from_ind(ind):
   # Convert the index in the adjacency matrix to the corresponding city name
   return chr(ind + ord('A'))


print(a_star())