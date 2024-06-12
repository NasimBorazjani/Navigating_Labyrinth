
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Blue', 'Red', 'Red'),
                   ('Blue', 'Green', 'Green', 'Blue'),
                   ('Green', 'Blue', 'Green', 'Red'))
   num_tubes = 3
   # The maximum capacity of each tube is 7 balls
   tube_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be when each tube contains balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       # Iterating through tubes and their colors
       for tube_from in range(num_tubes):
           for tube_to in range(num_tubes):
               if tube_from != tube_to:
                   # Check if the ball can be moved from the current tube to the other tube, ie the other tube is not full
                   if len(state[tube_to]) < tube_capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       # Remove the ball from the current tube and add it to the other tube
                       new_state[tube_from].pop()
                       new_state[tube_to].append(state[tube_from][-1])
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # In the problem statement the tubes are indexed starting from 0, thus must add 1 to the tube_from and tube_to
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(tube_from+1, tube_to+1)], new_state))
   return None




def heuristic(state):
   # An admissible and consistent heuristic is the number of balls that are not in their correct tubes
   # The heuristic is admissible because it can never overestimate the cost to reach the goal
   # The heuristic is consistent because the cost of moving a ball from one tube to another can never be less than the cost of moving it to a different tube
   return sum(len(set(tube) - {'Blue', 'Red', 'Green'[i]}) for i, tube in enumerate(state))


print(a_star())
