
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Green', 'Blue', 'Red', 'Red', 'Blue'],
                   ['Green', 'Red', 'Green', 'Green', 'Blue', 'Red'],
                   ['Green', 'Blue', 'Green', 'Blue', 'Blue', 'Red'])
   # Define the goal state
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
   # Define the capacities of the tubes
   capacities = [9, 9, 9]
   # Define the number of balls
   num_balls = 6


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
                   if len(state[to_tube]) < capacities[to_tube]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, using the next color ball repeatedly as long as the tube has space
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is removed from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the next color ball, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency of their occurrence in the goal state
   colors = sorted(set(color for tube in goal_state for color in tube), key=lambda color: goal_state[0].count(color), reverse=True)
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by the frequency of their occurrence in the goal state
       state[i] = sorted(state[i], key=lambda color: goal_state[0].count(color), reverse=True)
       # Sort the balls in the tube greedily using the next color ball repeatedly as long as the tube has space
       for color in colors:
           while state[i].count(color) < goal_state[i].count(color) and len(state[i]) < capacities[i]:
               state[i].append(color)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
