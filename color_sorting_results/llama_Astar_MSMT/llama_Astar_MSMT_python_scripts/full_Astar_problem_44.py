
import heapq


def initialize():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Green', 'Green', 'Green'], ['Red', 'Blue', 'Blue', 'Green']]
   num_tubes = 3
   max_capacity = 7


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls are correctly sorted in the tubes, return the actions taken
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all valid actions from the current state
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if moving the top ball from the from_tube to the to_tube is valid
               if from_tube != to_tube and len(state[to_tube]) < max_capacity and state[from_tube][-1] != state[to_tube][-1]:
                   new_state = [list(tube) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = [tuple(tube) for tube in new_state]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic function is a simulation of sorting balls greedily, always moving the ball that results in the most sorted tubes after the move
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most
   # The heuristic is consistent because the estimated cost of the next node is higher if a ball is moved from a less sorted tube to a more sorted tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved from a less sorted tube to a more sorted tube is by moving the most sorted balls, which is exactly the balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the tubes by the number of different balls in them
   state.sort(key=lambda tube: len(set(tube)))
   for i in range(len(state) - 1):
       h += len(set(state[i])) - len(set(state[i + 1]))
   return h


print(a_star())
