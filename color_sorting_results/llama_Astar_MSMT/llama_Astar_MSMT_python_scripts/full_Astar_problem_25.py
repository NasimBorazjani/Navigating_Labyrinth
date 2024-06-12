
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Green', 'Red', 'Red'),
                   ('Blue', 'Blue', 'Blue', 'Blue'),
                   ('Green', 'Red', 'Green', 'Red'))
   num_tubes = 3
   tube_capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Blue', 'Red'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left in the tubes, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(tuple(tube)) if ball != 'x']
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the tubes to any other tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other cells of the tubes
           used_colors  = set(ball for tube in state for ball in tube if ball != 'x')
           for color in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the number of balls in each tube must not exceed the tube capacity
               count_color_new_state = sum(1 for ball in state[first_ball_coord[0]] if ball == color) - 1
               count_color_dest_tube = sum(1 for ball in state[k] if ball == color)
               for dest_tube in range(num_tubes):
                   if dest_tube != first_ball_coord[0]:
                       count_color_dest_tube += 1
                   if (color not in used_colors and
                       count_color_new_state + 1 <= tube_capacity and
                       count_color_dest_tube <= tube_capacity):
                  
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                       new_state[dest_tube].append(color)
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The additional cost of this state is the value of the ball moved as we are trying to minimize the number of moves
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                           h = heuristic(new_state, colors)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color, dest_tube)], new_state))
   return None




def heuristic(state, colors):
   # Relax the constraints on the colors and the number of balls in the tubes to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the goal state and the current state, for each color, counting the number of balls of that color in each tube
   # The heuristic assumes that balls can be moved to any tube to reach the goal state, even if the tube capacity is exceeded, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball is 1, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the number of balls of each color in each tube equals the goal state


   h = 0
   for color in colors:
       for tube in state:
           count_color = sum(1 for ball in tube if ball == color)
           h += abs(count_color)
   return h


print(a_star())
