
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each unlabeled bucket
   initial_state = (52, 55, 84, 135, 136, 47, 139, 76, 0, 0, 0, 0)
   goal_state = (0, 0, 0, 292, 325, 496, 516)
   # The capacities of the jugs and the unlabeled buckets
   capacities = (52, 55, 84, 135, 136, 47, 139, 76)
   # The amount of water in each unlabeled bucket at the goal state
   goal_amounts = (292, 325, 496, 516)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[8:] == goal_state:
           return actions


       # Generate all possible actions from the current state
       for i in range(len(capacities)):
           for j in range(4):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if state[8 + j] + capacities[i] <= state[8 + j + 1]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[8 + j] += capacities[i]
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_amounts), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


                   # If the amount of water in the unlabeled bucket is more than the goal amount, try to remove water from it
                   if state[8 + j] - capacities[i] >= goal_amounts[j]:
                       new_state = list(state)
                       new_state[8 + j] -= capacities[i]
                       new_state = tuple(new_state)
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_amounts), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal_amounts):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amount of water in each unlabeled bucket and the goal amount
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each overage of the goal amount must be corrected by a corresponding underage
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of 2 * capacities[i], which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(4):
       h += abs(state[8 + i] - goal_amounts[i])
   return h


print(a_star())
