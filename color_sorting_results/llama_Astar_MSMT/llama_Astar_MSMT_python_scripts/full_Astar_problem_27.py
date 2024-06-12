
import heapq

def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Red', 'Red', 'Blue'),
                   ('Green', 'Red', 'Red', 'Green'),
                   ('Blue', 'Blue', 'Green', 'Green'))
   # Define the capacity of each tube
   capacity = 7
   # Define the goal state, with each tube containing balls of only one color
   goal_state = (('Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'),
                 ('Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'),
                 ('Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'))
   # Define the possible colors of the balls
   colors = ['Blue', 'Red', 'Green']
   # Create a visited_costs dictionary to store the cost of reaching each state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Create a priority queue to store the states not yet visited, with the initial state as the first element
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, capacity, goal_state, colors, visited_costs, queue
  
def a_star():
  
   initial_state, capacity, goal_state, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which involves moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube:
                   # Check if the new state, with the balls swapped, would be valid
                   if len(state[to_tube]) < capacity:
                       new_state = [list(row[:]) for row in state]
                       # Swap the balls between the tubes
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken, as we aim to minimize the number of actions required to sort the balls
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the differences between the current state and the goal state
                           h = heuristic(new_state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic is the sum of the differences between the current state and the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
