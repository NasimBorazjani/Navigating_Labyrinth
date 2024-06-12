
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Green', 'Blue', 'Red'),
                   ('Red', 'Green', 'Blue', 'Red'),
                   ('Green', 'Red', 'Green', 'Blue'))
   num_tubes = 3
   tube_capacity = 7
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Green', 'Red'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls of different colors in the same tube, thus we need to get (the coordinates of) the balls of different colors in the same tube to check whether the current state is the goal state
       for i in range(num_tubes):
           for j in range(i+1, num_tubes):
               if state[i] != state[j] and state[i] in colors and state[j] in colors:
                   # If the current state is the goal state, return the actions taken
                   return actions


       # If the state has at least 1 ball of a different color in the same tube, generate all possible actions from the current state, which includes moving the ball from one tube to another
       else:
           for i in range(num_tubes):
               for j in range(num_tubes):
                   if i != j and state[i] != state[j]:
                       # Check if the new state, containing the moved ball, would be valid; ie the capacity of the tubes must not be exceeded
                       if len(state[i]) < tube_capacity and len(state[j]) < tube_capacity:
                           # Generate the new state
                           new_state = [list(tube[:]) for tube in state]
                           new_state[i].append(new_state[i].pop())
                           new_state[j].append(new_state[i].pop())
                           new_state = tuple(tuple(tube) for tube in new_state)
                           # The additional cost of this state is 1 as we are trying to minimize the number of moves
                           new_cost = g + 1
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is the number of balls of different colors in the same tube, as it is a lower bound on the number of moves required to reach the goal state
                               h = heuristic(new_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(i, j)], new_state))
   return None




def heuristic(state):
   # The heuristic function counts the number of balls of different colors in the same tube
   h = 0
   for i in range(len(state)):
       for j in range(i+1, len(state)):
           if state[i] != state[j]:
               h += 1
   return h


print(a_star())
