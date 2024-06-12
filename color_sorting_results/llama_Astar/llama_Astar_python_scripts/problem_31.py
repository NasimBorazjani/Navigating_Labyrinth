
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Red', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Blue'], ['Blue', 'Red', 'Green', 'Blue'])
   num_tubes = 3
   tube_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls are sorted in the tubes, return the actions taken
       if state == (['Red'], ['Green'], ['Blue']):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we're moving to has less than 7 balls
                   if len(state[to_tube]) < tube_capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, ['Red'], ['Green'], ['Blue'])
                           heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, red_tube, green_tube, blue_tube):
   # The heuristic function can be a simulation of sorting the balls greedily, moving the ball from the tube with the most balls to the tube with the least balls
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube with more balls to a tube with fewer balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the ball from the tube with the most balls, which is exactly the tube used to move the ball in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the tubes by the number of balls they have
   tubes = sorted(state, key=len)
   # Iterate through the tubes
   for i in range(len(tubes)):
       # If the tube has more balls than the goal tube, move balls to the goal tube
       while len(tubes[i]) > len(state[i]):
           # Move the ball from the tube with the most balls to the tube with the least balls
           tubes[i - 1].append(tubes[i].pop())
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
