
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Red', 'Blue', 'Green'),
                   ('Blue', 'Red', 'Blue', 'Green'),
                   ('Blue', 'Green', 'Red', 'Green'))
   num_tubes = 3
   # Define the goal state
   goal_state = (['Red'] * 4, ['Blue'] * 4, ['Green'] * 4)
   # Define the maximum capacity of each tube
   capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, capacity, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we're moving to has space for another ball
                   if len(state[to_tube]) < capacity:
                       # Perform the move
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the balls greedily, using the next color ball repeatedly as long as the tube has space
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is removed from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to the tube is by using the largest color ball that won't cause an overflow, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the frequency of their occurrence in the state
   colors = sorted(set(color for tube in state for color in tube), key=lambda color: -state.count(color))
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by color
       state[i] = sorted(state[i], key=colors.index)
       # Fill the tube with the next color ball repeatedly as long as the tube has space
       for color in colors:
           while state[i].count(color) < capacity and state[i].count(color) < goal[i].count(color):
               state[i].append(color)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
