
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Red', 'Blue', 'Green'),
                   ('Red', 'Blue', 'Green', 'Red'),
                   ('Blue', 'Green', 'Green', 'Red'))
   num_tubes = 3
   tube_capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Red', 'Green'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the tubes of) the balls to be sorted to check whether the current state is the goal state
       balls_to_sort = [(i, ball) for i, tube in enumerate(state) for j, ball in enumerate(reversed(tube)) if ball != 'x']
       if not balls_to_sort:
           return actions


       # If the state has at least 1 remaining ball to sort, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_to_sort = balls_to_sort[0]
           # The ball must be unique and not be present in any other tubes
           used_balls  = set(ball for tube in state for ball in tube if ball != 'x')
           for tube_to_move in range(num_tubes):
               # Check if the new state, containing the moved ball, would be valid; ie the ball must be unique and the tube must not be full
               if (state[first_ball_to_sort[0]][first_ball_to_sort[1]] not in used_balls and
                   len(state[first_ball_to_sort[0]]) < tube_capacity and
                   len(state[Tube_to_move]) < tube_capacity):
              
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_to_sort[0]].pop(first_ball_to_sort[1])
                   new_state[Tube_to_move].append(first_ball_to_sort[1])
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_to_sort[0], tube_to_move)], new_state))
   return None




def heuristic(state, colors):
   # Relax the columns and diagonal sum constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the given and current row sums, for rows with a specified sum value that have at least one unknown number, filling other x with the smallest unique number
   # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as the sum of the rows equals their goal sums and there are no unknown numbers to fill in the grid


   # Get balls not used in the state currently
   used_balls = set(ball for tube in state for ball in tube if ball != 'x')
   available_balls = sorted(list(colors - used_balls))
   h = 0
   for i in range(len(state)):
       if row_sums[i] is not None:
           row_full = True
           sum_row = sum(int(cell) for cell in state[i] if cell != 'x')
           # Check to see if the row with a target some has any more xs
           for cell in state[i]:
               if cell == 'x':
                   row_full = False
          
           if not row_full:  
               h += row_sums[i] - sum_row
           # Otherwise the sum of a row must equal the target sum or there's no path to reach the goal state from this state. Return math.inf
           else:
               if sum_row != row_sums[i]:
                   return math.inf
      
       # For other rows, greedily fill the x positions with the smallest unique number in the range
       else:
           for cell in state[i]:
               if cell == 'x' and available_balls:
                   h += available_balls.pop(0)
   return h


print(a_star())
