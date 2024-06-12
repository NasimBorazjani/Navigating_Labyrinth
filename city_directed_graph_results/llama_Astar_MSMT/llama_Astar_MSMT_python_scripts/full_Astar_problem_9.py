
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
       [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]
   ]
   # Define the start city and the destination cities
   start = 'C'
   destinations = ['F', 'W']
   # Define the number of visits to each destination city
   visits = 2
   # Define the number of cities
   num_cities = 9
   # Define the city names
   city_names = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
   # Define the initial state
   initial_state = (start, 0, 0)
   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[initial_state] = 0
   queue = [(0, 0, [], initial_state)]
  
   return adj_matrix, start, destinations, visits, num_cities, city_names, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, visits, num_cities, city_names, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_city, visit_f, visit_w = state


       # If we have visited both destination cities exactly twice, and the current city is the start city, return the path
       if visit_f == visits and visit_w == visits and state_city == start:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[city_names.index(state_city)][i] == 1:
               # To generate the new state, we must update the number of visits to the destination cities
               # In the new state, the number of visits to the cities will include all the visits from the current state, as well as the city where we are moving to
               visit_f_new = visit_f
               visit_w_new = visit_w
               if city_names[i] == 'F':
                   visit_f_new += 1
               elif city_names[i] == 'W':
                   visit_w_new += 1
               # Generate the new state
               new_state = (city_names[i], visit_f_new, visit_w_new)
               # Cost of the new state is the travel time to get to the new city, which is the same for all directly connected cities
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state_city, city_names[i]), new_cost, path + [city_names[i]], new_state))
   return None




def heuristic(state_city, city_names):
   # The heuristic function can be a simulation of moving to the next city with the shortest travel time from the current city
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the travel time, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city with a longer travel time, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum travel time that can be added to the current city is by moving to the next city with the shortest travel time, which is exactly the city used to move from the current city in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Find the shortest travel time from the current city to the next city
   for i in range(len(city_names)):
       if adj_matrix[city_names.index(state_city)][i] == 1:
           h += 1
   return h


print(a_star())
