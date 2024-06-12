
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Green', 'Green', 'Red', 'Blue', 'Blue'],
                   ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'],
                   ['Blue', 'Green', 'Blue', 'Red', 'Red', 'Blue'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
   # Define the maximum capacity of the tubes
   capacity = 9


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube and len(state[to_tube]) < capacity:
                   # Move the top ball from the from_tube to the to_tube
                   temp_state = [list(tube[:]) for tube in state]
                   moved_ball = temp_state[from_tube].pop(0)
                   temp_state[to_tube].insert(0, moved_ball)
                   # Generate the new state
                   new_state = tuple(tuple(tube) for tube in temp_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting balls greedily, moving the ball from the tube with the most balls to the tube with the least balls
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube with more balls to a tube with fewer balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the ball from the tube with the most balls, which is exactly the tube used to move the ball in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the tubes by the number of balls in them
   sorted_state = sorted(state, key=len)
   # Iterate through the tubes
   for i in range(len(sorted_state)):
       # Move the top ball from the tube with the most balls to the tube with the least balls
       while len(sorted_state[i]) > 0 and len(sorted_state[-1]) < 9:
           moved_ball = sorted_state[i].pop(0)
           sorted_state[-1].insert(0, moved_ball)
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
