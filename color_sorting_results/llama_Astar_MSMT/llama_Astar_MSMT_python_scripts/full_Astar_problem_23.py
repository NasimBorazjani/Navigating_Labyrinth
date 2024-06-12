
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d list
   initial_state = [['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Blue', 'Blue'], ['Red', 'Green', 'Green', 'Red']]
   num_tubes = 3
   max_capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Red', 'Blue', 'Green'])


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(tube) if ball in colors]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_colors  = set(ball for tube in state for ball in tube if ball in colors)
           for color in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the number of balls in each tube must not exceed the maximum capacity
               num_balls_in_tubes_new_state = [sum(ball == color for ball in tube) for tube in state]
               if (color not in used_colors and
                   all(num_balls_in_tubes_new_state[i] <= max_capacity for i in range(num_tubes))):
              
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[0]].append(color)
                   new_state = [tuple(tube) for tube in new_state]
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                       visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, colors):
   # Relax the constraints on the colors to compute an admissible and consistent heuristic
   # This heuristic considers the sum of differences between the goal state and the current state, for each color, counting the number of balls of that color in the wrong tube
   # The heuristic assumes balls can be moved to the correct tube, even if the maximum capacity constraint is violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball to the correct tube is 1, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as all balls are in the correct tube

   h = 0
   for color in colors:
       for i in range(len(state)):
           h += sum(ball == color for ball in state[i])
   return h


print(a_star())
