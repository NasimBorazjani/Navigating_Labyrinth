
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue'], ['Red', 'Blue', 'Green', 'Green']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
   # Define the maximum capacity of the tubes
   capacity = 6


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
                   # Check if the move is valid, ie the to_tube is not full and the color of the ball is not already in the to_tube
                   if len(state[to_tube]) < capacity and state[to_tube][-1] != state[from_tube][from_ball]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[from_tube].pop(from_ball)
                       new_state[to_tube].append(state[from_tube][from_ball])
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                       new_cost = g + 1


                       if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                           visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, using the color of the next ball in the tube as the color of the ball to sort
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 6 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by using the color of the next ball in the tube, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the color of the next ball in the tube
           next_color = state[i][j]
           # Sort the balls in the tube greedily
           while state[i].count(next_color) < len(state[i]):
               # Find the tube with the same color ball
               for k in range(len(state)):
                   if k != i and state[k].count(next_color) < len(state[k]):
                       # Move the ball to the tube
                       state[k].append(next_color)
                       state[i].remove(next_color)
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
