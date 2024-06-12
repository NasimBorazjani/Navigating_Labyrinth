
import heapq


def a_star():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((145, 101, 17, 75, 102, 129), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = ((0, 0, 0), (260, 287, 413))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (145, 101, 17, 75, 102, 129)
   num_jugs = len(capacities)
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state
       for jug_ind in range(num_jugs):
           for bucket_ind in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_ind] + capacities[jug_ind] <= state[1][bucket_ind + 1]:
                   # Generate the new state
                   new_state = (list(capacities), list(state[1]))
                   new_state[1][bucket_ind] += capacities[jug_ind]
                   new_state = tuple(tuple(x) for x in new_state)
                   # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[jug_ind], bucket_ind + 1)], new_state))


                   # Also consider the action of removing water from the bucket
                   if state[1][bucket_ind] - capacities[jug_ind] >= 0:
                       new_state = (list(capacities), list(state[1]))
                       new_state[1][bucket_ind] -= capacities[jug_ind]
                       new_state = tuple(tuple(x) for x in new_state)
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[jug_ind], bucket_ind + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets in the current state and the amounts in the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a positive amount
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
