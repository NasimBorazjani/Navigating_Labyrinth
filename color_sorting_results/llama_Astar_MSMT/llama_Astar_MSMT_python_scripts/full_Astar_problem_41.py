
import heapq


def initialize():
   # Define the initial state as a 2d tuple
   initial_state = (('Green', 'Blue', 'Red', 'Blue'),
                   ('Red', 'Green', 'Blue', 'Green'),
                   ('Red', 'Blue', 'Green', 'Red'))
   num_tubes = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls in the tubes are correctly sorted, return the actions taken
       if state == (('Blue', 'Blue', 'Blue', 'Blue', 'Green', 'Green', 'Green'),
                    ('Red', 'Red', 'Red', 'Red', 'Blue', 'Blue', 'Blue'),
                    ('Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red')):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the move would be valid, ie the to_tube does not have 7 balls and the color of the ball moved is not the same as the color of the ball on top of the to_tube
               if len(state[to_tube]) < 7 and (len(state[to_tube]) == 0 or state[to_tube][-1] != state[from_tube][-1]):
                   # Perform the move
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the tubes greedily, using the next color ball repeatedly as long as the to_tube does not have 7 balls and the color is not the same as the color of the ball on top of the to_tube
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the ball of the same color from the tube with the most balls, which is exactly the ball used to move to the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube
       state[i] = sorted(state[i], key=state[i].count, reverse=True)
       # Move the balls to the goal state
       for ball in state[i]:
           if len(goal[i]) < 7 and (len(goal[i]) == 0 or goal[i][-1] != ball):
               h += 1
   return h


print(a_star())
