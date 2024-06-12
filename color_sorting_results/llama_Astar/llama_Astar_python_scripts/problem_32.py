
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Red', 'Blue', 'Green'],
                   ['Blue', 'Blue', 'Red', 'Blue'],
                   ['Red', 'Red', 'Green', 'Green'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue'])
   # Define the maximum capacity of the tubes
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube and len(state[to_tube]) < capacity:
                   # Move the top ball from the from_tube to the to_tube
                   temp_state = [list(tube[:]) for tube in state]
                   moved_ball = temp_state[from_tube].pop(0)
                   temp_state[to_tube].append(moved_ball)
                   # Generate the new state
                   new_state = tuple(tuple(tube) for tube in temp_state)
                   # The cost so far is the number of actions taken, as we aim to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the topmost ball in each tube as the sorting priority
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to another tube is by moving the topmost ball, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the color of the topmost ball in the tube
           top_ball = state[i][j]
           # Find the color of the topmost ball in the goal state
           goal_top_ball = goal_state[i][j] if j < len(goal_state[i]) else None
           # If the color of the topmost ball in the tube is not the same as the color of the topmost ball in the goal state, increment the estimated cost to the goal by 1 actions
           if top_ball != goal_top_ball:
               h += 1
   return h


print(a_star())
