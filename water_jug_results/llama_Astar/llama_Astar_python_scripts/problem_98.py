
import heapq


def a_star():
   # Define the initial state of the problem, as a list of the capacities of the unlabeled buckets
   initial_state = [0, 0, 0, 0]
   # Define the goal state, as a list of the amounts of water in the unlabeled buckets
   goal_state = [272, 439, 458, 590]
   # Define the capacities of the labeled jugs
   capacities = [137, 100, 82, 25, 21, 101, 118, 117, 26, 131]
   # Define the maximum capacity of the unlabeled buckets
   max_capacity = max(goal_state)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes adding water to any of the unlabeled buckets from any of the jugs
       for i in range(len(capacities)):
           for j in range(len(state)):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the max_capacity and the jug must not be empty
               if state[j] + capacities[i] <= max_capacity and capacities[i] > 0:
                   # Generate the new state
                   new_state = [state[k] + capacities[i] if k == j else state[k] for k in range(len(state))]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


                   # Generate the new state by removing water from the bucket
                   new_state = [state[k] - capacities[i] if k == j else state[k] for k in range(len(state))]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the max_capacity, as it never overestimates the cost to reach the goal
   # It is consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the amount of water moved, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       h += abs(state[i] - goal[i])
   return h


print(a_star())
