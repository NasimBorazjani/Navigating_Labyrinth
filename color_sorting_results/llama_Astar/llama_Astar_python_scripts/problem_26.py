
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Blue', 'Blue', 'Red'],
                   ['Green', 'Green', 'Blue', 'Blue'],
                   ['Green', 'Green', 'Red', 'Red'])
   # Define the goal state
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of the tubes
   capacity = 7


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




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube that already has a ball of the same color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving a ball of the color that is the most common in the remaining tubes, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency in the state
   colors = sorted(set(color for tube in state for color in tube), key=lambda color: sum(tube.count(color) for tube in state), reverse=True)
   # Iterate through the colors
   for color in colors:
       # For each color, move the balls to the tubes in the goal state
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if state[from_tube].count(color) > 0 and goal_state[to_tube].count(color) > 0:
                   h += min(state[from_tube].count(color), goal_state[to_tube].count(color) - len(state[to_tube]))
   return h


print(a_star())
