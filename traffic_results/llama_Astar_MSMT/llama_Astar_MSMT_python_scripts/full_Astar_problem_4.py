
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = (('18', '9', '2', 'x', '9', '14', 'x', '1', 'x'),
               ('3', '14', '18', '7', 'x', '3', 'x', '2', '19'),
               ('6', '18', '20', '3', '13', 'x', '6', '10', 'x'),
               ('20', 'x', '12', '4', '14', '6', 'x', 'x', 'x'),
               ('7', '18', '8', '5', '19', '3', 'x', 'x', '7'),
               ('15', '9', '14', '16', '5', '14', '6', 'x', 'x'),
               ('x', '5', '13', 'x', 'x', '19', 'x', 'x', '2'),
               ('x', 'x', '8', 'x', 'x', 'x', 'x', '17', '12'),
               ('x', '1', 'x', '3', '19', 'x', '2', '18'))
   num_rows = 9
   num_cols = 9
   start = (2, 0)
   end = (5, 6)
   districts = [(0, 2), (3, 4), (5, 8)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new workshop is not visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(start_row <= new_row <= end_row for start_row, end_row in districts):
               # Check if the new state would be valid, ie the new workshop is in the same district as the current workshop
               for district in districts:
                   if district[0] <= new_row <= district[1]:
                       # The new state is valid, generate the new state
                       new_state = (new_row, new_col)
                       # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                       new_cost = g + int(city_map[new_row][new_col])
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                          
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual travel time
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of sqrt(2) (if the new district is 1 row and 1 column away), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to sqrt(2)) + h(n)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
