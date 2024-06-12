
import heapq


def initialize():
   # Define the adjacency matrix of the graph
   graph = [
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
   ]
   # Define the start city and the cities to visit exactly twice
   start_city = 'T'
   cities_to_visit_twice = ['N', 'W']
   num_cities = len(graph)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], (start_city, 0, 0)))
  
   return graph, start_city, cities_to_visit_twice, num_cities, visited_costs, queue
  
def a_star():
  
   graph, start_city, cities_to_visit_twice, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the cities to visit exactly twice have been visited twice, return the actions taken
       if state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for city_index in range(num_cities):
           if graph[state[0].upper() - 'A', city_index] == 1:
               # Check if the new city is not the start city and has not been visited twice yet
               if chr(city_index + ord('A')) != start_city and chr(city_index + ord('A')) not in cities_to_visit_twice:
                   new_state = (chr(city_index + ord('A')), state[1], state[2])
                   # The cost of the new state is the travel time to get to the new city
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, cities_to_visit_twice)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
              
               # If the new city is one of the cities to visit exactly twice and has not been visited yet
               elif state[1] == 0 and chr(city_index + ord('A')) in cities_to_visit_twice:
                   new_state = (chr(city_index + ord('A')), 1, state[2])
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, cities_to_visit_twice)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
              
               # If the new city is the other city to visit exactly twice and has been visited once
               elif state[2] == 1 and chr(city_index + ord('A')) in cities_to_visit_twice:
                   new_state = (chr(city_index + ord('A')), state[1], 2)
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, cities_to_visit_twice)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, cities_to_visit_twice):
   # The heuristic function can be a simulation of visiting the cities to visit exactly twice greedily, using the next city that has not been visited yet as the next city to visit
   # This heuristic is admissible because it is greedy, always opting for the action that visits the cities to visit exactly twice the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a city to visit exactly twice has been visited, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of times a city to visit exactly twice can be visited is twice, and the cost of reaching the successor node is 1
   h = 0
   for city in cities_to_visit_twice:
       if state[0] == city:
           h += 1
   return h


print(a_star())
