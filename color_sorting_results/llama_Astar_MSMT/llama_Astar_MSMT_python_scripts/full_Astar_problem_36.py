
import heapq


def initialize():
   # Define the initial state of the game as a 2d tuple
   initial_state = (('Blue', 'Red', 'Red', 'Red'),
                   ('Green', 'Blue', 'Green', 'Green'),
                   ('Blue', 'Blue', 'Green', 'Red'))
   num_tubes = 3
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all tubes containing balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the move is valid, ie if the tube we are moving to has not reached its capacity
               if len(state[to_tube]) < capacity:
                   # Perform the move
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # In the problem statement the tubes are indexed starting from 0, thus must add 1 to the tube indices
                       heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be a simulation of sorting tubes greedily, using the color of the next ball as the color to sort to
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the tubes the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that already has 7 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be added to a tube is by moving balls of the same color, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for tube in state:
       # Sort the tube by color
       tube.sort()
       # Move balls to the next tube as long as it has not reached its capacity
       while len(tube) > 1 and len(state[state.index(tube) + 1]) < capacity:
           # Move the next ball to the next tube
           state[state.index(tube) + 1].append(tube.pop())
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
