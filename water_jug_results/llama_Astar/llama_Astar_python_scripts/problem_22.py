
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = (16, 124, 57, 40, 99, 45, 72, 98, 0, 0, 0)
   goal_state = (0, 0, 0, 263, 341, 360)
   # The capacities of the jugs and the unlabeled buckets
   capacities = (16, 124, 57, 40, 99, 45, 72, 98)
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[9:] == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the unlabeled buckets with the jugs
       for i in range(len(capacities)):
           for j in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the next bucket
               if state[9 + j] + capacities[i] <= state[9 + min(j + 1, num_buckets - 1)]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i] = capacities[i]
                   new_state[9 + j] += capacities[i]
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], tuple(new_state)))


                   # If the amount of water in the bucket exceeds the goal amount, generate the new state with the amount of water reduced
                   if state[9 + j] - capacities[i] >= goal_state[j]:
                       new_state[9 + j] -= capacities[i]
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], tuple(new_state)))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the unlabeled buckets and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each overfilled bucket must be emptied at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(goal_state)):
       h += abs(state[9 + i] - goal_state[i])
   return h


print(a_star())
