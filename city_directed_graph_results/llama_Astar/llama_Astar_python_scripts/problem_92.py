
import heapq


def a_star():
   # Define the adjacency matrix and the start city
   adjacency_matrix = [
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
       [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
       [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
   ]
   start = 'F'
  
   # Define the goal cities and the number of visits required for each
   goal_cities = {'R': 2, 'S': 2}
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start] = 0
  
   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path required to get to each city in a list; no path performed to reach the start city
   queue = [(0, 0, [], start)]


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, city = heapq.heappop(queue)


       # Check if the current city is a goal city
       if city in goal_cities:
           # If the city has been visited the required number of times, return the path to this city
           if actions.count(city) == goal_cities[city]:
               return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind, is_connected in enumerate(adjacency_matrix[ord(city) - ord('A')]):
           if is_connected:
               to_city = chr(to_city_ind + ord('A'))
               # Generate the new city
               new_city = to_city
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal city
               new_cost = g + 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_city, goal_cities), new_cost, actions + [new_city], new_city))
   return None


def heuristic(city, goal_cities):
   # An admissible and consistent heuristic for this problem is the sum of the remaining number of visits to the goal cities
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each visit to a goal city must be made at least once
   # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a goal city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = sum(goal_cities[city] for city in goal_cities if city != city)
   return h


print(a_star())
