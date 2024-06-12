
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Green', 'Blue', 'Red'),
                   ('Red', 'Green', 'Blue', 'Red'),
                   ('Green', 'Red', 'Green', 'Blue'))
   num_tubes = 3
   tube_capacity = 7
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Green', 'Red'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left in tubes, thus we need to get (the coordinates of) the balls to check whether the current state is the goal state
       ball_coords = [(i, j) for i, tube in enumerate(state) for j, ball in enumerate(tuple(reversed(tube))) if ball != 'x']
       if not ball_coords:
           return actions


       # If the state has at least 1 remaining ball, generate all possible actions from the current state, which includes moving the next ball in the grid to any of the other tubes
       else:
           first_ball_coord = ball_coords[0]
           # The ball must be unique and not be present in any other cells of the grid
           used_colors  = set(ball for tube in state for ball in tube if ball != 'x')
           for color in colors:
               # Check if the new state, containing the new ball, would be valid; ie the ball must be unique and the number of balls in the tube must not exceed the tube capacity
               num_balls_in_tube_new_state = len([ball for ball in state[first_ball_coord[0]] if ball != 'x']) - 1 + (first_ball_coord[0] != first_ball_coord[1])
               if (color not in used_colors and
                   num_balls_in_tube_new_state < tube_capacity):
              
                   # Generate the new state
                   new_state = [list(reversed(tube[:])) for tube in state]
                   new_state[first_ball_coord[0]].pop(j)
                   new_state[first_ball_coord[1]].append(color)
                   new_state = tuple(tuple(reversed(tube)) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(first_ball_coord[0], first_ball_coord[1], color)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic function can be a simulation of moving balls greedily, using the color with the largest amount of balls in the tube as the ball to move, until all tubes are sorted
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved from a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to another tube is by using the color with the largest amount of balls in the tube, which is exactly the ball used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the number of balls in each tube for each color
   balls_in_tube = {color: [0 for _ in range(num_tubes)] for color in colors}
   for tube_ind, tube in enumerate(state):
       for ball_ind, ball in enumerate(tuple(reversed(tube))):
           if ball != 'x':
               balls_in_tube[ball][tube_ind] += 1
   # Sort colors by the number of balls in the tube
   sorted_colors = sorted(colors, key=lambda color: sum(balls_in_tube[color]), reverse=True)
   # Move balls from the tube with the most balls of the color to the tube with the least balls of the next color
   for color in sorted_colors:
       max_balls_tube = balls_in_tube[color].index(max(balls_in_tube[color]))
       min_balls_tube = balls_in_tube[sorted_colors[sorted_colors.index(color) + 1]].index(min(balls_in_tube[sorted_colors[sorted_colors.index(color) + 1]]))
       h += abs(max_balls_tube - min_balls_tube)
   return h


print(a_star())
