
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
   adjacency_matrix = {
       'U': {'K': 1, 'R': 1},
       'W': {'U': 1, 'J': 1},
       'A': {'H': 1, 'E': 1},
       'J': {'U': 1, 'K': 1, 'E': 1},
       'K': {'W': 1, 'J': 1, 'T': 1},
       'H': {'K': 1, 'E': 1},
       'E': {'R': 1, 'T': 1},
       'X': {'W': 1, 'H': 1},
       'R': {'U': 1, 'W': 1, 'T': 1},
       'T': {'U': 1, 'W': 1, 'R': 1}
   }
   start_city = 'E'
   goal_cities = ['W', 'X']
   num_visits = 2


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], start_city, 0))


   while queue:
       _, g, actions, current_city, visits = heappop(queue)


       # If we have visited both destination cities twice, return the actions taken
       if visits == num_visits and all(goal in actions for goal in goal_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to any connected city
       for next_city in adjacency_matrix[current_city]:
           # Check if the new state would be valid, ie we have not visited the next city before
           if (next_city, visits) not in [(city, v) for city, v in visited_costs]:
               # Generate the new state
               new_visits = visits + 1 if next_city in goal_cities else visits
               new_cost = g + 1
               new_actions = actions + [next_city]
               visited_costs[(next_city, new_visits)] = new_cost
               heappush(queue, (new_cost + heuristic(next_city, goal_cities, num_visits - new_visits), new_cost, new_actions, next_city, new_visits))
   return None


def heuristic(current_city, goal_cities, remaining_visits):
   # The heuristic function is the number of remaining visits multiplied by the number of goal cities not yet visited
   # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes we can visit all remaining goal cities in the minimum number of steps
   # The heuristic is consistent because the cost of reaching the next node is always 1, and the heuristic estimate for the goal state is 0, as there are no remaining goal cities to visit
   return remaining_visits * len([goal for goal in goal_cities if goal != current_city])


print(a_star())
