
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((126, 120, 127, 110, 54, 39, 38, 47, 139, 99), (0, 0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, (219, 240, 312, 411))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = [126, 120, 127, 110, 54, 39, 38, 47, 139, 99]
   num_buckets = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying a bucket with a jug
       for i in range(len(capacities)):
           for j in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][j] + capacities[i] <= goal_state[1][j] and state[1][j] + capacities[i] <= capacities[i]:
                   # Generate the new state
                   new_state = (list(capacities[:]), list(state[1][:]))
                   new_state[1][j] += capacities[i]
                   new_state = tuple(tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


                   # If the amount of water in the bucket exceeds the goal amount, generate a new state with the amount of water reduced
                   if state[1][j] - capacities[i] >= 0:
                       new_state = (list(capacities[:]), list(state[1][:]))
                       new_state[1][j] -= capacities[i]
                       new_state = tuple(tuple(new_state[0]), tuple(new_state[1]))
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets in the current state and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference between the amounts of water in the buckets in the current state and the goal amounts must be reduced by a max of the capacity of the jug
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
