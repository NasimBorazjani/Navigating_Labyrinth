
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((33, 56, 108, 53, 65, 54, 52, 59), (0, 0, 0))
   goal_state = ((0, 0, 0), (168, 239, 307))
   capacities = [33, 56, 108, 53, 65, 54, 52, 59]
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for jug_capacity in capacities:
           for bucket_num in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_num] + jug_capacity <= state[1][bucket_num + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][bucket_num] += jug_capacity
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num)], new_state))


                   # If the amount of water in the bucket is more than the goal amount, we can empty the bucket
                   if state[1][bucket_num] - jug_capacity >= 0:
                       new_state = (list(state[0]), list(state[1]))
                       new_state[1][bucket_num] -= jug_capacity
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the jug capacity
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the jug capacity, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
