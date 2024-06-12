
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Blue', 'Blue', 'Blue'),
                   ('Red', 'Green', 'Red', 'Red'),
                   ('Green', 'Red', 'Green', 'Blue'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Blue', 'Red'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(tube) if ball in colors]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball to sort, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_balls  = set(ball for tube in state for ball in tube if ball in colors)
           for tube_ind, tube in enumerate(state):
               if tube_ind != first_ball_coord[0]:
                   # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the tube must not be full
                   if (state[first_ball_coord[0]][first_ball_coord[1]] not in used_balls and
                       len(state[first_ball_coord[0]]) < 6 and
                       len(state[tube_ind]) < 6):
                  
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[tube_ind].append(new_state[first_ball_coord[0]].pop(first_ball_coord[1]))
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The additional cost of this state is 1 as we are trying to minimize the number of moves
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                           h = heuristic(new_state, colors)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], tube_ind)], new_state))
   return None




def heuristic(state, colors):
   # Relax the constraints on the columns sums and the diagonal sum to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the number of balls left to sort in the tubes
   # The heuristic assumes that the balls can be sorted in the minimum number of moves, even if the tubes are not full, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball in the grid is 1, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as there are no balls left to sort in the tubes

   h = 0
   for i in range(len(state)):
       for ball in state[i]:
           if ball in colors:
               h += 1
   return h


print(a_star())
