
import heapq


def a_star():
   # Define the adjacency matrix of the cities and the start city
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
   ]
   start = 'A'
  
   # Define the goal cities and the number of times we need to visit each
   goal_cities = {'D': 2, 'E': 2}
  
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


       # Check if the current city is a goal city
       if city in goal_cities:
           # If we have visited the goal city the required number of times, return the path to reach this city
           if goal_cities[city] == 0:
               return actions
           # Otherwise, decrement the number of times we need to visit this city
           else:
               goal_cities[city] -= 1


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind, is_connected in enumerate(adjacency_matrix[ord(city) - ord('A')]):
           if is_connected:
               to_city = chr(to_city_ind + ord('A'))
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal cities
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if to_city not in visited_costs or new_cost < visited_costs[to_city]:
                   visited_costs[to_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(to_city, goal_cities), new_cost, actions + [to_city], to_city))
   return None


def heuristic(city, goal_cities):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the goal cities
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
   # It's consistent because moving to a city from another city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a goal city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for goal_city, times in goal_cities.items():
       if goal_city != city:
           h += 1
   return h


print(a_star())
