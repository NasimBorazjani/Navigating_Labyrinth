
import heapq


def initialize():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are the cities they are connected to
   adjacency_matrix = {
       'X': ['N', 'T', 'V', 'Z', 'S', 'F'],
       'M': ['N', 'T', 'V', 'S'],
       'U': ['N', 'S'],
       'N': ['X', 'M', 'U', 'V', 'S'],
       'T': ['X', 'M', 'U', 'V', 'E'],
       'V': ['M', 'U', 'N', 'T', 'Z', 'S', 'E'],
       'Z': ['M', 'V'],
       'S': ['X', 'N', 'V', 'Z', 'F', 'E'],
       'F': ['S', 'E'],
       'E': ['T', 'V', 'S', 'F', 'J'],
       'J': ['M', 'U', 'V']
   }
  
   # Encoding other variables given in the problem statement
   start_city = 'X'
   goal_cities = ['E', 'T']
   num_visits = 2


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path taken to reach the initial state
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, goal_cities, num_visits, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, goal cities, and number of visits)
   adjacency_matrix, start_city, goal_cities, num_visits, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the path taken
       if all(actions.count(city) == num_visits for city in goal_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any of the cities connected to the current city
       for next_city in adjacency_matrix[current_city]:
           # Check if the new state would be valid, ie we can only visit each city once, apart from the destination cities, and we can only visit the destination cities twice
           if (actions.count(next_city) < 1 or next_city in goal_cities) and actions.count(next_city) < num_visits:
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   h = heuristic(next_city, goal_cities, num_visits)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [current_city], next_city))
                  
   return None


def heuristic(current_city, goal_cities, num_visits):
   # An admissible and consistent heuristic is the number of goal cities that have not been visited the required number of times
   # The heuristic relaxes the constraint that we can only visit each city once, apart from the destination cities, and we can only visit the destination cities twice
   # The heuristic is admissible because it underestimates the cost to reach the goal state, as it only considers the number of goal cities that have not been visited the required number of times
   # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the heuristic estimate if the city is a goal city that has not been visited the required number of times
   h = sum(goal_cities.count(city) < num_visits for city in goal_cities)
   return h


print(a_star())
