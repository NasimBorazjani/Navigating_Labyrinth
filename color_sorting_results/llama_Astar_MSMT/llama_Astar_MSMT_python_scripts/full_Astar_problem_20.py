
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Red', 'Green', 'Blue'),
                   ('Green', 'Green', 'Red', 'Green'),
                   ('Blue', 'Blue', 'Red', 'Blue'))
   num_tubes = 3
   capacity = 6
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Red', 'Green', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all tubes containing balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for tube_from in range(num_tubes):
           for tube_to in range(num_tubes):
               if tube_from != tube_to and len(state[tube_from]) > 0 and len(state[tube_to]) < capacity:
                   # The color of the ball to be moved
                   color = state[tube_from][0]
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[tube_from].pop(0)
                   new_state[tube_to].append(color)
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, colors), new_cost, actions + [(tube_from, tube_to)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic function can be a simulation of moving balls greedily, using the next color ball repeatedly as long as the tube does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that moves the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the largest color ball that won't cause an overflow, which is exactly the ball used to move to the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by their frequency in the tubes
   colors = sorted(colors, key=lambda color: sum(state[tube].count(color) for tube in range(len(state))), reverse=True)
   # Iterate through the tubes
   for tube_from in range(len(state)):
       # Fill the tube with the next color ball repeatedly as long as the tube does not exceed its capacity
       for color in colors:
           while state[tube_from].count(color) > 0 and len(state[tube_from]) < capacity:
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
