
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]
   num_cities = 10
   start = 'D'
   goal_cities = ['G', 'Q']
   city_names = ['G', 'P', 'H', 'I', 'J', 'X', 'D', 'V', 'Q', 'L', 'Y']
   city_indices = {city: index for index, city in enumerate(city_names)}
   start_index = city_indices[start]
   goal_indices = [city_indices[city] for city in goal_cities]


   visited_costs = {}
   visited_costs[(start_index, goal_indices)] = 0


   queue = [(0, 0, [], (start_index, goal_indices))]
  
   return adj_matrix, num_cities, start_index, goal_indices, visited_costs, queue
  
def a_star():
  
   adj_matrix, num_cities, start_index, goal_indices, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited each goal city twice, return the path
       if all(state[1][i] == 2 for i in goal_indices):
           return actions


       # Generate all possible actions from the current state, which includes moving to any directly connected city
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie we have not visited the city twice yet
               if state[1][i] < 2:
                   # Generate the new state
                   new_state = (i, list(state[1]))
                   new_state[1][i] += 1
                   # The additional cost of this state is the travel time to get to the new city, which is the same for all directly connected cities
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the distances from the new state to the goal states
                       h = heuristic(new_state, goal_indices)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [city_names[i]], new_state))
   return None




def heuristic(state, goal_indices):
   # The heuristic is the sum of the distances from the current state to the goal states
   # The distance between two cities is the same for directly connected cities
   return sum(1 for i in goal_indices if state[1][i] < 2)


print(a_star())
