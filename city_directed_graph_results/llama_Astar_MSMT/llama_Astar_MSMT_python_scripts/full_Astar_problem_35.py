
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
       [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]


   # Define the start city 'G' and the destination cities 'L' and 'P'
   start = 'G'
   destinations = ['L', 'P']
   num_cities = len(adj_matrix)
   # Encode the cities as integers for the algorithm
   cities = {city: i for i, city in enumerate(list('AVNQPSEMLHWG'))}


   visited_costs = {}
   visited_costs[(cities[start], 0, 0)] = 0


   queue = [(0, 0, 0, [], (cities[start], 0, 0))]
  
   return adj_matrix, start, destinations, cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, l_visits, p_visits, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and we have visited it twice, return the path
       if state[0] in [cities[dest] for dest in destinations] and (state[1] == 2 or state[2] == 2):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for city in range(num_cities):
           if adj_matrix[state[0]][city] == 1:
               # If the city is a destination city, we must update the number of times we have visited it
               l_visits_new = state[1] + (1 if city == cities[destinations[0]] else 0)
               p_visits_new = state[2] + (1 if city == cities[destinations[1]] else 0)
               # Generate the new state
               new_state = (city, l_visits_new, p_visits_new)
               # Cost of the new state is the travel time to get to the new city, which is always 1
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, destinations, cities), new_cost, l_visits_new, p_visits_new, actions + [list('AVNQPSEMLHWG')[city]], new_state))
   return None




def heuristic(state, destinations, cities):
   # The heuristic function can be a simple sum of the estimated travel times to reach the destination cities
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of reaching the goal state is exactly the cost of reaching the successor node, ie one action
   h = 0
   for dest in destinations:
       h += abs(state[0] - cities[dest])
   return h


print(a_star())
