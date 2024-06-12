
import heapq


def initialize():
   # Define the adjacency matrix of the graph
   adj_matrix = [[0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0]]
   # Define the start city, end cities and their visit counts
   start_city = 'J'
   end_cities = {'E': 2, 'D': 2}
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start_city, end_cities)] = 0


   queue = [(0, 0, [], (start_city, end_cities))]
  
   return adj_matrix, start_city, end_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, end_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all cities and all destination cities have been visited twice, return the path
       if state[0] == 'F' and all(count == 2 for count in state[1].values()):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie the city has not been visited before or it is a destination city that has not been visited twice yet
               if i not in state[1] or state[1][chr(i + 65)] < 2:
                   # Generate the new state
                   new_state = (chr(i + 65), {city: count + 1 if city == chr(i + 65) else count for city, count in state[1].items()})
                   # The cost of the new state is the travel time to get to the new city, plus the cost of the current state
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the distances from the new city to all destination cities that have not been visited twice yet
                       h = heuristic(new_state, end_cities)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, end_cities):
   # The heuristic is the sum of the distances from the current city to all destination cities that have not been visited twice yet
   # This heuristic is admissible as it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent as it never overestimates the cost to reach the goal state
   return sum(i for city, count in state[1].items() if city in end_cities and count < 2)


print(a_star())
