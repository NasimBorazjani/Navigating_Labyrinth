
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
       [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'G'
   destinations = ['F', 'U']
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
           if actions.count(city) == 1:
               # Generate the new state
               new_actions = actions + [city]
               new_cost = g + 1
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited cities
               if new_actions not in visited_costs or new_cost < visited_costs[new_actions]:
                   visited_costs[new_actions] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_actions, destinations), new_cost, new_actions, city))
           # If we have visited the destination city twice, we can continue to the next city
           else:
               continue


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind(city)][to_city_ind] == 1:
               to_city = city_from_ind(to_city_ind)
               # Check if the new city is a destination city
               if to_city in destinations:
                   # If the city is a destination city, we need to visit it twice
                   if actions.count(to_city) == 1:
                       continue


               # Generate the new state
               new_actions = actions + [to_city]
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_actions not in visited_costs or new_cost < visited_costs[new_actions]:
                   visited_costs[new_actions] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_actions, destinations), new_cost, new_actions, to_city))
   return None


def heuristic(actions, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current state to the destination cities
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each city in the current state is either a destination city or not
   # It's consistent because moving to a city from another city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city in actions:
       if city in destinations:
           h += 1
   return h


def city_from_ind(ind):
   # Convert the index of the city to the city name
   return chr(ord('A') + ind)


def city_to_ind(city):
   # Convert the city name to the index of the city
   return ord(city) - ord('A')


print(a_star())
