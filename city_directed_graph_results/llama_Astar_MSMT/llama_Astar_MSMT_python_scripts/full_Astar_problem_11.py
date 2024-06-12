
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
   ]
   # Define the start city and the destination cities
   start_city = 'Q'
   dest_cities = ['T', 'E']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and we have visited it twice, return the path
       if state[0] in dest_cities and state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Generate the new state
               new_state = (chr(i + 65), state[1] + (1 if state[0] == 'T' else 0), state[2] + (1 if state[0] == 'E' else 0))
               # The cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simulation of moving to the destination cities greedily, using the next closest city as the next destination city
   # This heuristic is admissible because it is greedy, always opting for the action that moves us closer to the destination cities, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is not a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of travel time that can be saved by moving to a destination city is by moving to the closest destination city, which is exactly the city used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Calculate the distances to the destination cities
   dest_distances = [min(abs(ord(state[0]) - ord(dest)) for dest in dest_cities)]
   # Calculate the number of destination cities not visited twice
   num_dest_not_visited = sum(state[i] < 2 for i in range(1, 3))
   # The heuristic is the sum of the distances to the destination cities not visited twice
   h = sum(dest_distances) * num_dest_not_visited
   return h


print(a_star())
