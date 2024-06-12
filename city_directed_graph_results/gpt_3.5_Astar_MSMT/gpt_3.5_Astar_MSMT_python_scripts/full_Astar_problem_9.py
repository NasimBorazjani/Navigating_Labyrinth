
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]]
   # Define the cities and the starting city
   cities = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
   start_city = 'C'
   # Define the goal cities to visit twice
   goal_cities = ['F', 'W']
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0
   # Initialize a priority queue of cities not yet visited, with the starting city as the first element
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem
   adjacency_matrix, cities, start_city, goal_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)


       # If we have visited both goal cities twice, return the path
       if all(path.count(city) == 2 for city in goal_cities):
           return path


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
           if connected == 1 and cities[i] not in path:
               new_path = path + [cities[i]]
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
               if cities[i] not in visited_costs or new_cost < visited_costs[cities[i]]:
                   visited_costs[cities[i]] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_path, goal_cities), new_cost, new_path, cities[i]))
                  
   return None


def heuristic(path, goal_cities):
   # A heuristic for this problem can be the number of goal cities that have not been visited twice yet
   # This heuristic is admissible because it underestimates the cost to reach the goal state, as it only considers the number of goal cities that have not been visited twice yet
   # The heuristic is consistent because the cost of reaching a city is always 1, and the heuristic estimate for the goal state is 0, as all goal cities have been visited twice
   h = sum(2 - path.count(city) for city in goal_cities)
   return h


print(a_star())
