
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['8', 'x', '7', '10', 'x', '12', '5', 'x'],
               ['x', 'x', '4', '11', '16', '4', '12', '15', 'x'],
               ['3', 'x', '16', '16', '4', 'x', 'x', 'x', 'x'],
               ['11', '6', '3', '12', '8', '2', '19', '14', 'x'],
               ['20', '18', '19', 'x', '4', '18', 'x', '15', '13'],
               ['8', '15', 'x', '16', '11', 'x', '10', '14', '1'],
               ['x', 'x', 'x', '19', 'x', 'x', 'x', 'x', 'x'],
               ['7', 'x', 'x', 'x', 'x', 'x', '1', '7', '8'],
               ['15', '3', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
   # Define the starting and ending positions of Ben
   start = (5, 0)
   end = (3, 7)
   # Define the districts
   districts = [(0, 3), (4, 4), (5, 8)]


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]
  
   return city_map, start, end, districts, visited_costs, queue
  
def a_star():
  
   city_map, start, end, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and it's in a different district than the current state
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (state[0] + d_row, state[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not an 'x'
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x' and
               any(districts[i][0] <= new_pos[0] < districts[i][1] for i in range(len(districts)) if not (districts[i][0] <= state[0] < districts[i][1]))):
               # The actions is valid, generate the new state
               new_cost = g + int(city_map[new_pos[0]][new_pos[1]])
              
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_pos, end), new_cost, actions + [new_pos], new_pos))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a different district than the current state
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual travel time
   # It's consistent because moving to a workshop in a different district reduces the heuristic cost of the successor node by a max of sqrt(2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to sqrt(2)) + h(n)
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
