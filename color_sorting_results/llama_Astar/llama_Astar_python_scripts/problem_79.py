
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'],
                   ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'],
                   ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red'])
   # Define the goal state, where each tube contains balls of only one color
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                 ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
   # Define the maximum capacity of each tube
   capacity = 9


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(len(state)):
           for to_tube in range(len(state)):
               if from_tube != to_tube:
                   # Check if the move is valid, ie if the tube we're moving to has space for another ball
                   if len(state[to_tube]) < capacity:
                       # Perform the move
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to be sorted as the color of the ball to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the color of the next ball to be sorted, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the colors in the goal state
   for color in ['Red', 'Green', 'Blue']:
       # Find the number of balls of the current color in the state
       balls = sum(row.count(color) for row in state)
       # Find the number of balls of the current color in the goal state
       balls_goal = sum(row.count(color) for row in goal_state)
       # Move balls to the goal state greedily
       while balls > balls_goal:
           # Find the tube with the most balls of the current color
           max_balls_tube = max(state, key=lambda tube: tube.count(color))
           # Find the tube with the least balls of the current color
           min_balls_tube = min(state, key=lambda tube: tube.count(color))
           # Move a ball from the tube with the most balls to the tube with the least balls
           max_balls_tube.remove(color)
           min_balls_tube.append(color)
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
