
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Red', 'Green', 'Green', 'Blue', 'Green'],
                   ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Green'],
                   ['Blue', 'Red', 'Blue', 'Red', 'Red', 'Green'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
   # Define the maximum capacity of the tubes
   capacity = 9


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
                   # Check if the move is valid, ie the tubes are not full and the color of the ball to be moved is not the same as the color of the topmost ball in the destination tube
                   if len(state[from_tube]) > 0 and len(state[to_tube]) < capacity and state[from_tube][-1] != state[to_tube][-1]:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[from_tube].pop()
                       new_state[to_tube].append(state[from_tube][-1])
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
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the topmost ball from the tube with the most balls, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Check if the color of the ball is not the same as the color of the topmost ball in the destination tube
           if state[i][j] != goal_state[i][j]:
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
