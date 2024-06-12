
import heapq


def initialize():
   # Define the initial state of the 3 tubes as a 2d tuple
   initial_state = (('Green', 'Green', 'Blue', 'Red'),
                   ('Red', 'Blue', 'Green', 'Blue'),
                   ('Green', 'Blue', 'Red', 'Red'))
   num_tubes = 3
   # The maximum capacity of each tube is 7 balls
   tube_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls are correctly sorted in the tubes, return the moves taken to sort them
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # A ball can only be moved if the destination tube is not full
                   if len(state[to_tube]) < tube_capacity:
                       # Move the top ball from the from_tube to the to_tube
                       temp_state = [list(tube[:]) for tube in state]
                       temp_state[to_tube].append(temp_state[from_tube].pop())
                       # Generate the new state
                       new_state = tuple(tuple(tube) for tube in temp_state)
                       # The cost so far is the number of moves made, as the task is to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, new_state):
   # The heuristic is the number of balls in tubes that are not sorted yet
   # This heuristic is admissible because it is always less than or equal to the actual cost of reaching the goal state
   # The heuristic is consistent because it never overestimates the cost to reach the goal state
   h = sum(len(tube) for tube in new_state if len(set(tube)) > 1)
   return h


print(a_star())
