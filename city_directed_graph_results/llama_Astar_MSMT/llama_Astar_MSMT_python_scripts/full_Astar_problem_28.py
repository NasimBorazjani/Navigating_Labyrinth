
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
   ]
   # Define the cities in the same order as the adjacency matrix
   cities = ['A', 'N', 'B', 'M', 'Z', 'O', 'E', 'Q', 'G', 'L', 'P']
   # Define the start city and the cities we need to visit twice
   start_city = 'B'
   visit_twice = ['E', 'N']
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], (start_city, 0, 0)))
  
   return adj_matrix, cities, start_city, visit_twice, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, cities, start_city, visit_twice, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all cities twice, return the actions taken
       if all(visit == 2 for visit in state[1:]):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       city_index = cities.index(state[0])
       for i in range(num_cities):
           if adj_matrix[city_index][i] == 1:
               # Check if the new city is not the start city
               if cities[i] != start_city:
                   # Check if the new city is not one of the cities we need to visit twice
                   if cities[i] not in visit_twice:
                       # Generate the new state
                       new_state = (cities[i],)
                       for visit in state[1:]:
                           if cities[i] == visit_twice[visit_twice.index(cities[i])]:
                               new_state += (visit + 1,)
                           else:
                               new_state += (visit,)
                       new_state = tuple(new_state)
                       # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal state
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, visit_twice)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [cities[i]], new_state))
   return None




def heuristic(state, visit_twice):
   # The heuristic function can be a simulation of visiting the cities greedily, visiting the cities we need to visit twice first
   # This heuristic is admissible because it is greedy, always opting for the action that visits the cities we need to visit twice the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city we do not need to visit twice, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of cities we can visit in the heuristic is by visiting the cities we need to visit twice first
   h = 0
   # Sort the cities by whether they are in the visit_twice list
   cities = sorted(state[0], key=lambda city: city not in visit_twice)
   # Iterate through the cities
   for city in cities:
       # Check if we have visited the city twice
       if state[1:].count(city) == 2:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
