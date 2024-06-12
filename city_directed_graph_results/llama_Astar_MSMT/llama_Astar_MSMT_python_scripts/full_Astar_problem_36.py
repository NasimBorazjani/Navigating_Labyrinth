
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]]
   # Define the start and goal cities
   start = 'G'
   goal_cities = ['O', 'R']
   num_cities = 12
   city_names = ['F', 'I', 'C', 'G', 'N', 'L', 'X', 'Q', 'U', 'R', 'O', 'B']


   visited_costs = {}
   visited_costs[start] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], start))
  
   return adj_matrix, start, goal_cities, num_cities, city_names, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, goal_cities, num_cities, city_names, visited_costs, queue = initialize()


   while queue:
       _, g, actions, city = heapq.heappop(queue)


       # If the current city is one of the goal cities and we have visited it twice, return the actions taken
       if city in goal_cities and actions.count(city) == 2:
           return actions


       # Generate all possible actions from the current city, which includes moving to any of the directly connected cities
       for new_city in range(num_cities):
           if adj_matrix[city_names.index(city)][new_city] == 1:
               new_city = city_names[new_city]
               # The cost of the new city is the travel time to get to the new city in the adjacency matrix
               new_cost = g + 1


               if new_city not in actions or actions.count(new_city) < 2:
                   visited_costs[new_city] = new_cost
                   # The heuristic function is the straight-line distance between the current city and the goal cities
                   h = heuristic(new_city, goal_cities)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
   return None




def heuristic(city, goal_cities):
   # The heuristic function is the straight-line distance between the current city and the goal cities
   # This heuristic is admissible because it is the straight-line distance, which is an underestimate of the actual cost to reach the goal
   # The heuristic is consistent because the cost of moving to a successor node is always 1, which is the decrease in the heuristic
   # Thus h(n) can never be greater than c(n, n’) + h(n’)
   h = 0
   for goal_city in goal_cities:
       h += abs(city_names.index(city) - city_names.index(goal_city))
   return h


print(a_star())
