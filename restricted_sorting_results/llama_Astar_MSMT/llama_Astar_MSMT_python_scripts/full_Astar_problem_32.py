
import heapq


def initialize():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Yellow', 'Blue', 'Yellow', 'Red'], [], [], [], [], ['Blue', 'Green', 'Blue', 'Green', 'Blue'], ['Yellow', 'Black', 'Green', 'Yellow', 'Black'], ['Red', 'Red', 'Red', 'Green', 'Black'])
   # Define the costs of moving a block to each stack
   costs = [5, 8, 1, 6, 8, 2, 1, 8]
   # The goal state is when all blocks are sorted by shade and each stack has 4 blocks of a single shade
   goal_state = (['Black', 'Black', 'Black', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'])

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, costs, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, costs, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       for from_stack in range(len(state)):
           for to_stack in range(len(state)):
               if from_stack != to_stack and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                   # Move the top block from the from_stack to the to_stack
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(state[from_stack][-1])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost of this move is the cost of moving the block to the to_stack
                   new_cost = g + costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic is the sum of the number of misplaced blocks and the sum of the heights of the stacks
   h = 0
   for i in range(len(state)):
       for block in state[i]:
           if block not in goal_state[i]:
               h += 1
   h += sum(len(stack) for stack in state)
   return h


print(a_star())
