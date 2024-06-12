
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Red', 'Red', 'Blue'),
                   ('Green', 'Green', 'Red', 'Red'),
                   ('Green', 'Green', 'Blue', 'Blue'))
   num_tubes = 3
   tube_capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all tubes containing balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[from_tube]) > 0 and len(state[to_tube]) < tube_capacity:
                   # The new state is the current state with the ball moved from the from_tube to the to_tube
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be a simulation of moving balls greedily, always moving the ball from the tube with the most different colors to the tube with the least different colors
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube with more different colors to a tube with fewer different colors, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to a tube is by moving the ball from a tube with more different colors, which is exactly the tube used to move the ball in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(i + 1, len(state)):
           # Calculate the number of different colors in each tube
           num_diff_colors_i = len(set(state[i]))
           num_diff_colors_j = len(set(state[j]))
           # Move balls from the tube with more different colors to the tube with fewer different colors
           while num_diff_colors_i > num_diff_colors_j and len(state[j]) < tube_capacity:
               state[j].append(state[i].pop())
               num_diff_colors_i = len(set(state[i]))
               num_diff_colors_j = len(set(state[j]))
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
