
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'D'
   destinations = ['K', 'Q']
   # Define the number of visits to each destination city
   visits_required = 2
   # Define the number of cities
   num_cities = 9
   # Define the city names
   city_names = ['S', 'U', 'X', 'D', 'I', 'Z', 'R', 'M', 'K', 'Q']
   # Define the initial state
   initial_state = (start, [0] * num_cities, [0, 0])
   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[initial_state] = 0
   queue = [(0, 0, [], initial_state)]
  
   return adj_matrix, start, destinations, visits_required, num_cities, city_names, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, visits_required, num_cities, city_names, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # If the current city is a destination city and the required number of visits has been made, return the path
       if state[0] in destinations and state[1][destinations.index(state[0])] == visits_required:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[city_names.index(state[0])][i] == 1:
               # To generate the new state, we must update the number of visits to the destination cities
               # In the new state, the number of visits to the current city will be incremented by 1
               visits_new = list(state[1])
               if city_names[i] in destinations:
                   visits_new[destinations.index(city_names[i])] += 1
               # Generate the new state
               new_state = (city_names[i], visits_new, state[2])
               # Cost of the new state is the travel time to get to the new city, which is the same for all directly connected cities
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city name of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state[0], destinations, city_names), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, destinations, city_names):
   # The heuristic function can be a simulation of moving to the nearest destination city first, using the city with the shortest path to the destination as the next city to visit
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is further from the destination, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving to a city is by moving to the nearest destination city, which is exactly the city used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the destination cities
   for dest in destinations:
       # Find the city with the shortest path to the destination
       min_distance = float('inf')
       for city in city_names:
           if city != state and city != dest:
               distance = abs(city_names.index(city) - city_names.index(dest))
               if distance < min_distance:
                   min_distance = distance
       # Increment the estimated cost to the goal by the shortest path to the destination
       h += min_distance
   return h


print(a_star())
