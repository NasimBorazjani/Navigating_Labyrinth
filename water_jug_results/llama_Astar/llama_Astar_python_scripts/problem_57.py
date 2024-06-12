
import heapq


def a_star():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((15, 20, 141, 104, 67), (0, 0, 0, 0))
   goal_state = ((0, 0, 0, 0), (230, 267, 278, 318))
  
   # Encoding other variables given in the problem statement
   capacities = [15, 20, 141, 104, 67]
   num_buckets = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which includes adding water to a bucket from a jug or removing water from a bucket and putting it into a larger jug
       for from_jug in range(len(capacities)):
           for to_bucket in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][to_bucket] + capacities[from_jug] <= state[1][to_bucket + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][to_bucket] += capacities[from_jug]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), g + 1, actions + [('+', from_jug, to_bucket)], new_state))


       for from_bucket in range(num_buckets):
           for to_jug in range(len(capacities)):
               # Check if the new state would be valid, ie the amount of water in the jug must not exceed its capacity
               if state[1][from_bucket] >= capacities[to_jug]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][from_bucket] -= capacities[to_jug]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), g + 1, actions + [('-', to_jug, from_bucket)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the amounts in the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket, as it allows the amounts of water in the buckets to be any values that would result in the goal state
   # It is admissible because it never overestimates the cost to reach the goal state, as each difference between the amounts of water in the buckets in the current state and the goal state must be reduced by a max of the capacity of the largest jug
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the largest jug, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
