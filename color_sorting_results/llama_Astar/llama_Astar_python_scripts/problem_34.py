
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Red', 'Green', 'Blue', 'Blue'],
                   ['Blue', 'Red', 'Green', 'Red'],
                   ['Green', 'Blue', 'Red', 'Green']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
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
                   # Check if the move is valid, ie if the tube we are moving the ball to is not full
                   if len(state[to_tube]) < capacity:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       ball = new_state[from_tube].pop(from_ball)
                       new_state[to_tube].append(ball)
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to be sorted repeatedly as long as it is possible to place it in a tube
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be placed in a tube is by using the largest number of balls that won't cause an overflow, which is exactly the number of balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency of their occurrence in the state
   colors = sorted(set(color for row in state for color in row), key=lambda color: -state.count(color))
   # Iterate through the colors
   for color in colors:
       # Iterate through the tubes
       for tube in state:
           # Count the number of balls of the current color in the tube
           balls = tube.count(color)
           # Move the balls to the goal state tubes as long as it is possible
           while balls > 0 and any(len(goal_tube) < capacity for goal_tube in goal_state):
               balls -= 1
               h += 1
   return h


print(a_star())
