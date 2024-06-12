
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]
   num_cities = 11
   start_city = 'D'
   goal_cities = ['H', 'Z']
   goal_visits = 2


   visited_costs = {}
   visited_costs[(start_city, goal_visits, goal_visits)] = 0


   queue = [(0, 0, [], (start_city, goal_visits, goal_visits))]
  
   return adj_matrix, num_cities, start_city, goal_cities, goal_visits, visited_costs, queue
  
def a_star():
  
   adj_matrix, num_cities, start_city, goal_cities, goal_visits, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited the goal cities the required number of times, return the actions taken
       if state[0] in goal_cities and state[1] == 0 and state[2] == 0:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0].upper() - 'A'][i] == 1:
               next_city = chr(i + ord('A'))
               # Check if the new city is a goal city
               if next_city in goal_cities:
                   # If we have already visited the goal city once, we can't visit it again
                   if state[1] == 0 and state[2] == 0:
                       continue
                   # Update the number of times we have visited the goal city
                   else:
                       visited_goal_city = next_city == state[0]
                       goal_visits_new = state[1] + (1 if visited_goal_city else 0)
                       goal_visits_other = state[2] + (1 if not visited_goal_city else 0)
               else:
                   goal_visits_new, goal_visits_other = state[1], state[2]


               # Generate the new state
               new_state = (next_city, goal_visits_new, goal_visits_other)
               # The cost of the new state is the travel time to get to the new city in the adjacency matrix
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city we have moved to must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, new_state, adj_matrix), new_cost, actions + [next_city], new_state))
   return None




def heuristic(state, goal_state, adj_matrix):
   # The heuristic function can be a simulation of moving to the goal state greedily, using the next closest city as the next city to move to
   # This heuristic is admissible because it is greedy, always opting for the action that moves us closer to the goal state, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that can be moved in one action is by moving to the closest city, which is exactly the city used to move to the goal in the heuristic
   h = 0
   # Calculate the distances from the current state to the goal state
   distances = [min(abs(ord(state[0].upper()) - ord(city.upper())), abs(ord(city.upper()) - ord(state[0].upper()))) for city in goal_cities]
   # The heuristic is the sum of the distances
   h = sum(distances)
   return h


print(a_star())
