
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Red', 'Blue', 'Red'),
                   ('Red', 'Blue', 'Green', 'Blue'),
                   ('Green', 'Green', 'Blue', 'Green'))
   num_tubes = 3
   capacity = 7
   # The colors of the balls in the correct sorted state
   sorted_colors = ['Red', 'Blue', 'Green']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, sorted_colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, capacity, sorted_colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls in the tubes are sorted, return the actions taken
       if state == tuple(sorted_colors[i] for i in range(num_tubes)):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # The ball must not be moved from a full tube
                   if state[from_tube] != 'x':
                       # Generate the new state
                       new_state = list(state)
                       new_state[from_tube] = 'x'
                       new_state[to_tube] = sorted_colors[to_tube]
                       new_state = tuple(new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the number of misplaced balls in the new state
                           h = heuristic(new_state, sorted_colors)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, sorted_colors):
   # The heuristic is the number of misplaced balls in the state
   # The heuristic is admissible as it never overestimates the cost to reach the goal
   # The heuristic is consistent as it is always greater than or equal to the cost of reaching a successor node, and can only decrease by 1 with each action
   return sum(state[i] != sorted_colors[i] for i in range(len(state)))


print(a_star())
