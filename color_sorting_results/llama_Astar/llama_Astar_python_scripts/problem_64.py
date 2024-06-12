
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Blue', 'Red', 'Red', 'Red'],
                   ['Blue', 'Blue', 'Blue', 'Green', 'Green'],
                   ['Red', 'Green', 'Green', 'Green', 'Blue'])
   # Define the goal state
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Red', 'Blue', 'Blue', 'Green'],
                 ['Green', 'Green', 'Green', 'Green', 'Blue', 'Blue', 'Blue', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Green', 'Green', 'Green', 'Green'])
   # Define the capacities of the tubes
   capacities = [8, 8, 8]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube:
                   # Check if the action is valid
                   if len(state[to_tube]) < capacities[to_tube]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the differences between the current state and the goal state
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic is the sum of the differences between the current state and the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != goal_state[i][j]:
               h += 1
   return h


print(a_star())
