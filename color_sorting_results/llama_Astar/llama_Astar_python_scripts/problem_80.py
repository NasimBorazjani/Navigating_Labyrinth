
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Blue', 'Red', 'Blue', 'Green', 'Blue', 'Green'],
                   ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red'],
                   ['Green', 'Blue', 'Red', 'Red', 'Red', 'Red'])
   # Define the goal state
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of the tubes
   max_capacity = 9


   visited_costs = {}
   visited_costs[initial_state] = 0


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
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       # Move the ball from the from_tube to the to_tube
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to move
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube that is not the one with the next color to sort, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to the tube with the next color to sort is by moving the balls from the tubes with the next color to sort, which is exactly the number of balls moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the number of balls in the goal state
   colors = sorted(set(color for tube in goal_state for color in tube), key=lambda color: sum(tube.count(color) for tube in goal_state))
   # Iterate through the colors
   for color in colors:
       # Iterate through the tubes
       for tube in state:
           # Count the number of balls of the current color in the tube
           balls = tube.count(color)
           # Move the balls to the tube with the next color to sort
           while balls > 0:
               # Find the tube with the next color to sort
               for next_color in colors:
                   if next_color > color:
                       next_tube = next((tube for tube in state if next_color in tube), None)
                       # Move the ball to the next tube
                       if next_tube and len(next_tube) < max_capacity:
                           next_tube.append(color)
                           balls -= 1
                           h += 1
   return h


print(a_star())
