
import heapq


def a_star():
   # Define the initial state of the problem, as a list of the capacities of the jugs and a list of the amounts of water in the unlabeled buckets
   initial_state = ([19, 42, 18, 127, 106, 32, 22, 137], [0, 0, 0, 0])
   # Define the goal state, as a list of the amounts of water in the unlabeled buckets
   goal_state = [245, 252, 264, 314]
   # Define the capacities of the jugs and the amounts of water in the unlabeled buckets
   capacities, amounts = initial_state
   # Define the maximum amount of water that can be in a bucket
   max_amount = max(amounts)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket or removing water from a bucket to a jug
       for i in range(len(capacities)):
           for j in range(len(amounts)):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the maximum amount and the jug must not be empty
               if amounts[j] + capacities[i] <= max_amount and capacities[i] > 0:
                   # Generate the new state
                   new_state = ([capacities[:i] + [capacities[i] - 1] + capacities[i+1:] for capacities in state[0]], [amounts[:j] + [amounts[j] + 1] + amounts[j+1:] for amounts in state[1]])
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


       for j in range(len(amounts)):
           # Check if the new state would be valid, ie the amount of water in the bucket must not be negative
           if amounts[j] > 0:
               # Generate the new state
               new_state = ([capacities[:i] + [capacities[i] + 1] + capacities[i+1:] for capacities in state[0]], [amounts[:j] + [amounts[j] - 1] + amounts[j+1:] for amounts in state[1]])
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
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be at least 0
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the difference between the amounts of water in the two buckets, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the difference between the amounts of water in the two buckets) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[i])
   return h


print(a_star())
