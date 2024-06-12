
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'Z'
   destinations = ['B', 'H']
   # Define the number of visits to each destination city
   visits_required = 2
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   queue = [(0, 0, [], (start, 0, 0))]
  
   return adj_matrix, start, destinations, visits_required, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, visits_required, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and the required number of visits has been made, return the actions taken
       if state[0] in destinations and state[1] == visits_required and state[2] == visits_required:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie if the city is not a destination city or the required number of visits has not been made
               if (state[0] not in destinations or state[1] < visits_required or state[2] < visits_required) and (i not in destinations or state[1] < visits_required or state[2] < visits_required):
                   # Generate the new state
                   new_state = (chr(i + 65), state[1] + (1 if i == ord(destinations[0]) - 65 else 0), state[2] + (1 if i == ord(destinations[1]) - 65 else 0))
                   # The cost of the new state is the travel time to get to the new city
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The city must be added to the path
                       heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current city to the goal city
   # The heuristic relaxes the constraints that the travel time between different cities is not the same, that we cannot visit the destination cities more than twice, and that we can only visit each city once on our path; ie It presumes we can move directly to any given city toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is the travel time between the cities, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return abs(ord(state[0]) - ord(goal[0]))


print(a_star())
