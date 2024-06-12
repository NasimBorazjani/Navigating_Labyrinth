
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
       [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
   ]
   # Define the start city and the cities to visit twice
   start = 'C'
   cities_to_visit_twice = ['B', 'L']
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
           # If the current city has been visited twice, continue to the next city
           if actions.count(city) == 2:
               continue


       # If the current city is the goal city, return the actions taken
       if actions.count(city) == len(cities_to_visit_twice) * 2:
           return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[ord(city) - ord('A')][to_city_ind]:
               # Generate the new city
               new_city = chr(to_city_ind + ord('A'))
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal city
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   h = heuristic(new_city, cities_to_visit_twice)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, cities_to_visit_twice):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the cities to visit twice
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each additional city must be visited at least once
   # It's consistent because moving to a city from another city results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved city is one of the cities to visit twice), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for to_city in cities_to_visit_twice:
       # Calculate the distance between the current city and the city to visit twice
       distance = abs(ord(city) - ord(to_city))
       h += distance
   return h


print(a_star())
