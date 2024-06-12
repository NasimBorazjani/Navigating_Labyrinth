
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Green', 'Red', 'Blue', 'Blue'],
                   ['Blue', 'Green', 'Green', 'Red', 'Red'],
                   ['Red', 'Red', 'Blue', 'Green', 'Blue'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red', 'Red'])
   # Define the maximum capacity of the tubes
   max_capacity = 8


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
               if from_tube != to_tube:
                   # Check if the move is valid, ie the tubes are not full and the balls are not of the same color
                   if len(state[from_tube]) > 0 and len(state[to_tube]) < max_capacity and state[from_tube][-1] != state[to_tube][-1]:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the topmost ball in each tube as the sorting key
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the largest number of balls that won't cause an overflow, which is exactly the number of balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the color of the topmost ball in the tube
           color = state[i][j]
           # Find the number of balls of the same color in the tube
           count = len([ball for ball in state[i] if ball == color])
           # Find the number of balls of the same color in the goal state
           goal_count = len([ball for ball in goal_state[i] if ball == color])
           # Increment the estimated cost to the goal by the difference between the current count and the goal count
           h += abs(count - goal_count)
   return h


print(a_star())