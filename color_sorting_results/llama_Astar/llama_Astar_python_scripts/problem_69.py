
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Blue', 'Blue', 'Green', 'Blue'],
                   ['Blue', 'Red', 'Red', 'Blue', 'Red'],
                   ['Red', 'Red', 'Green', 'Green', 'Green'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'])
   # Define the capacities of the tubes
   capacities = [8, 8, 8]
   # Define the colors
   colors = ['Green', 'Blue', 'Red']


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
                   if len(state[to_tube]) < capacities[to_tube] and state[from_tube][0] == colors[to_tube]:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[from_tube].pop(0)
                       new_state[to_tube].insert(0, colors[to_tube])
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of moving balls greedily, using the next color ball repeatedly as long as the tube can fit it
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the largest color ball that won't cause an overflow, which is exactly the ball used to move to the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for color in colors:
           # Count the number of balls of the color in the state
           balls = sum(row.count(color) for row in state)
           # Count the number of balls of the color in the goal state
           balls_goal = sum(row.count(color) for row in goal_state)
           # Move the balls greedily to the goal state
           while balls > balls_goal:
               # Find the tube with the color ball
               for tube in range(len(state)):
                   if state[tube][0] == color:
                       # Move the ball to the tube with the most balls of the color
                       for tube_goal in range(len(state)):
                           if len(state[tube_goal]) < capacities[tube_goal] and state[tube_goal][0] == color:
                               state[tube].pop(0)
                               state[tube_goal].insert(0, color)
                               balls -= 1
                               h += 1
   return h


print(a_star())
