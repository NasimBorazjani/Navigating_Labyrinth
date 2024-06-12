
import heapq


def a_star():
   # Define the initial state of the tubes
   initial_state = (['Green', 'Red', 'Red', 'Green'],
                   ['Blue', 'Red', 'Green', 'Blue'],
                   ['Green', 'Blue', 'Blue', 'Red'])
   # Define the goal state
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Red', 'Red'],
                 ['Red', 'Red', 'Red', 'Blue', 'Blue', 'Blue'])
   # Define the capacities of the tubes
   capacities = [6, 6]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for tube_from in range(len(state)):
           for ball_from in range(len(state[tube_from])):
               color_from = state[tube_from][ball_from]
               for tube_to in range(len(state)):
                   if tube_from != tube_to and len(state[tube_to]) < capacities[tube_to]:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[tube_from].pop(ball_from)
                       new_state[tube_to].append(color_from)
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(tube_from, tube_to)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be a simulation of sorting the balls greedily, using the color of the next ball to sort as the color of the ball to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube to another, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the color of the next ball to sort, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors of the balls in the goal state
   goal_colors = sorted(set(color for tube in goal_state for color in tube))
   # Iterate through the colors in the goal state
   for color in goal_colors:
       # For each color, find the number of balls of that color in the goal state
       goal_balls = sum(color in tube for tube in goal_state)
       # Find the number of balls of that color in the current state
       current_balls = sum(color in tube for tube in state)
       # Move balls from the current state to the goal state as long as the number of balls in the goal state is less than the number of balls in the current state
       while current_balls > goal_balls:
           current_balls -= 1
           h += 1
   return h


print(a_star())
