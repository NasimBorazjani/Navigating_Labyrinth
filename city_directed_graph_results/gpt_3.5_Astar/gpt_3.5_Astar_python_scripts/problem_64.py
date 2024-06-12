
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'Z': {'D': 1, 'R': 1},
       'J': {'V': 1, 'H': 1},
       'T': {'Z': 1, 'D': 1},
       'D': {'Z': 1, 'T': 1, 'W': 1, 'L': 1, 'P': 1, 'R': 1},
       'W': {'Z': 1, 'J': 1, 'L': 1, 'V': 1, 'R': 1},
       'L': {'J': 1, 'T': 1, 'W': 1, 'V': 1, 'H': 1, 'R': 1},
       'P': {'T': 1, 'J': 1, 'W': 1, 'V': 1},
       'Y': {'T': 1, 'V': 1},
       'V': {'T': 1, 'D': 1, 'P': 1, 'R': 1, 'I': 1},
       'H': {'T': 1, 'R': 1},
       'R': {'Z': 1, 'T': 1, 'W': 1, 'L': 1, 'V': 1},
       'I': {'T': 1, 'D': 1, 'V': 1},
       'A': {'J': 1, 'L': 1, 'P': 1, 'Y': 1}
   }
  
   # Define the initial state, which is the starting city
   initial_state = 'Y'
   # Define the goal state, which is to visit cities D and R twice each
   goal_state = ['D', 'D', 'R', 'R']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # Initialize a priority queue of cities not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [initial_state], initial_state)]
  
   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)
      
       # If we have visited all the goal cities twice, return the path
       if all(goal_state.count(city) <= path.count(city) for city in set(goal_state)):
           return path
      
       # Generate all possible actions from the current city, which includes moving to any connected city
       for next_city, cost in adjacency_matrix[current_city].items():
           new_cost = g + cost
           new_path = path + [next_city]
          
           # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           if next_city not in visited_costs or new_cost < visited_costs[next_city]:
               visited_costs[next_city] = new_cost
               # Calculate the heuristic cost as the number of goal cities not yet visited twice
               h = sum(max(0, goal_state.count(city) - new_path.count(city)) for city in set(goal_state))
               heapq.heappush(queue, (new_cost + h, new_cost, new_path, next_city))
  
   return None


print(a_star())
