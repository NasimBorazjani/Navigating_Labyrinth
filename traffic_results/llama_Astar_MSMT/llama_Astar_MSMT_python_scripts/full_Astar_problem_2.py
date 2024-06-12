
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
               ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
               [8, 'x', 2, 5, 6, 12, 9, 10, 7],
               [12, 1, 6, 20, 19, 18, 12, 'x', 14],
               [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
               ['x', 3, 'x', 'x', 'x', 'x', 'x', 4],
               [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
               ['x', 5, 'x', 'x', 'x', 17, 'x', 9, 'x'],
               [13, 16, 8, 15, 'x', 2, 'x', 1, 2]]
   num_rows = 9
   num_cols = 9
   start = (2, 2)
   end = (5, 8)
   districts = [(0, 1), (2, 4), (5, 8)]


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]
  
   return city_map, num_rows, num_cols, start, end, districts, visited_costs, queue
  
def a_star():
  
   city_map, num_rows, num_cols, start, end, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new state is different from the current state
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(start[0] <= new_row <= end[0] <= start[0] + 1 or start[1] <= new_col <= end[1] <= start[1] + 1 for start, end in districts if start[0] <= new_row <= end[0] and start[1] <= new_col <= end[1]):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a different district if the new district is not visited before
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a workshop in a different district reduces the heuristic cost of the successor node by a max of 1 (if the new district is not visited before), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
