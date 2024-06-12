
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = (137, 29, 70, 138, 47, 64, 87, 16, 0, 0, 0)
   goal_state = (0, 0, 0, 0, 0, 0, 0, 0, 295, 327, 442)
   # The capacities of the jugs and the unlabeled buckets
   capacities = (137, 29, 70, 138, 47, 64, 87, 16)
   # The amounts of water in the unlabeled buckets in the goal state
   goal_amounts = (295, 327, 442)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for i in range(len(capacities)):
           for j in range(3):
               # Check if the action is valid
               if state[i + 8] + capacities[i] <= goal_amounts[j]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i + 8] += capacities[i]
                   new_cost = g + 1
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], tuple(new_state)))
               # Check if the action of removing water from the bucket is valid
               if state[i + 8] - capacities[i] >= 0:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i + 8] -= capacities[i]
                   new_cost = g + 1
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], tuple(new_state)))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraints that the amount of water in a bucket cannot exceed the amount of water in the bucket placed after it, and that the unlabeled buckets cannot be overfilled
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(3):
       h += abs(state[i + 8] - goal_state[i + 8])
   return h


print(a_star())
