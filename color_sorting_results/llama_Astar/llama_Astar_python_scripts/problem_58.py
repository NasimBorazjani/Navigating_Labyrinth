
import heapq


def a_star():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Red', 'Blue', 'Green', 'Blue', 'Blue'],
                   ['Green', 'Red', 'Green', 'Red', 'Blue'],
                   ['Blue', 'Green', 'Red', 'Red', 'Green']]
   # Define the goal state of the tubes, where each tube contains balls of only one color
   goal_state = [['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green']]
   # Define the maximum capacity of each tube
   max_capacity = 8


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube and len(state[to_tube]) < max_capacity:
                   # Move the ball from the top of the from_tube to the top of the to_tube
                   temp_state = [list(row[:]) for row in state]
                   temp_state[to_tube].append(temp_state[from_tube].pop())
                   # Generate the new state
                   new_state = [tuple(row) for row in temp_state]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, using the color of the next ball to be sorted repeatedly as long as the tube does not overflow
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the next ball to be sorted, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube greedily
       while len(state[i]) < max_capacity:
           # Find the color of the next ball to be sorted
           next_color = min(set(state[i]) - {state[i][-1]}, key=state[i].count)
           # Move the next ball to the tube with the same color
           for j in range(len(state)):
               if j != i:
                   while state[j].count(next_color) > 0:
                       state[i].append(state[j].pop(state[j].index(next_color)))
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
