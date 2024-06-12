
import heapq


def initialize():
   # Define the initial state of the tubes, with the colors represented as strings
   initial_state = (['Blue', 'Green', 'Green', 'Blue'],
                   ['Red', 'Blue', 'Green', 'Green'],
                   ['Red', 'Red', 'Red', 'Blue'])
   num_tubes = 3
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Green', 'Red'])
   # The maximum capacity of each tube
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, colors, capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, colors, capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all balls are sorted in the tubes, return the actions taken
       if sorted(state) == [['Blue'], ['Green'], ['Red']]:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[to_tube]) < capacity:
                   # Move the top ball from the from_tube to the to_tube
                   new_state = [list(tube[:]) for tube in state]
                   new_state[from_tube].pop(0)
                   new_state[to_tube].insert(0, state[from_tube][0])
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, ['Blue', 'Green', 'Red'])
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of moving the balls greedily, moving the ball with the color that is not in its correct tube
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube that is not its correct tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving a ball to the tube that is not its correct tube, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       # Move balls from the tube to the correct tube, if the tube is not already sorted
       if state[i] != [goal[i]]:
           h += 1
   return h


print(a_star())
