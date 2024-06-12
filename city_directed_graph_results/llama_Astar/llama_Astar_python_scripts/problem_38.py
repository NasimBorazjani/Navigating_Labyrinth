
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
       [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'Q'
   destinations = ['V', 'F']
   # Define the cities in the map
   cities = 'S X Y Q O R D V H J F C'.split()
   # Define the indices of the cities in the adjacency matrix
   city_indices = {city: i for i, city in enumerate(cities)}
   # Define the initial state of the map
   initial_state = (start, 0, 0)
   # Define the goal state of the map
   goal_state = (start, 2, 2)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving to any directly connected city
       current_city, visited_V, visited_F = state
       current_city_index = city_indices[current_city]
       for next_city_index, is_connected in enumerate(adjacency_matrix[current_city_index]):
           if is_connected:
               next_city = cities[next_city_index]
               # Update the visited count of the next city
               if next_city == 'V':
                   visited_V += 1
               elif next_city == 'F':
                   visited_F += 1
               # Generate the new state
               new_state = (next_city, visited_V, visited_F)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic is the sum of the distances from the current state to the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving from one state to another always decreases the heuristic cost of the successor node by a max of 1 (if the moved city is not a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   current_city, visited_V, visited_F = state
   goal_city, goal_visited_V, goal_visited_F = goal_state
   h = 0
   for city in 'S X Y Q O R D V H J F C'.split():
       if city != current_city:
           h += 1
   return h


print(a_star())
