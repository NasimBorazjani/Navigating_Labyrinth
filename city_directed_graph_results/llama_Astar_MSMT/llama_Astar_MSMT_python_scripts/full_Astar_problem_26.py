
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                 [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]
   # Define the start city and the destination cities
   start_city = 'I'
   dest_cities = ['L', 'W']
   # Define the number of cities
   num_cities = 11


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       current_city, num_visits_L, num_visits_W = state


       # If we have visited both destination cities exactly twice, return our path
       if num_visits_L >= 2 and num_visits_W >= 2:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for new_city_index in range(num_cities):
           # Check if the new city is directly connected to the current city
           if adj_matrix[ord(current_city) - ord('A')][new_city_index] == 1:
               # To generate the new state, we must update the number of times we have visited the destination cities
               # In the new state, the number of times we have visited the destination cities will include all the visits from the current state, as well as the destination city if the new city is one of the destination cities
               num_visits_L_new = num_visits_L
               num_visits_W_new = num_visits_W
               if chr(new_city_index + ord('A')) in dest_cities:
                   if chr(new_city_index + ord('A')) == 'L':
                       num_visits_L_new += 1
                   else:
                       num_visits_W_new += 1
               # Generate the new state
               new_state = (chr(new_city_index + ord('A')), num_visits_L_new, num_visits_W_new)
               # Cost of the new state is the travel time to get to the new city, which is the same for all directly connected cities
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simulation of visiting the destination cities greedily, visiting the nearest city first
   # This heuristic is admissible because it is greedy, always opting for the action that visits the destination cities the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is not a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of times we can visit a city is 2
   h = 0
   # Sort the cities by their distance to the destination cities
   cities = sorted(range(len(state)), key=lambda i: abs(ord(state[0]) - ord(dest_cities[0])) + abs(ord(state[0]) - ord(dest_cities[1])) if chr(i + ord('A')) in dest_cities else float('inf'))
   # Iterate through the cities
   for city_index in cities:
       # Check if we have visited the city twice
       if state[1] == 2 or state[2] == 2:
           break
       # If the city is a destination city and we have not visited it twice, increment the estimated cost to the goal by 1 actions
       elif chr(city_index + ord('A')) in dest_cities:
           h += 1
   return h


print(a_star())
