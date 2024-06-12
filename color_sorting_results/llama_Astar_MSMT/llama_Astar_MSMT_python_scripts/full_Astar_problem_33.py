
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d list
   initial_state = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Blue', 'Red']]
   num_tubes = 3
   tube_capacity = 7
   # The goal state is when each tube contains balls of only one color
   goal_state = [['Green'], ['Red'], ['Blue']]


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[to_tube]) < tube_capacity:
                   # Move the ball from the top of the from_tube to the top of the to_tube
                   temp_state = [list(row[:]) for row in state]
                   temp_state[to_tube].append(temp_state[from_tube].pop())
                   new_state = [tuple(row) for row in temp_state]
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball in the from_tube as the color of the ball to sort
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 7 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by moving the ball with the next color to sort, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Sort the balls in the tube greedily, using the next color in the from_tube as the color of the ball to sort
           color = state[i][j]
           for k in range(len(goal)):
               if goal[k][0] == color:
                   while len(state[k]) < tube_capacity and state[i][:]:
                       state[k].append(state[i].pop())
                       h += 1
   return h


print(a_star())
