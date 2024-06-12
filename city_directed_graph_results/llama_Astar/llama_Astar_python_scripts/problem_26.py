
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'I'
   destinations = ['L', 'W']
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
       _, g, l_visits, w_visits, city = heapq.heappop(queue)


       # Check if the current city is a destination city
       if city in destinations:
           # If the destination city is 'L'
           if city == 'L':
               # If we have visited 'L' exactly twice, return the path to reach this city
               if l_visits == 2:
                   return path
           # If the destination city is 'W'
           else:
               # If we have visited 'W' exactly twice, return the path to reach this city
               if w_visits == 2:
                   return path


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for to_city_ind in range(num_cities):
           if adjacency_matrix[city_ind][to_city_ind] == 1:
               # Generate the new city
               new_city = chr(to_city_ind + 65)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
               new_l_visits, new_w_visits = l_visits, w_visits
               # Update the visit counts for the new city
               if new_city == 'L':
                   new_l_visits += 1
               elif new_city == 'W':
                   new_w_visits += 1


               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if (new_city, new_l_visits, new_w_visits) not in visited_costs or new_cost < visited_costs[(new_city, new_l_visits, new_w_visits)]:
                   visited_costs[(new_city, new_l_visits, new_w_visits)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_city, destinations, adjacency_matrix), new_cost, new_l_visits, new_w_visits, new_city))
   return None


def heuristic(city, destinations, adjacency_matrix):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each additional city in the path increases the heuristic cost of the successor node by a max of 1
   # It's consistent because moving to a city in the path reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for dest in destinations:
       # Calculate the distance from the current city to the destination city using the adjacency matrix
       h += sum(adjacency_matrix[ord(city) - 65][i] for i in range(num_cities))
   return h


print(a_star())
