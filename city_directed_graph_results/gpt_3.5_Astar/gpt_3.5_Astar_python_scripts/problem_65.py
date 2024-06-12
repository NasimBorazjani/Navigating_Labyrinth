
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary with city names as keys and their connections as values
   adjacency_matrix = {
       'F': {'D': 0, 'E': 0, 'Z': 1, 'G': 0, 'Y': 0, 'N': 0, 'I': 1, 'X': 0, 'P': 1, 'S': 0, 'Q': 0, 'C': 0},
       'D': {'F': 1, 'E': 0, 'Z': 1, 'G': 0, 'Y': 0, 'N': 0, 'I': 1, 'X': 0, 'P': 0, 'S': 0, 'Q': 0, 'C': 0},
       'E': {'F': 0, 'D': 0, 'Z': 0, 'G': 1, 'Y': 0, 'N': 0, 'I': 0, 'X': 0, 'P': 0, 'S': 1, 'Q': 0, 'C': 1},
       'Z': {'F': 0, 'D': 0, 'E': 1, 'G': 0, 'Y': 1, 'N': 0, 'I': 0, 'X': 1, 'P': 0, 'S': 1, 'Q': 0, 'C': 1},
       'G': {'F': 1, 'D': 0, 'E': 0, 'Z': 0, 'Y': 0, 'N': 0, 'I': 1, 'X': 0, 'P': 1, 'S': 0, 'Q': 0, 'C': 0},
       'Y': {'F': 0, 'D': 0, 'E': 0, 'Z': 0, 'G': 1, 'N': 0, 'I': 1, 'X': 0, 'P': 0, 'S': 0, 'Q': 0, 'C': 0},
       'N': {'F': 0, 'D': 0, 'E': 0, 'Z': 0, 'G': 0, 'Y': 1, 'I': 0, 'X': 0, 'P': 0, 'S': 0, 'Q': 0, 'C': 0},
       'I': {'F': 0, 'D': 0, 'E': 1, 'Z': 1, 'G': 0, 'Y': 0, 'N': 0, 'X': 1, 'P': 0, 'S': 0, 'Q': 0, 'C': 0},
       'X': {'F': 0, 'D': 0, 'E': 1, 'Z': 0, 'G': 1, 'Y': 0, 'N': 0, 'I': 0, 'P': 1, 'S': 0, 'Q': 0, 'C': 0},
       'P': {'F': 0, 'D': 1, 'E': 0, 'Z': 1, 'G': 0, 'Y': 0, 'N': 0, 'I': 0, 'X': 0, 'S': 0, 'Q': 1, 'C': 0},
       'S': {'F': 1, 'D': 1, 'E': 0, 'Z': 0, 'G': 0, 'Y': 0, 'N': 1, 'I': 0, 'X': 1, 'P': 0, 'Q': 0, 'C': 1},
       'Q': {'F': 0, 'D': 1, 'E': 0, 'Z': 0, 'G': 0, 'Y': 0, 'N': 0, 'I': 0, 'X': 1, 'P': 0, 'S': 0, 'C': 0},
       'C': {'F': 0, 'D': 0, 'E': 0, 'Z': 0, 'G': 1, 'Y': 0, 'N': 1, 'I': 1, 'X': 1, 'P': 0, 'S': 0, 'Q': 0}
   }
  
   # Define the initial state, goal state, and other variables
   initial_state = 'Q'
   goal_state = ['F', 'N']
   num_visits = 2
   visited = {initial_state: 1}
   path = [initial_state]
   queue = [(0, initial_state, path)]


   while queue:
       _, current_city, path = heapq.heappop(queue)


       # If we have visited the goal cities the required number of times, return the path
       if path.count(goal_state[0]) == num_visits and path.count(goal_state[1]) == num_visits:
           return path


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for city, connected in adjacency_matrix[current_city].items():
           if connected == 1 and visited.get(city, 0) < num_visits:
               visited[city] = visited.get(city, 0) + 1
               heapq.heappush(queue, (len(path), city, path + [city]))
   return None


print(a_star())
