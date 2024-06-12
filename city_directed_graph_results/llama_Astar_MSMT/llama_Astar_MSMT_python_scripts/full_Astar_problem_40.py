
import heapq


def initialize():
   # Define the graph as an adjacency matrix
   graph = [
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
       [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
   ]

   # Define the start city 'F' and the cities to visit twice 'A' and 'R'
   start = 'F'
   visit_twice = ['A', 'R']
   num_cities = len(graph)


   visited_costs = {}
   visited_costs[(start, visit_twice, [])] = 0


   queue = [(0, 0, [], (start, visit_twice, []))]
  
   return graph, start, visit_twice, num_cities, visited_costs, queue
  
def a_star():
  
   graph, start, visit_twice, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       city, visit_twice, visited_cities = state


       # If we have visited all cities and all required cities have been visited twice, return the path
       if len(visited_cities) == num_cities - 1 and all(city in visited_cities for city in visit_twice):
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if graph[city][i] == 1:
               # To generate the new state, we must update the visited_cities list
               visited_cities_new = visited_cities[:]
               if i not in visited_cities:
                   visited_cities_new.append(i)
               elif i in visit_twice:
                   continue
               # Generate the new state
               new_state = (i, visit_twice, visited_cities_new)
               # Cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, visit_twice, graph), new_cost, path + [i], new_state))
   return None




def heuristic(state, visit_twice, graph):
   # The heuristic is the sum of the minimum travel times from the current city to the cities to visit twice, and the cities not yet visited
   # This heuristic is admissible because it is the minimum possible cost to reach the goal state
   # The heuristic is consistent because it never overestimates the cost to reach the goal state
   h = 0
   for i in range(len(graph)):
       if i not in state[2]:
           h += min(graph[state[0]][i], graph[i][state[0]])
   for city in visit_twice:
       h += min(graph[state[0]][city], graph[city][state[0]])
   return h


print(a_star())
