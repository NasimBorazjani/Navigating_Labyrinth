
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
   ]
   # Define the start city and the cities to visit twice
   start = 'S'
   cities_to_visit_twice = ['P', 'G']
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


       # Check if the current city is a city to visit twice
       if city in cities_to_visit_twice:
           # If the current city has been visited twice, remove it from the list of cities to visit twice
           if city in actions:
               cities_to_visit_twice.remove(city)


       # If all cities to visit twice have been visited twice, the current city is the last city to visit
       if not cities_to_visit_twice:
           return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_to_ind][to_city_ind] == 1:
               # Generate the new city
               new_city = chr(ord('A') + to_city_ind)
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   h = heuristic(new_city, cities_to_visit_twice)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, cities_to_visit_twice):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the cities to visit twice
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from one city to another is always 1
   # It's consistent because moving to a city that is closer to the cities to visit twice reduces the heuristic cost of the successor node by a max of 1 (if the moved city is closer to the cities to visit twice), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for to_city in cities_to_visit_twice:
       h += abs(ord(city) - ord(to_city))
   return h


print(a_star())
