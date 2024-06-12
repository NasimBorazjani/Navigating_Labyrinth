
import heapq


def a_star():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((76, 135, 134, 19, 10, 30), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, 390, 420, 439)
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (76, 135, 134, 19, 10, 30)
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for i in range(len(capacities)):
           for j in range(1, num_buckets + 1):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][j] + capacities[i] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (capacities, (state[0][i], state[1][0] + capacities[i], state[1][1], state[1][2] - capacities[i], state[1][3], state[1][4]))
                   # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', i, j)], new_state))


                   # If the amount of water in the bucket is more than the amount of water in the next bucket, we can also empty the bucket
                   if state[1][j] - capacities[i] >= state[1][j + 1]:
                       new_state = (capacities, (state[0][i], state[1][0] - capacities[i], state[1][1], state[1][2] + capacities[i], state[1][3], state[1][4]))
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', i, j)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the capacity of the jugs
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jugs
   # Thus h(s) is always less than or equal to c(s, n)(equal to the capacity of the jugs) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[i])
   return h


print(a_star())
