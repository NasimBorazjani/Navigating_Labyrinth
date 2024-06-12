
import heapq


def initialize():
   # Define the adjacency matrix of the graph
   adj_matrix = [
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
   ]

   # Encoding other variables of the problem
   num_cities = 11
   start_city = 4
   dest_cities = ['Y', 'A']
   dest_counts = [2, 2]


   visited_costs = {}
   visited_costs[(start_city, dest_cities, dest_counts)] = 0


   queue = [(0, 0, [], (start_city, dest_cities, dest_counts))]
  
   return adj_matrix, num_cities, start_city, dest_cities, dest_counts, visited_costs, queue
  
def a_star():
  
   adj_matrix, num_cities, start_city, dest_cities, dest_counts, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_city, state_dest_cities, state_dest_counts = state


       # If we have visited all destination cities twice, return the path
       if all(count == 2 for count in state_dest_counts):
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for new_city in range(num_cities):
           if adj_matrix[state_city][new_city] == 1:
               # Update the destination cities and their visit counts
               state_dest_cities_new = list(state_dest_cities)
               state_dest_counts_new = list(state_dest_counts)
               for i, city in enumerate(state_dest_cities):
                   if city == new_city:
                       state_dest_counts_new[i] += 1
               # Generate the new state
               new_state = (new_city, state_dest_cities_new, state_dest_counts_new)
               # Cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state_city, new_city, adj_matrix), new_cost, path + [new_city], new_state))
   return None




def heuristic(current_city, new_city, adj_matrix):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current city to the next city
   # The heuristic relaxes the constraints that the travel time between different cities is not the same, that we cannot visit any city more than twice; ie It presumes we can move directly to any given city
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current city to the next city can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, the decrease in the Manhattan distance
   return abs(current_city - new_city)


print(a_star())
