
import heapq


def initialize():
   # Define the initial state of the game as a 2d tuple
   initial_state = (('Red', 'Blue', 'Blue', 'Green'),
                   ('Green', 'Green', 'Red', 'Blue'),
                   ('Red', 'Red', 'Blue', 'Green'))
   num_tubes = 3
   max_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left in the tubes, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(Tube) if ball]
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the top ball from one tube to another
       else:
           first_ball_coord = ball_coords[0]
           for tube_to in range(num_tubes):
               # Check if the new state, containing the moved ball, would be valid; ie the capacity of the tube must not be exceeded
               if len(state[tube_to]) < max_capacity:
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   # Remove the ball from the current tube
                   new_state[first_ball_coord[0]].pop(first_ball_coord[1])
                   # Add the ball to the new tube
                   new_state[tube_to].append(state[first_ball_coord[0]][first_ball_coord[1]])
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, num_tubes, max_capacity)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_ball_coord[0], tube_to)], new_state))
   return None




def heuristic(state, num_tubes, max_capacity):
   # The heuristic function can be a simulation of moving balls greedily, using the next smallest color ball as the ball to move first
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls with the smallest color, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to another tube is by using the next smallest color ball, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by increasing order
   colors = sorted(set(ball for tube in state for ball in tube))
   # Iterate through the tubes
   for i in range(num_tubes):
       # Sort the balls in the tube by color
       state[i] = sorted(state[i], key=colors.index)
       # Move the balls to the next tube with the smallest color ball
       for ball in state[i]:
           # Check if the tube can be moved to another tube with the smallest color ball
           for tube_to in range(num_tubes):
               if len(state[tube_to]) < max_capacity:
                   h += 1
   return h


print(a_star())
