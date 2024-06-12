
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Red', 'Green'])
   # Define the goal state
   goal_state = (['Red', 'Red', 'Red', 'Red', 'Blue', 'Blue'], ['Blue', 'Blue', 'Blue', 'Blue', 'Green', 'Green'], ['Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of the tubes
   capacity = 6


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
                   # Check if the action is valid
                   if len(state[to_tube]) < capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another tube that already has 6 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by moving the balls of the next color to sort, which is exactly the balls moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by the number of balls of each color in the goal state
   colors = sorted(set(color for tube in goal_state for color in tube), key=lambda color: sum(tube.count(color) for tube in goal_state))
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by the number of balls of each color in the goal state
       state[i] = sorted(state[i], key=lambda color: colors.index(color))
       # Move the balls to the goal state greedily
       for color in colors:
           while state[i].count(color) < goal_state[i].count(color):
               # Find the tube with the next color to sort
               for j in range(len(state)):
                   if j != i and state[j].count(color) > 0:
                       # Move the ball from the tube with the next color to sort to the current tube
                       state[i].append(state[j].pop(state[j].index(color)))
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
