
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Green', 'Green', 'Red'),
                   ('Red', 'Red', 'Green', 'Blue'),
                   ('Green', 'Blue', 'Blue', 'Red'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Green', 'Red'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left in the tubes, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(reversed(tube)) if ball != 'x']
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_colors  = set(color for tube in state for color in tube if color != 'x')
           for color in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the tube must not be full
               if (color not in used_colors and
                   len(state[first_ball_coord[0]]) < 6):
              
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[0]].append(color)
                   new_state = tuple(tuple(reversed(tube)) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of balls not in their correct tubes
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], color)], new_state))
   return None




def heuristic(state):
   # The heuristic is the number of balls not in their correct tubes
   # The heuristic is admissible because it is a lower bound on the number of moves to reach the goal state
   # The heuristic is consistent because the cost of moving a ball to its correct tube is always 1, which is exactly the decrease in the heuristic
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != 'x':
               h += 1
   return h


print(a_star())
