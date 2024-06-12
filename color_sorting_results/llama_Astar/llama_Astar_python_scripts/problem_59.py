
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Blue', 'Red', 'Red', 'Blue', 'Red'],
                   ['Green', 'Blue', 'Blue', 'Red', 'Green'],
                   ['Blue', 'Green', 'Red', 'Green', 'Green'])
   # Define the goal state
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of the tubes
   capacity = 8


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
           for from_ball in range(len(state[from_tube])):
               for to_tube in range(len(state)):
                   # Check if the move is valid
                   if from_tube != to_tube and len(state[to_tube]) < capacity:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[to_tube].append(new_state[from_tube].pop(from_ball))
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of moves made
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the distances of the balls in the tubes from their goal positions
                           h = heuristic(new_state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic is admissible and consistent
   # It is admissible because it is a lower bound on the cost to reach the goal state
   # It is consistent because it never overestimates the cost to reach the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the goal position of each ball
           goal_tube = goal.index(state[i][j])
           h += abs(i - goal_tube) + abs(j - len(state[goal_tube]))
   return h


print(a_star())
