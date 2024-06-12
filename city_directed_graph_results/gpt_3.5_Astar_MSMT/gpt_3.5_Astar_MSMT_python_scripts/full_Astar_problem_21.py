
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                       [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'Y'
   target_cities = ['I', 'Q']
   num_cities = len(adjacency_matrix)


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to get to each city in a list; no path taken to reach the start city
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, and number of cities)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If the current city is one of the target cities and it has been visited twice, return the path taken
       if current_city in target_cities and actions.count(current_city) == 2:
           return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the target cities
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(next_city, target_cities), new_cost, actions + [current_city], next_city))
                  
   return None


def heuristic(city, target_cities):
   # An admissible and consistent heuristic is the number of cities remaining to visit, excluding the target cities that have been visited twice
   # This heuristic relaxes the constraint that only target cities can be visited twice, as it assumes the remaining cities can be visited once
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as it assumes the remaining cities can be visited once, ensuring a lower cost estimate
   # The heuristic is consistent because the cost of visiting a city is always 1, which is exactly the decrease in the number of remaining cities, if the city is visited, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining cities to visit
   return len(target_cities) - target_cities.count(city)


print(a_star())
