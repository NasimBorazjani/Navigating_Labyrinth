
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Red', 'Red', 'Green'),
                   ('Blue', 'Green', 'Green', 'Blue'),
                   ('Blue', 'Red', 'Green', 'Blue'))
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Red', 'Green', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort, thus we need to get (the coordinates of) the balls to sort in the current state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(Tube) if ball in colors]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball to sort, generate all possible actions from the current state, which includes moving the next ball in the tubes to another tube
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other tubes
           used_balls  = set(ball for tube in state for ball in tube if ball in colors)
           for ball in colors:
               if ball not in used_balls:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   # Add the ball to the destination tube
                   new_state[first_ball_coord[0]].append(ball)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], ball)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be a simulation of moving balls greedily, using the next smallest ball repeatedly as long as the balls can be moved
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 7 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by moving the ball to the tube with the least balls, which is exactly the tube used to move the ball in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the tubes
   for i in range(len(state)):
       tube_balls = state[i]
       # Move the balls to the tubes with the least balls
       for ball in colors:
           while len(state[i]) < 7 and ball in tube_balls:
               tube_balls.remove(ball)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
