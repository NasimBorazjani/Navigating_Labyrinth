
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Blue', 'Green', 'Red', 'Green', 'Green', 'Red'],
                   ['Green', 'Blue', 'Red', 'Blue', 'Blue', 'Red'],
                   ['Red', 'Green', 'Blue', 'Blue', 'Green', 'Red'])
   # Define the goal state
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'])
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
                       # The cost so far is the number of moves made, as we are trying to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to be sorted repeatedly as long as there's space in the tube
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by using the color of the next ball to be sorted, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the number of balls of each color in the goal state
   colors = sorted(set(color for tube in goal_state for color in tube), key=lambda color: sum(tube.count(color) for tube in goal_state))
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by the number of balls of each color in the goal state
       state[i] = sorted(state[i], key=lambda color: colors.index(color))
       # Sort the balls in the tube greedily using the next color to be sorted
       for color in colors:
           while state[i].count(color) < goal_state[i].count(color) and len(state[i]) < max_capacity:
               state[i].append(color)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
