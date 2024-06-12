
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
   adjacency_matrix = {
       'D': {'Z': 1, 'X': 1, 'B': 1},
       'Z': {'D': 1, 'T': 1, 'X': 1, 'H': 1, 'Y': 1},
       'T': {'Z': 1, 'H': 1, 'Q': 1},
       'X': {'L': 1, 'B': 1},
       'L': {'D': 1, 'Z': 1, 'K': 1, 'Q': 1},
       'K': {'D': 1, 'T': 1, 'A': 1},
       'N': {'D': 1, 'A': 1, 'Y': 1},
       'H': {'Z': 1, 'T': 1, 'N': 1, 'Q': 1},
       'U': {'Q': 1, 'B': 1},
       'A': {'L': 1, 'U': 1},
       'Q': {'T': 1, 'L': 1, 'H': 1, 'U': 1},
       'B': {'D': 1, 'Z': 1, 'K': 1, 'U': 1, 'Y': 1},
       'Y': {'Z': 1, 'N': 1, 'B': 1}
   }
   start_city = 'H'
   goal_cities = ['B', 'X']
  
   visited_costs = {}
   visited_costs[start_city] = 0

   queue = [(0, 0, [start_city], start_city)]

   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # Check if we have visited both goal cities twice
       if path.count('B') == 2 and path.count('X') == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any connected city
       for neighbor in adjacency_matrix[current_city]:
           new_path = path + [neighbor]
           new_cost = g + 1

           # If the new city is not visited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_path, goal_cities), new_cost, new_path, neighbor))
              
   return None


def heuristic(path, goal_cities):
   # The heuristic function calculates the number of goal cities that have not been visited twice yet
   # This heuristic is admissible because it underestimates the cost to reach the goal state, as we need to visit each goal city twice
   # The heuristic is consistent because the cost of reaching a city is always 1, and the heuristic estimate for the goal state is 0, as all goal cities have been visited twice
   return len([city for city in goal_cities if path.count(city) < 2])


print(a_star())
