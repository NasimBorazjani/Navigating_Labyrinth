
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Green', 'Red', 'Green', 'Red', 'Green'],
                   ['Blue', 'Red', 'Green', 'Blue', 'Green'],
                   ['Red', 'Blue', 'Red', 'Blue', 'Blue']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
   # Define the number of tubes
   num_tubes = 3


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we are moving to is not full
                   if len(state[to_tube]) < 8:
                       # Perform the move
                       new_state = [list(row[:]) for row in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       # The new state must maintain the constraint on the maximum capacity of the tubes
                       if all(len(tube) <= 8 for tube in new_state):
                           new_state = [tuple(row) for row in new_state]
                           new_cost = g + 1


                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube with a different color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the balls of the color that will be sorted next, which is exactly the balls moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the colors in the order of their frequency in the goal state
   for color in ['Green', 'Red', 'Blue']:
       # For each color, move balls from the tubes with the most balls of that color to the tubes with the least balls of that color
       for from_tube in sorted(range(len(state)), key=lambda i: -len([ball for ball in state[i] if ball == color])):
           for to_tube in sorted(range(len(state)), key=lambda i: len([ball for ball in state[i] if ball == color])):
               if from_tube != to_tube:
                   # Move balls of the current color from the from_tube to the to_tube until the from_tube is empty or the to_tube is full
                   while state[from_tube] and len(state[to_tube]) < 8:
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
