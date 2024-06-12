
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['19', 'x', '17', '14', '3', 'x', '10', '5', '2'],
               ['x', 'x', '1', 'x', 'x', '19', '7', '1'],
               ['16', '12', 'x', '3', '19', '2', '14', '1', '14'],
               ['x', '1', '16', 'x', '12', '3', '13', 'x', '3'],
               ['x', 'x', '7', '19', '10', 'x', '5', 'x', '19'],
               ['5', 'x', 'x', '6', '14', 'x', 'x', '10', '12'],
               ['x', 'x', 'x', 'x', '18', 'x', 'x', '15', '12'],
               ['x', 'x', '16', '8', 'x', '3', '4', 'x', 'x'],
               ['x', 'x', 'x', '16', 'x', 'x', '8', '14', '7'])
   start_workshop = (3, 1)
   end_workshop = (5, 8)
   num_rows = 9
   num_cols = 9
   districts = {0: (0, 3), 1: (4, 4), 2: (5, 8)}


   visited_costs = {}
   visited_costs[start_workshop] = 0


   queue = [(0, 0, [], start_workshop)]
  
   return city_map, start_workshop, end_workshop, num_rows, num_cols, districts, visited_costs, queue
  
def a_star():
  
   city_map, start_workshop, end_workshop, num_rows, num_cols, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_workshop = heapq.heappop(queue)


       # Check if the current workshop is the destination workshop
       if current_workshop == end_workshop:
           return actions


       # Generate all possible actions from the current workshop, which includes moving to any of the 4 neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_workshop = (current_workshop[0] + d_row, current_workshop[1] + d_col)
           # Check if the new workshop is valid, ie within the bounds of the city map, not a closed workshop, and in the same district as the current workshop
           if (0 <= new_workshop[0] < num_rows and 0 <= new_workshop[1] < num_cols and
               city_map[new_workshop[0]][new_workshop[1]] != 'x' and
               districts[current_workshop[0]][0] == districts[new_workshop[0]][0]):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the destination workshop
               new_cost = g + int(city_map[new_workshop[0]][new_workshop[1]])
              
               if new_workshop not in visited_costs or new_cost < visited_costs[new_workshop]:
                   visited_costs[new_workshop] = new_cost
                   # The heuristic is the Manhattan distance to the destination workshop
                   h = abs(new_workshop[0] - end_workshop[0]) + abs(new_workshop[1] - end_workshop[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_workshop], new_workshop))
   return None


print(a_star())
