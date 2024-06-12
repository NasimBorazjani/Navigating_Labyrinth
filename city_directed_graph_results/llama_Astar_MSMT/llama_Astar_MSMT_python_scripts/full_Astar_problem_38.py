
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]


   # Define the starting city and the goal cities
   start = 'Q'
   goals = ['V', 'F']


   # Define the number of cities
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, goals)] = 0


   # The information we must encode for each state includes the current city and the cities left to visit
   initial_state = (start, goals)
   # The cost of the initial state is 0
   queue = [(0, 0, [], initial_state)]
  
   return adj_matrix, num_cities, visited_costs, initial_state, queue
  
def a_star():
  
   adj_matrix, num_cities, visited_costs, initial_state, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       current_city, cities_left = state


       # If we have visited all cities twice, return the path
       if not cities_left:
           return path


       # Generate all possible actions from the current state, which includes moving to any directly connected city
       for i in range(num_cities):
           if adj_matrix[current_city][i] == 1:
               # To generate the new state, we must update the cities left to visit
               # In the new state, the cities left to visit will include all the cities left from the current state, as well as the city we moved to
               cities_left_new = cities_left[:]
               if i in cities_left:
                   cities_left_new[cities_left.index(i)] = cities_left_new[cities_left.index(i)] - 1
               else:
                   cities_left_new.append(i)
               # Generate the new state
               new_state = (i, cities_left_new)
               # Cost of the new state is the cost to reach the current state plus the cost of moving to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city we moved to must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goals), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, goals):
   # The heuristic function is an estimate of the cost to reach the goal from a given state
   # The heuristic is the number of cities left to visit (including the current city) multiplied by the maximum possible cost to visit a city (which is the maximum number of directly connected cities plus one)
   # This heuristic is admissible because it never overestimates the cost to reach the goal and is consistent because it never underestimates the cost to reach the goal
   current_city, cities_left = state
   return len(cities_left) * (max(cities_left) + 1)


print(a_star())
