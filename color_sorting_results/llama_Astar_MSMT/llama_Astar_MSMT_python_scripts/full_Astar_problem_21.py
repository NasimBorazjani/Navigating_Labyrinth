
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Red', 'Blue', 'Green'),
                   ('Red', 'Blue', 'Red', 'Blue'),
                   ('Red', 'Blue', 'Green', 'Green'))
   num_tubes = 3
   capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Red', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, capacity, colors, visited_costs, queue = initialize()


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
           used_colors  = set(ball for tube in state for ball in tube if ball in colors)
           for color in colors:
               if color not in used_colors:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[0]].append(color)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the capacity of the tubes to calculate the heuristic
                       h = heuristic(new_state, capacity)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, capacity):
   # Relax the capacity constraint to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the number of balls in each tube, penalizing tubes that are not full
   # The heuristic assumes that balls can be moved to a tube if it is not full, even if it is not the correct color, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball to a tube is 1, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as all balls are sorted in the tubes

   h = 0
   for i in range(len(state)):
       h += len(state[i])
   return h


print(a_star())
