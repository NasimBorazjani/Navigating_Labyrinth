
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'L': {'E': 1, 'M': 1},
       'Y': {'E': 1, 'Z': 1, 'O': 1},
       'V': {'L': 1, 'M': 1, 'Q': 1},
       'E': {},
       'A': {'E': 1, 'C': 1},
       'M': {'E': 1, 'L': 1, 'Q': 1},
       'C': {'M': 1, 'Y': 1},
       'Q': {'Y': 1, 'F': 1},
       'F': {'L': 1, 'Y': 1, 'V': 1, 'M': 1, 'Z': 1},
       'Z': {'Y': 1, 'F': 1},
       'G': {'Y': 1, 'V': 1},
       'O': {'Y': 1, 'V': 1, 'G': 1}
   }
  
   # Define the initial state, goal state, and other variables
   initial_state = 'E'
   goal_state = ['A', 'Y']
   num_visits = 2
   visited_states = {initial_state: 0}
   queue = [(0, [initial_state], initial_state, 0)]


   while queue:
       _, path, current_state, num_goal_visits = heapq.heappop(queue)


       # If we have visited both goal cities twice, return the path
       if num_goal_visits == num_visits:
           return path


       # Generate all possible actions from the current state, which are the cities connected to the current city
       for neighbor in adjacency_matrix[current_state]:
           # Check if the neighbor city has not been visited yet
           if neighbor not in path:
               new_path = path + [neighbor]
               new_num_goal_visits = num_goal_visits + (1 if neighbor in goal_state else 0)
               new_cost = len(new_path)
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
               if neighbor not in visited_states or new_cost < visited_states[neighbor]:
                   visited_states[neighbor] = new_cost
                   heapq.heappush(queue, (new_cost, new_path, neighbor, new_num_goal_visits))
                  
   return None


print(a_star())
