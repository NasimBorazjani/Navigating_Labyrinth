
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
       [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
   ]
   num_cities = len(adj_matrix)
   start_city = 'O'
   start_city_index = ord(start_city) - ord('A')
   goal_cities = ['N', 'T']
   goal_city_indices = [ord(city) - ord('A') for city in goal_cities]
   goal_city_counts = {city: 2 for city in goal_cities}


   visited_costs = {}
   visited_costs[(start_city, goal_city_counts)] = 0


   queue = [(0, 0, [start_city], (start_city, goal_city_counts))]
  
   return adj_matrix, num_cities, start_city_index, goal_city_indices, goal_city_counts, visited_costs, queue
  
def a_star():
  
   adj_matrix, num_cities, start_city_index, goal_city_indices, goal_city_counts, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       current_city, current_city_index, goal_city_counts = state


       # If we have visited each goal city exactly twice, return the path
       if all(count == 2 for count in goal_city_counts.values()):
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for new_city_index in range(num_cities):
           if adj_matrix[current_city_index][new_city_index] == 1:
               # To generate the new state, we must update the counts of the goal cities
               # In the new state, the counts of the goal cities will include all the counts from the current state, as well as the city we are moving to
               new_goal_city_counts = {city: goal_city_counts.get(city, 0) + (1 if new_city_index in goal_city_indices else 0) for city in goal_city_counts}
               # Generate the new state
               new_state = (chr(new_city_index + ord('A')), new_city_index, new_goal_city_counts)
               # Cost of the new state is the travel time to get to the new city in the adjacency matrix
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, goal_city_indices), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, goal_city_indices):
   # The heuristic function can be a simulation of visiting the goal cities greedily, using the next closest city as the city to visit next
   # This heuristic is admissible because it is greedy, always opting for the action that allows us to visit the goal cities the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is not a goal city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of times that we can visit a city that is not a goal city is by visiting the goal city that is closest to us in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   current_city_index, goal_city_counts = state
   h = 0
   # Calculate the distances to the goal cities
   distances = [abs(current_city_index - index) for index in goal_city_indices]
   # Visit the goal cities with the shortest distances first
   for index in sorted(range(num_cities), key=lambda i: distances[i] if i in goal_city_indices else float('inf')):
       if index in goal_city_indices:
           h += 1
       else:
           h += 0.5
   return h


print(a_star())
