
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Red', 'Blue', 'Green'),
                   ('Blue', 'Blue', 'Red', 'Blue'),
                   ('Red', 'Red', 'Green', 'Green'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Red', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left in the tubes, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, color in enumerate(tube) if color in colors]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The number must be unique and not be present in any other cells of the grid
           used_colors  = set(color for tube in state for color in tube if color in colors)
           for color in colors:
               # Check if the new state, containing the new color, would be valid; ie the color must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new color
               if color not in used_colors:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[0]].append(color)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is the value of the color moved as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, colors):
   # Relax the columns and diagonal sum constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the given and current row sums, for rows with a specified sum value that have at least one unknown number, filling other x with the smallest unique number
   # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the sum of the rows equals their goal sums and there are no unknown numbers to fill in the grid


   # Get colors not used in the state currently
   used_colors = set(color for tube in state for color in tube if color in colors)
   available_colors = sorted(list(colors - used_colors))
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] in colors:
               # If the color is not in the correct tube, count it as a difference
               if i != j:
                   h += 1
           else:
               # If there's an empty spot, greedily fill it with the smallest unique color
               if available_colors:
                   h += 1
   return h


print(a_star())
