
import heapq


def a_star():
   # Define the adjacency matrix of the cities and the start city
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
   ]
   start = 'C'
  
   # Define the goal cities and the number of times we need to visit each
   goal_cities = {'J': 2, 'D': 2}
  
   # Define the list of cities and their indices in the adjacency matrix
   cities = ['C', 'L', 'D', 'O', 'A', 'Z', 'M', 'H', 'K', 'R', 'Q', 'N', 'J']
   city_indices = {city: index for index, city in enumerate(cities)}
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start] = 0
  
   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each city in a list; no path performed to reach the start city
   queue = [(0, 0, [], start)]


   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, city = heapq.heappop(queue)


       # Check if the current city is a goal city and we have visited it the required number of times
       if city in goal_cities and actions.count(city) == goal_cities[city]:
           return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for next_city_index, connected in enumerate(adjacency_matrix[city_indices[city]]):
           if connected:
               next_city = cities[next_city_index]
               # Generate the new city
               new_city = next_city
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   h = heuristic(new_city, goal_cities, city_indices, adjacency_matrix)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, goal_cities, city_indices, adjacency_matrix):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of roads to travel to reach each goal city from the current city
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each road must be traveled at least once
   # It's consistent because moving to a city results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved city is closer to one of the goal cities), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for goal_city, times in goal_cities.items():
       if goal_city != city:
           h += min(adjacency_matrix[city_indices[city]][city_indices[goal_city]], adjacency_matrix[city_indices[goal_city]][city_indices[city]])
   return h


print(a_star())
