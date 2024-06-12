
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
       [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'I'
   destinations = ['H', 'R']
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
           # If the city is a destination city, we need to visit it twice
           # Check if we have visited the city twice
           if actions.count(city) == 2:
               # If we have visited the city twice, we need to check if we have visited all destination cities twice
               if all(actions.count(dest) == 2 for dest in destinations):
                   return actions
           else:
               # If we have not visited the city twice, add it to the queue again
               heapq.heappush(queue, (g, g, actions, city))


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind(city)][to_city_ind] == 1:
               to_city = ind_to_city(to_city_ind)
               # Check if the new city is a destination city
               if to_city in destinations:
                   # If the new city is a destination city, we need to visit it twice
                   # Check if we have visited the city twice
                   if actions.count(to_city) == 2:
                       # If we have visited the city twice, we need to check if we have visited all destination cities twice
                       if all(actions.count(dest) == 2 for dest in destinations):
                           return actions
                   else:
                       # If we have not visited the city twice, add it to the queue again
                       heapq.heappush(queue, (g, g + 1, actions + [to_city], to_city))
               else:
                   # If the new city is not a destination city, add it to the queue
                   heapq.heappush(queue, (g, g + 1, actions + [to_city], to_city))
   return None


def city_to_ind(city):
   # Convert the city name to its index in the adjacency matrix
   return ord(city) - ord('A')


def ind_to_city(ind):
   # Convert the index in the adjacency matrix to the city name
   return chr(ind + ord('A'))


print(a_star())
