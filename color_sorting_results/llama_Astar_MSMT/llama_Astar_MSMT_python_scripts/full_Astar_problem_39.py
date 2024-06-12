
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d list
   initial_state = [['Red', 'Green', 'Blue', 'Red'],
                    ['Blue', 'Red', 'Blue', 'Green'],
                    ['Green', 'Red', 'Blue', 'Green']]
   num_tubes = 3
   tube_capacity = 7


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls are correctly sorted in the tubes, return the moves taken
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[to_tube]) < tube_capacity:
                   # Move the ball from the top of the from_tube to the top of the to_tube
                   temp_state = [list(tube[:]) for tube in state]
                   temp_state[from_tube].pop()
                   temp_state[to_tube].append(state[from_tube][-1])
                   # Generate the new state
                   new_state = [tuple(tube) for tube in temp_state]
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, new_state):
   # The heuristic function can be the number of misplaced balls in the new state
   # This heuristic is admissible because it is always less than or equal to the actual cost to reach the goal
   # The heuristic is consistent because it is always less than or equal to the cost of reaching the successor node
   h = sum(state[i][-1] != new_state[i][-1] for i in range(len(state)))
   return h


print(a_star())
