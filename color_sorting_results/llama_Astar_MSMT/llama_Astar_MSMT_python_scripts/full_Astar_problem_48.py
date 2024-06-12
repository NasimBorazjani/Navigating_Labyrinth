
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Blue', 'Blue', 'Red'),
                   ('Blue', 'Green', 'Blue', 'Green'),
                   ('Green', 'Red', 'Green', 'Red'))
   num_tubes = 3
   goal_state = (['Red']*4, ['Blue']*4, ['Green']*4)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls in the tubes are correctly sorted, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[to_tube]) < 7:
                   # Move the ball from the top of the from_tube to the to_tube
                   temp_state = [list(tube[:]) for tube in state]
                   temp_state[to_tube].append(temp_state[from_tube].pop())
                   # Generate the new state
                   new_state = tuple(tuple(tube) for tube in temp_state)
                   # The cost so far is the number of actions taken, as we aim to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of misplaced balls, assuming the goal state has no misplaced balls
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic is the number of misplaced balls, assuming the goal state has no misplaced balls
   h = sum(len(tube) - 1 for tube in state)
   return h


print(a_star())
