
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]]
   cities = ['G', 'D', 'X', 'N', 'Y', 'W', 'A', 'P', 'V', 'H']
   start_city = 'W'
   goal_cities = ['A', 'H']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to get to each city in a list; no path taken to reach the start city
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, cities, start city, and goal cities)
   adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the path taken
       if all(actions.count(city) == 2 for city in goal_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
           if connected == 1:
               new_city = cities[i]
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   # Calculate the heuristic cost, which is the number of goal cities not visited twice yet
                   h = sum(1 for city in goal_cities if actions.count(city) < 2)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
                  
   return None


print(a_star())
