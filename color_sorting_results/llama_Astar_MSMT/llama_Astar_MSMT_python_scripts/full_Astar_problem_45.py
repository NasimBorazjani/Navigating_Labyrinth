
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d list
   initial_state = [['Red', 'Green', 'Green', 'Green'], 
                    ['Blue', 'Red', 'Blue', 'Blue'], 
                    ['Green', 'Red', 'Red', 'Blue']]
   # Define the maximum capacity of the tubes
   capacity = 7
   # Define the goal state, with each tube containing balls of only one color
   goal_state = [['Red'], ['Blue'], ['Green']]
   # The number of balls in the initial state
   num_balls = sum(len(tube) for tube in initial_state)


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, capacity, goal_state, num_balls, visited_costs, queue
  
def a_star():
  
   initial_state, capacity, goal_state, num_balls, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube and len(state[to_tube]) < capacity:
                   # Move the top ball from the from_tube to the to_tube
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = [tube for tube in new_state if tube]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, always moving the ball from the tube with the most different colors to the tube with the least different colors
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is removed from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by moving the ball with the most different colors in the tube, which is exactly the ball used to fill the tube in the heuristic
   h = 0
   for i in range(len(state)):
       for j in range(i + 1, len(state)):
           # Calculate the number of different colors in the tubes
           num_diff_colors = len(set(state[i] + state[j]))
           # If the number of different colors is less than the maximum capacity of the tubes, sort the balls greedily
           if num_diff_colors < capacity:
               h += num_diff_colors
   return h


print(a_star())
