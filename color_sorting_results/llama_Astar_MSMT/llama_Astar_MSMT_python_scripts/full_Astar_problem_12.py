
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Blue', 'Red', 'Blue'),
                   ('Red', 'Green', 'Green', 'Green'),
                   ('Red', 'Red', 'Blue', 'Green'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Red', 'Green'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls of different colors in the same tube, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(tuple(tube)) if ball in colors]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball of different colors, generate all possible actions from the current state, which includes moving the next ball to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_colors  = set(state[first_ball_coord[0]][first_ball_coord[1]])
           for color in colors:
               if color != used_colors:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]][first_ball_coord[1]] = color
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of balls of different colors in the same tube
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state):
   # The heuristic is the number of balls of different colors in the same tube
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] in colors:
               h += 1
   return h


print(a_star())
