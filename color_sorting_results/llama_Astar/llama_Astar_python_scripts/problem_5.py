
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Blue', 'Blue', 'Blue'],
                   ['Red', 'Green', 'Red', 'Red'],
                   ['Green', 'Red', 'Green', 'Blue'])
   # Define the goal state
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'])
   # Define the capacities of the tubes
   capacities = [6, 6, 6]
   # Define the colors
   colors = ['Blue', 'Green', 'Red']


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
                   # Check if the top ball in the from_tube can be moved to the to_tube
                   if state[from_tube][0] != state[to_tube][-1] and len(state[to_tube]) < capacities[to_tube]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[from_tube].pop(0)
                       new_state[to_tube].append(state[from_tube][0])
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of moving balls greedily, using the next color ball repeatedly as long as the color of the ball is not the same as the color of the topmost ball in the to_tube
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 6 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by using the largest ball that won't cause an overflow, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           for k in range(len(colors)):
               if state[i][j] != colors[k]:
                   # Move the ball to the tube with the same color
                   for tube in range(len(state)):
                       if tube != i and len(state[tube]) < capacities[tube]:
                           h += 1
   return h


print(a_star())
