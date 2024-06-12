
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Green', 'Red', 'Red', 'Green'),
                   ('Blue', 'Red', 'Green', 'Blue'),
                   ('Green', 'Blue', 'Blue', 'Red'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Green', 'Red', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(reversed(tube)) if ball != 'x']
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball from one tube to another
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_balls  = set(ball for tube in state for ball in tube if ball != 'x')
           for ball in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the tube must not be full
               if (ball not in used_balls and
                   len(state[first_ball_coord[0]]) < 6):
              
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   new_state[first_ball_coord[0]].append(ball)
                   new_state = tuple(tuple(reversed(tube)) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, colors), new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], ball)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic function can be a simulation of moving balls greedily, using the next color ball repeatedly as long as the tube does not overflow
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the largest color ball that won't cause an overflow, which is exactly the ball used to move to the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by their frequency in the state
   colors = sorted(colors, key=lambda color: sum(tube.count(color) for tube in state))
   # Iterate through the tubes
   for i in range(len(state)):
       tube_balls = state[i]
       # Move the balls using the next color ball as long as the tube does not overflow
       for ball in colors:
           while tube_balls.count(ball) < 6 and tube_balls.count(ball) < len(state):
               tube_balls.append(ball)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
