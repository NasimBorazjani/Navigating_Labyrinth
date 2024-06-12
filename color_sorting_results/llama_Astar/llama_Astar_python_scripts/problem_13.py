
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Blue', 'Blue', 'Green'],
                   ['Red', 'Green', 'Red', 'Blue'],
                   ['Red', 'Green', 'Blue', 'Red'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Blue', 'Blue', 'Red', 'Red'], [], [])
   # Define the maximum capacity of the tubes
   capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube:
                   # Check if the action is valid
                   if len(state[to_tube]) < capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to sort in the current state
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that is not the correct color for that ball, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to the correct color tube is by moving the balls of the next color to sort, which is exactly the balls moved in the heuristic
   h = 0
   # Sort the colors by the number of balls of that color in the goal state
   colors = sorted(set(sum(tube.count(color) for tube in state) for color in set(sum(tube for tube in state))), key=lambda color: goal_state[0].count(color))
   # Iterate through the colors
   for color in colors:
       # For each color, move the balls of that color to the correct color tube
       for tube in state:
           while color in tube:
               # Find the correct color tube
               for i, correct_tube in enumerate(state):
                   if correct_tube[0] == color:
                       # Move the ball to the correct color tube
                       tube.remove(color)
                       correct_tube.append(color)
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
