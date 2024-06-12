
import heapq


def a_star():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((36, 88, 132, 70, 87, 111), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = ((0, 0, 0), (225, 237, 243))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (36, 88, 132, 70, 87, 111)
   # Define the amounts of water in the buckets
   goal_water = (225, 237, 243)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # Check if the current state is the goal state
       if state[1] == goal_water:
           return actions
       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for i in range(len(capacities)):
           for j in range(2):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if j == 0:
                   new_water = list(state[1])
                   new_water[i] += capacities[i]
                   new_water = tuple(new_water)
               else:
                   new_water = list(state[1])
                   new_water[i] -= capacities[i]
                   new_water = tuple(new_water)
               # If the new state is valid
               if all(new_water[k] >= 0 for k in range(i + 1)) and all(new_water[k] <= goal_water[k] for k in range(i + 1)):
                   # Generate the new state
                   new_state = (capacities, new_water)
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_water), new_cost, actions + [(('+', capacities[i]), j)], new_state))
   return None


def heuristic(state, goal_water):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied by at least one action
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal_water[i])
   return h


print(a_star())
