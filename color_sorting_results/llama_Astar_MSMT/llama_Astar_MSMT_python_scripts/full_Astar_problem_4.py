
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Red', 'Blue', 'Blue'),
                   ('Red', 'Blue', 'Red', 'Green'),
                   ('Green', 'Blue', 'Green', 'Green'))
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
           for tube_ind in range(num_tubes):
               # Check if the new state, containing the moved ball, would be valid; ie the tube must not be full
               if len(state[tube_ind]) < 6:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[tube_ind].append(new_state[first_ball_coord[0]].pop(first_ball_coord[1]))
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of balls not in their correct tubes
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], tube_ind)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic is the number of balls not in their correct tubes
   # This heuristic is admissible because it is a lower bound on the number of moves required to reach the goal state
   # The heuristic is consistent because the cost of moving a ball to its correct tube is always 1, which is exactly the decrease in the heuristic value
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != 'x':
               # Check if the ball is in its correct tube
               if state[i][j] == state[i][0]:
                   h += 1
   return len(state) - h


print(a_star())
