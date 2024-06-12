
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Red', 'Green', 'Red'],
                   ['Blue', 'Blue', 'Red', 'Green'],
                   ['Red', 'Blue', 'Green', 'Blue'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
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
           for from_ball in range(len(state[from_tube])):
               color = state[from_tube][from_ball]
               for to_tube in range(len(state)):
                   if to_tube != from_tube and len(state[to_tube]) < capacity and state[to_tube][-1:] != [color]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[from_tube].pop(from_ball)
                       new_state[to_tube].append(color)
                       new_state = tuple(tuple(row) for row in new_state)
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
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is removed from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the next color ball, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency of their occurrence in the state
   colors = sorted(set(color for tube in state for color in tube), key=lambda color: -state.count(color))
   # Iterate through the tubes
   for i in range(len(state)):
       for color in colors:
           # Fill the tube with the next color ball repeatedly as long as the tube does not exceed its capacity
           while len(state[i]) < capacity and state[i][-1:] != [color]:
               h += 1
   return h


print(a_star())
