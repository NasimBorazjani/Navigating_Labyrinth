
import heapq


def a_star():
   # Define the initial state of the system as a list of the capacities of the unlabeled buckets
   initial_state = [0, 0, 0, 0]
   # Define the goal state of the system as a list of the amounts of water in the unlabeled buckets
   goal_state = [281, 401, 423, 427]
   # Define the capacities of the labeled water jugs
   capacities = [57, 98, 149, 99, 105, 28]
   # Define the maximum capacity of the unlabeled buckets
   max_capacity = max(goal_state)
   # Define the maximum capacity of the labeled water jugs
   max_jug_capacity = max(capacities)


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


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket or removing water from a bucket to a jug
       for i in range(len(capacities)):
           for j in range(len(state)):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the bucket placed after it
               if state[j] + capacities[i] <= state[j + 1] + max_capacity:
                   # Generate the new state
                   new_state = list(state[:])
                   new_state[j] += capacities[i]
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


       for j in range(len(state)):
           # Check if the new state would be valid, ie the amount of water in the bucket must not be negative
           if state[j] - capacities[i] >= 0:
               # Generate the new state
               new_state = list(state[:])
               new_state[j] -= capacities[i]
               new_state = tuple(new_state)
               # The cost so far is the number of actions made, as the task is to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by at least 1
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of 1 (if the moved water is 1), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       h += abs(state[i] - goal[i])
   return h


print(a_star())
