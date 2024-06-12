
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'X'
   destinations = ['E', 'T']
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
       _, g, visited_destinations, actions, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the city is a destination city and we have visited it twice, return the path to reach this city
           if visited_destinations[destinations.index(city)] == 2:
               return actions
           # If the city is a destination city and we have not visited it twice, continue to the next city
           else:
               continue


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind(city)][to_city_ind] == 1:
               to_city = city_from_ind(to_city_ind)
               # Check if the new city would be valid, ie the new city is not the start city and we have not visited it before
               if to_city != start and to_city not in actions:
                   # Generate the new city
                   new_visited_destinations = list(visited_destinations)
                   if to_city in destinations:
                       new_visited_destinations[destinations.index(to_city)] += 1
                   new_city = to_city
                   # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal
                   new_cost = g + 1


                   # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
                   if (new_city, tuple(new_visited_destinations)) not in visited_costs or new_cost < visited_costs[(new_city, tuple(new_visited_destinations))]:
                       visited_costs[(new_city, tuple(new_visited_destinations))] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_city, destinations, visited_destinations), new_cost, new_visited_destinations, actions + [new_city], new_city))
   return None


def heuristic(city, destinations, visited_destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the unvisited destination cities
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
   # It's consistent because moving to a city that is not a destination city does not change the heuristic cost of the successor node
   h = 0
   for destination in destinations:
       if destination not in visited_destinations:
           h += 1
   return h


def city_to_ind(city):
   # Convert the city name to its index in the adjacency matrix
   return ord(city) - ord('A')


def city_from_ind(ind):
   # Convert the index in the adjacency matrix to the city name
   return chr(ind + ord('A'))


print(a_star())
