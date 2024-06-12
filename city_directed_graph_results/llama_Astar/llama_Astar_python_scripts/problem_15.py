
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
       [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'E'
   destinations = ['W', 'X']
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
       _, g, w_visits, x_visits, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the destination city is W
           if city == 'W':
               # If we have visited W exactly twice, return the path to reach this city
               if w_visits == 2:
                   return path
           # If the destination city is X
           else:
               # If we have visited X exactly twice, return the path to reach this city
               if x_visits == 2:
                   return path


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           # Check if the new city is not the current city and there is a direct road between the current city and the new city
           if to_city_ind != city and adjacency_matrix[city][to_city_ind] == 1:
               # Generate the new city
               new_city = chr(ord('A') + to_city_ind)
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal
               new_cost = g + 1
               # Update the number of visits to W and X
               new_w_visits = w_visits + (1 if new_city == 'W' else 0)
               new_x_visits = x_visits + (1 if new_city == 'X' else 0)


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if (new_city, new_w_visits, new_x_visits) not in visited_costs or new_cost < visited_costs[(new_city, new_w_visits, new_x_visits)]:
                   visited_costs[(new_city, new_w_visits, new_x_visits)] = new_cost
                   h = heuristic(new_city, destinations, adjacency_matrix)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_w_visits, new_x_visits, new_city))
   return None


def heuristic(city, destinations, adjacency_matrix):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of reaching a city is always less than or equal to the cost of reaching the goal
   # It is consistent because moving to a city that is closer to a destination city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is closer to the destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for dest in destinations:
       # Calculate the distance from the current city to the destination city
       distance = sum(adjacency_matrix[city - ord('A')][i] + adjacency_matrix[i][dest - ord('A')] for i in range(len(adjacency_matrix)))
       h += distance
   return h


print(a_star())
