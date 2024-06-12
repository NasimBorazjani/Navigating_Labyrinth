
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]]
   # Define the start city and the destination cities
   start = 'Q'
   destinations = ['K', 'Y']
   # Define the number of destinations to visit
   num_visits = 2
   # Define the cities
   cities = ['G', 'J', 'Y', 'Q', 'C', 'D', 'R', 'F', 'K', 'H', 'N']
   # Define the index of the start city
   start_index = cities.index(start)


   visited_costs = {}
   visited_costs[(start_index, 0, 0)] = 0


   queue = [(0, 0, [], (start_index, 0, 0))]
  
   return adj_matrix, start, destinations, num_visits, cities, start_index, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, num_visits, cities, start_index, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_coord, num_visits_k, num_visits_y = state


       # If we have visited both destination cities exactly twice, return the path
       if num_visits_k == num_visits and num_visits_y == num_visits:
           return [cities[i] for i in path]


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(len(cities)):
           if adj_matrix[state_coord][i] == 1:
               # To generate the new state, we must update the number of times we have visited the destination cities
               # In the new state, the number of times we have visited the destination cities will include all the visits from the current state, as well as the destination city we are moving to
               num_visits_k_new = num_visits_k
               num_visits_y_new = num_visits_y
               if cities[i] == 'K':
                   num_visits_k_new += 1
               elif cities[i] == 'Y':
                   num_visits_y_new += 1
               # Generate the new state
               new_state = (i, num_visits_k_new, num_visits_y_new)
               # Cost of the new state is the travel time to get to the new city in the adjacency matrix
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The index of the new city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state_coord, i, adj_matrix), new_cost, path + [i], new_state))
   return None




def heuristic(state_coord, new_city_index, adj_matrix):
   # The heuristic function can be a simulation of moving to the next closest city that has not been visited yet
   # This heuristic is admissible because it is greedy, always opting for the action that moves to the closest city, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that has already been visited, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance to the next closest city that has not been visited yet is by moving to that city, which is exactly the city used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the cities
   for i in range(len(adj_matrix)):
       # Check if there is a direct road from the current city to the city i
       if adj_matrix[state_coord][i] == 1:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
