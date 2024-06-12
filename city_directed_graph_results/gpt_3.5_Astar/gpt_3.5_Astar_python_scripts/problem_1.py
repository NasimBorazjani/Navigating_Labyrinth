
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'G': {'G': 0, 'D': 0, 'X': 1, 'N': 0, 'Y': 0, 'W': 0, 'A': 1, 'P': 1, 'V': 1, 'H': 1},
       'D': {'G': 0, 'D': 0, 'X': 0, 'N': 0, 'Y': 0, 'W': 0, 'A': 1, 'P': 0, 'V': 0, 'H': 1},
       'X': {'G': 0, 'D': 0, 'X': 0, 'N': 0, 'Y': 1, 'W': 1, 'A': 1, 'P': 0, 'V': 0, 'H': 0},
       'N': {'G': 0, 'D': 0, 'X': 0, 'N': 0, 'Y': 1, 'W': 0, 'A': 0, 'P': 0, 'V': 0, 'H': 1},
       'Y': {'G': 0, 'D': 0, 'X': 1, 'N': 1, 'Y': 0, 'W': 0, 'A': 0, 'P': 1, 'V': 0, 'H': 0},
       'W': {'G': 0, 'D': 0, 'X': 1, 'N': 0, 'Y': 0, 'W': 0, 'A': 0, 'P': 0, 'V': 0, 'H': 0},
       'A': {'G': 0, 'D': 0, 'X': 1, 'N': 0, 'Y': 0, 'W': 0, 'A': 0, 'P': 0, 'V': 1, 'H': 1},
       'P': {'G': 0, 'D': 0, 'X': 0, 'N': 0, 'Y': 1, 'W': 0, 'A': 0, 'P': 0, 'V': 0, 'H': 1},
       'V': {'G': 0, 'D': 0, 'X': 0, 'N': 0, 'Y': 0, 'W': 0, 'A': 1, 'P': 0, 'V': 0, 'H': 0},
       'H': {'G': 0, 'D': 0, 'X': 1, 'N': 1, 'Y': 0, 'W': 0, 'A': 0, 'P': 1, 'V': 0, 'H': 0}
   }
  
   # Encoding other variables given in the problem statement
   start_city = 'W'
   target_cities = ['A', 'H']
   num_targets = 2


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], (start_city, 0, 0)))


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited both target cities twice, return the actions taken
       if state[1] == num_targets and state[2] == num_targets:
           return actions


       # Generate all possible actions from the current state, which includes moving to any city that has a direct road from the current city
       current_city = state[0]
       for next_city in adjacency_matrix[current_city]:
           if adjacency_matrix[current_city][next_city] == 1:
               # Check if the new state would be valid, ie we have not visited the next city before
               if (next_city != state[0] and
                   (next_city != target_cities[0] or state[1] < num_targets) and
                   (next_city != target_cities[1] or state[2] < num_targets)):
                   # Generate the new state
                   new_state = (next_city, state[1] + (1 if next_city == target_cities[0] else 0), state[2] + (1 if next_city == target_cities[1] else 0))
                   # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
   return None


print(a_star())
