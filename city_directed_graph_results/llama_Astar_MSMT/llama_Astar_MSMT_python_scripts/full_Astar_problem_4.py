
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'L'
   destinations = ['D', 'N']
   # Define the number of visits to each destination city
   visits_required = 2
   # Define the number of cities
   num_cities = 10
   # Define the city names
   city_names = ['D', 'E', 'Z', 'R', 'N', 'I', 'K', 'G', 'L', 'B']
   # Define the goal state
   goal_state = (destinations, visits_required)
   # Define the initial state
   initial_state = (start, 0, 0)
   # Initialize the visited_costs dictionary
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize the priority queue
   queue = [(0, 0, [], initial_state)]
  
   return adj_matrix, start, destinations, visits_required, num_cities, city_names, goal_state, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, visits_required, num_cities, city_names, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the path
       if state[0] == goal_state[0] and state[1] == visits_required and state[2] == visits_required:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Generate the new state
               new_state = (i, state[1] + (i in destinations), state[2] + (i in destinations))
               # The cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city name must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, goal_state, city_names), new_cost, actions + [city_names[i]], new_state))
   return None




def heuristic(state, goal, city_names):
   # The heuristic function can be a simulation of moving to the next city with the least travel time to the goal city
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum travel time that can be added to the current city is by moving to the city that is closest to the goal, which is exactly the city used to fill the city in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Find the city with the least travel time to the goal city
   for i in range(len(city_names)):
       if city_names[i] != state[0]:
           h += 1
   return h


print(a_star())
