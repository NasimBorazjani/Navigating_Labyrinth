
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red']]
   # Define the maximum capacity of the tubes
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
                       # The new state must maintain the constraint on the maximum capacity of the tubes
                       if all(len(tube) <= capacity for tube in new_state):
                           new_state = [tuple(row) for row in new_state]
                           new_cost = g + 1


                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of moving balls greedily, using the color of the next ball in the tube as the color of the ball to move
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to a tube is by moving the balls of the same color, which is exactly the balls moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Find the color of the next ball in the tube
           next_color = state[i][j]
           # Move balls of the same color to the tube
           for k in range(len(state)):
               if k != i:
                   for l in range(len(state[k])):
                       if state[k][l] == next_color:
                           h += 1
   return h


print(a_star())
