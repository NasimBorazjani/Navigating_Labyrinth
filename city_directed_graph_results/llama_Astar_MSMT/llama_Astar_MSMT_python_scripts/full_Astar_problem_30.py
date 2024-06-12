
import heapq


def initialize():
   # Define the adjacency matrix of the graph
   adj_matrix = [
       [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
   ]
   # Define the start city and the cities to visit twice
   start = 'G'
   cities_to_visit_twice = ['P', 'H']
   # Define the cities in the graph
   cities = 'S V U W G E H P T Q Z'.split()
   # Define the index of the start city
   start_index = cities.index(start)
   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0
   queue = [(0, 0, [], (start, 0, 0))]
  
   return adj_matrix, start_index, cities_to_visit_twice, cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_index, cities_to_visit_twice, cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all cities and the cities to visit twice have been visited twice, return the actions taken
       if len(actions) == len(cities) - 1 and all(state[1] >= 2 for city in cities_to_visit_twice if city != start):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(len(adj_matrix)):
           if adj_matrix[start_index][i] == 1:
               # Check if the new state is valid, ie if we have visited the city before or if it is one of the cities to visit twice
               if (cities[i] not in actions or (cities[i] in cities_to_visit_twice and state[1] < 2)) and cities[i] != start:
                   # Generate the new state
                   new_state = (cities[i], state[1] + 1 if cities[i] in cities_to_visit_twice else 1, state[2] + 1)
                   # The additional cost of this state is the travel time to get to the new city
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The city must be added to the path
                       heapq.heappush(queue, (new_cost + heuristic(new_state, cities_to_visit_twice), new_cost, actions + [cities[i]], new_state))
   return None




def heuristic(state, cities_to_visit_twice):
   # The heuristic function can be a simulation of visiting the cities greedily, visiting the cities to visit twice first
   # This heuristic is admissible because it is greedy, always opting for the city that leads to the goal state the quickest
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is not one of the cities to visit twice, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of actions that can be taken in the heuristic is by visiting the cities to visit twice first
   h = 0
   # Sort the cities to visit twice by the order of their occurrence in the path
   cities_to_visit_twice = sorted(cities_to_visit_twice, key=lambda city: state[0].index(city) if city in state[0] else float('inf'))
   # Iterate through the cities
   for city in cities_to_visit_twice:
       if state[0].count(city) < 2:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
