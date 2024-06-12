
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
   adjacency_matrix = {
       'O': {'A': 1},
       'T': {'I': 1},
       'I': {'A': 1, 'F': 1, 'Y': 1, 'G': 1},
       'F': {'I': 1, 'R': 1},
       'A': {'O': 1, 'I': 1, 'X': 1},
       'M': {'F': 1, 'R': 1},
       'X': {'I': 1, 'F': 1, 'Y': 1},
       'Y': {'A': 1, 'X': 1, 'R': 1, 'G': 1},
       'R': {'T': 1, 'M': 1, 'Y': 1},
       'G': {'F': 1, 'Y': 1}
   }
   start_city = 'M'
   goal_cities = ['A', 'R']
   num_visits = 2


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # The initial state is represented as a tuple containing the current city, the number of times A has been visited, and the number of times R has been visited
   heappush(queue, (0, 0, [], (start_city, 0, 0)))


   while queue:
       _, g, actions, state = heappop(queue)


       # If both A and R have been visited the required number of times, return the actions taken
       if state[1] == num_visits and state[2] == num_visits:
           return actions


       # Generate all possible actions from the current state, which includes moving to any connected city
       current_city, a_visits, r_visits = state
       for next_city in adjacency_matrix[current_city]:
           # Check if visiting the next city would be valid, ie the city has not been visited before or we are allowed to visit it again
           if (next_city != 'A' or a_visits < num_visits) and (next_city != 'R' or r_visits < num_visits):
               # Generate the new state
               new_state = (next_city, a_visits + (1 if next_city == 'A' else 0), r_visits + (1 if next_city == 'R' else 0))
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
               new_cost = g + 1
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Calculate the heuristic cost as the number of cities left to visit
                   h = num_visits - a_visits + num_visits - r_visits
                   heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
   return None


print(a_star())
