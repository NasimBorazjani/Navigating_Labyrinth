
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Red', 'Blue', 'Blue', 'Red'],
                   ['Green', 'Green', 'Red', 'Red', 'Green'],
                   ['Blue', 'Blue', 'Green', 'Blue', 'Green'])
   # Define the goal state
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of the tubes
   capacity = 8


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
   # The heuristic function can be a simulation of sorting the balls greedily, using the next color ball repeatedly as long as the tube does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is removed from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the largest color ball that won't cause an overflow, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency of their occurrence in the state
   colors = sorted(set(color for tube in state for color in tube), key=lambda color: -state.count(color))
   # Iterate through the colors
   for color in colors:
       # Iterate through the tubes
       for tube in state:
           # Count the number of balls of the current color in the tube
           balls = tube.count(color)
           # Move the balls to the goal state tubes
           for goal_tube in goal_state:
               if goal_tube.count(color) < capacity:
                   h += min(balls, capacity - len(goal_tube))
   return h


print(a_star())
