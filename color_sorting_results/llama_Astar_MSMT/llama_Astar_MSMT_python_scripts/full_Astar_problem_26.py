
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Blue', 'Blue', 'Red'),
                   ('Green', 'Green', 'Blue', 'Blue'),
                   ('Green', 'Green', 'Red', 'Red'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Red', 'Blue', 'Green'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(Tube) if ball != 'x']
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the tube to any other tube
       else:
           first_ball_coord = ball_coords[0]
           # The number must be unique and not be present in any other cells of the grid
           used_colors  = set(color for tube in state for color in tube)
           for color in colors:
               # Check if the new state, containing the new color, would be valid; ie the color must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new color
               if (color not in used_colors):
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[color].append(color)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, colors):
   # Relax the constraints on the colors to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the number of balls that are not in their correct color tubes
   # The heuristic assumes that balls can be moved to their correct color tubes, even if the capacity constraint is violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a ball to its correct color tube is 1, which is always greater than or equal to the cost used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as all balls are in their correct color tubes


   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != colors[i]:
               h += 1
   return h


print(a_star())
