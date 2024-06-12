
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((36, 88, 132, 70, 87, 111), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = ((0, 0, 0), (225, 237, 243))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (36, 88, 132, 70, 87, 111)
   # Define the amounts of water in the buckets
   goal_water = (225, 237, 243)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, goal_water, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, goal_water, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for i in range(len(capacities)):
           for j in range(2):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the next bucket
               if j == 0:
                   new_state = list(state[0])
                   new_state[i] = min(capacities[i], state[1][j] + capacities[i] - state[0][i])
                   new_state = tuple(new_state)
               else:
                   new_state = list(state[0])
                   new_state[i] = max(0, state[1][j] - capacities[i] + state[0][i])
                   new_state = tuple(new_state)
               # The cost so far is the number of actions made, as we aim to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities, goal_water), new_cost, actions + [(('+', capacities[i]), j)], new_state))
   return None


def heuristic(state, goal_state, capacities, goal_water):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[0])):
       h += abs(state[1][i] - goal_water[i])
   return h


print(a_star())
