
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
   ]
   # Define the start city, the cities to visit twice, and the goal cities
   start = 'N'
   visit_twice = ['H', 'M']
   goal_cities = list('BFEUZPV')
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, visit_twice[:], goal_cities[:])] = 0


   queue = [(0, 0, [], (start, visit_twice[:], goal_cities[:]))]
  
   return adj_matrix, start, visit_twice, goal_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, visit_twice, goal_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all goal cities and have visited the cities to visit twice twice, we have found the shortest path
       if not goal_cities and not visit_twice:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0].index(i)][i] == 1:
               # If the city is in the list of cities to visit twice, remove it from the list
               if i in map(lambda x: x.index(i), visit_twice):
                   visit_twice_new = [city for city in visit_twice if city[i] != 'x']
               # If the city is in the list of goal cities, remove it from the list
               elif i in map(lambda x: x.index(i), goal_cities):
                   goal_cities_new = [city for city in goal_cities if city[i] != 'x']
               # If the city is neither in the list of cities to visit twice nor in the list of goal cities, continue
               else:
                   continue
               # Generate the new state
               new_state = (state[0], visit_twice_new, goal_cities_new)
               # The additional cost of this state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the distances from the current city to the cities to visit twice and the goal cities
                   h = heuristic(new_state, adj_matrix)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [i], new_state))
   return None




def heuristic(state, adj_matrix):
   # The heuristic is the sum of the distances from the current city to the cities to visit twice and the goal cities
   h = 0
   for i in range(len(state[0])):
       if state[0][i] != 'x':
           h += 1
   return h


print(a_star())
