
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Green', 'Green', 'Blue', 'Red', 'Green'],
                   ['Red', 'Red', 'Blue', 'Red', 'Blue'],
                   ['Green', 'Blue', 'Blue', 'Red', 'Green']]
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
                       # The new state must maintain the constraint that each tube contains balls of only one color
                       if all(len(set(row)) == 1 for row in new_state):
                           new_state = [tuple(row) for row in new_state]
                           new_cost = g + 1


                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to be sorted repeatedly as long as the tube has space
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 8 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the largest number of balls that won't cause an overflow, which is exactly the number of balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the number of balls in each color in the goal state
   colors = sorted(set(color for row in goal_state for color in row), key=lambda color: goal_state[0].count(color))
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by the number of balls in each color in the goal state
       balls = sorted(state[i], key=lambda color: goal_state[0].count(color))
       # Sort the balls in the tube greedily using the next color to be sorted repeatedly as long as the tube has space
       for color in colors:
           while state[i].count(color) < goal_state[i].count(color) and len(state[i]) < max_capacity:
               state[i].append(color)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
