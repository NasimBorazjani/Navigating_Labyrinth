
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Green', 'Green', 'Blue'),
                   ('Blue', 'Red', 'Red', 'Red'),
                   ('Blue', 'Green', 'Green', 'Blue'))
   num_tubes = 3
   # Define the goal state
   goal_state = (('Red', 'Red', 'Red', 'Red'),
                 ('Green', 'Green', 'Green', 'Green'),
                 ('Blue', 'Blue', 'Blue', 'Blue'))
   tube_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we are moving to has less than 7 balls
                   if len(state[to_tube]) < tube_capacity:
                       # Perform the move
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be the sum of the differences between the number of balls of each color in the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if a ball is moved from a tube with more balls of a certain color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to a tube with fewer balls of a certain color is by moving one ball, which is exactly the number of balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for color in set(state[i]):
           h += abs(len([ball for ball in state[i] if ball == color]) - len([ball for ball in goal[i] if ball == color]))
   return h


print(a_star())
