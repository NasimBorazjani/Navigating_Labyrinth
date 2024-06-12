
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Green', 'Red', 'Green', 'Blue', 'Red'],
                   ['Red', 'Green', 'Red', 'Blue', 'Blue'],
                   ['Green', 'Blue', 'Red', 'Green', 'Blue']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
   # Define the maximum capacity of each tube
   max_capacity = 8


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we are moving to has space for another ball
                   if len(state[to_tube]) < max_capacity:
                       # Perform the move
                       new_state = [list(row[:]) for row in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       # The new state must maintain the constraint on the maximum capacity of the tubes
                       if all(len(row) <= max_capacity for row in new_state):
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
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube with a different color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the balls of the next color to sort, which is exactly the balls moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the number of balls of that color in the initial state
   colors = sorted(set(color for row in state for color in row), key=lambda color: sum(row.count(color) for row in state))
   # Iterate through the colors
   for color in colors:
       # For each color, move the balls of that color to the tubes containing balls of that color
       for i in range(len(state)):
           # Move the balls of the color from the tube to the tubes containing balls of that color
           while state[i].count(color) > 0:
               # Find the tube with the fewest balls of that color
               min_balls = min(row.count(color) for row in state)
               for j in range(len(state)):
                   if state[j].count(color) == min_balls:
                       # Move the ball to the tube with the fewest balls of that color
                       state[j].append(state[i].pop(state[i].index(color)))
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
