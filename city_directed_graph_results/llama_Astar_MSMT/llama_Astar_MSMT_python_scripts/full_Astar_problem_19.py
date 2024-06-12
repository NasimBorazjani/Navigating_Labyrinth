
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]]
   # Define the start city and the destination cities
   start_city = 'E'
   dest_cities = ['Y', 'T']
   # Define the number of visits to each destination city
   num_visits = 2
   # Define the number of cities
   num_cities = 10


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   heappush(queue, (0, 0, [], (start_city, 0, 0)))
  
   return adj_matrix, start_city, dest_cities, num_visits, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_visits, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state meets the requirements of visiting each destination city twice, return the actions taken
       if state[1] == num_visits and state[2] == num_visits:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie if the city is not a destination city or we have not visited it the required number of times
               if (i not in dest_cities or state[1] < num_visits) and (i not in dest_cities or state[2] < num_visits):
                   # Generate the new state
                   new_state = (i, state[1] + (i == dest_cities.index('Y')), state[2] + (i == dest_cities.index('T')))
                   # The cost of the new state is the travel time to get to the new city in the adjacency matrix
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The city must be added to the path
                       heapq.heappush(queue, (new_cost + heuristic(state, dest_cities, num_visits), new_cost, actions + [i], new_state))
   return None




def heuristic(state, dest_cities, num_visits):
   # The heuristic function can be a simulation of visiting the destination cities greedily, using the next closest city as the next city to visit
   # This heuristic is admissible because it is greedy, always opting for the action that visits the destination cities the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is not a destination city, or we visit a destination city less than the required number of times, or we visit a destination city more than the required number of times. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the cities by their distance to the destination cities
   cities = sorted(range(len(state)), key=lambda i: (state[0] - i) % len(state))
   # Iterate through the cities
   for i in cities:
       # Check if we have visited the city the required number of times
       if state[1] == num_visits and state[2] == num_visits:
           break
       # Visit the city
       if i not in dest_cities or state[1] < num_visits:
           state = (i, state[1] + (i == dest_cities.index('Y')), state[2] + (i == dest_cities.index('T')))
           h += 1
   return h


print(a_star())
