
import heapq


def initialize():
   # Define the initial state of the tubes
   initial_state = (['Blue', 'Red', 'Green', 'Green'],
                    ['Green', 'Blue', 'Red', 'Blue'],
                    ['Red', 'Green', 'Blue', 'Red'])
   num_tubes = 3
   # Define the goal state
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue'],
                 ['Green', 'Green', 'Green', 'Green'],
                 ['Red', 'Red', 'Red', 'Red'])
   max_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for tube_from in range(num_tubes):
           for tube_to in range(num_tubes):
               if tube_from != tube_to:
                   # Check if moving a ball from the tube_from to the tube_to results in a valid state
                   if len(state[tube_to]) < max_capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[tube_to].append(new_state[tube_from].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, goal_state)
                           heappush(queue, (new_cost + h, new_cost, actions + [(tube_from, tube_to)], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the number of misplaced balls, ie the number of balls that are not in the correct tube
   # The heuristic is admissible because it is always less than or equal to the actual cost of reaching the goal state
   # The heuristic is consistent because the cost of reaching the goal state from any other state is always greater than or equal to the cost of reaching the goal state from the current state
   return sum(1 for tube in state for color in tube if color not in goal[state.index(tube)])


print(a_star())
