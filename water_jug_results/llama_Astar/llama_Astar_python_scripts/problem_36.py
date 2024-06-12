
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = (15, 138, 24, 10, 30, 82, 11, 94, 0, 0, 0)
   goal_state = (0, 0, 0, 239, 275, 286)
   # The capacities of the jugs and the unlabeled buckets
   capacities = (15, 138, 24, 10, 30, 82, 11, 94)
   # The amount of water in each unlabeled bucket at the goal state
   goal_amounts = (239, 275, 286)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[9:] == goal_state:
           return actions


       # Generate all possible actions from the current state
       for i in range(len(capacities)):
           for j in range(3):
               # Check if the action is valid
               if state[i + 9] + capacities[i] <= goal_amounts[j]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i + 9] += capacities[i]
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


               # Check if the action is valid
               if state[i + 9] >= capacities[i]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i + 9] -= capacities[i]
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], new_state))


   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amount of water in each bucket and the goal amount of water in each bucket
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(3):
       h += abs(state[9 + i] - goal_state[i])
   return h


print(a_star())
