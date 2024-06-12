
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Red', 'Blue', 'Green', 'Green'],
                   ['Blue', 'Red', 'Green', 'Blue'],
                   ['Green', 'Blue', 'Red', 'Red']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green']]
   # Define the maximum capacity of each tube
   capacity = 7


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves moving a ball from one tube to another
       for from_tube in range(len(state)):
           for from_ball in range(len(state[from_tube])):
               for to_tube in range(len(state)):
                   if from_tube != to_tube and len(state[to_tube]) < capacity:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       ball = new_state[from_tube].pop(from_ball)
                       new_state[to_tube].append(ball)
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of actions taken, as we aim to minimize the number of actions required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, using the color of the next ball in the tube as the color of the ball to be sorted
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 7 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by using the color of the next ball in the tube, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the color of the next ball in the tube
           next_color = state[i][j]
           # Sort the balls in the tube greedily
           while state[i].count(next_color) > 1:
               # Move the ball to the tube with the same color
               for k in range(len(state)):
                   if k != i and state[k].count(next_color) < capacity:
                       state[k].append(next_color)
                       state[i].remove(next_color)
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
