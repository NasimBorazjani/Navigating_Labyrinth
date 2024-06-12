
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Red', 'Green', 'Red'),
                   ('Blue', 'Blue', 'Red', 'Green'),
                   ('Red', 'Blue', 'Green', 'Blue'))
   num_tubes = 3
   tube_capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Red', 'Blue'])


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


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_colors  = set(ball for tube in state for ball in tube if ball != 'x')
           for color in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the number of balls in each tube must not exceed the tube capacity
               num_balls_in_tubes_new_state = [sum(1 for ball in tube if ball != 'x') for tube in state]
               if (color not in used_colors and
                   num_balls_in_tubes_new_state[first_ball_coord[0]] - 1 + num_balls_in_tubes_new_state[first_ball_coord[1]] + 1 <= tube_capacity):
              
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[1]].append(color)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, colors):
   # Relax the constraints on the columns sums and the diagonal sum to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the goal and current state, for each color, considering the number of balls of that color in each tube
   # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball in the grid is 1, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the sum of the rows equals their goal sums and there are no unknown numbers to fill in the grid


   h = 0
   for color in colors:
       num_balls_in_tubes = [sum(1 for ball in tube if ball == color) for tube in state]
       h += abs(sum(num_balls_in_tubes) - len(color))
   return h


print(a_star())
