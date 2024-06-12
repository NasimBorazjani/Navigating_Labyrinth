
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = ((58, 18, 19, 47, 86, 75, 119, 34), [0, 0, 0, 0], [234, 331, 343, 379])
  
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
       # The goal state is when all the unlabeled buckets have the specified amounts of water
       if state[1] == state[2]:
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket, or removing water from a bucket to a jug
       for i in range(len(state[0])):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the bucket placed after it
               if state[1][j] < state[1][j + 1] and state[1][j] + state[0][i] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]), list(state[2]))
                   new_state[1][j] += state[0][i]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [('+', state[0][i], j + 1)], new_state))


       for j in range(len(state[1])):
           # Check if the new state would be valid, ie the amount of water in the bucket must not be negative
           if state[1][j] > 0:
               # Generate the new state
               new_state = (list(state[0]), list(state[1]), list(state[2]))
               new_state[1][j] -= min(state[1][j], state[1][j + 1] - state[1][j])
               # The cost so far is the number of actions made, as the task is to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [('-', state[0][i], j + 1)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amounts of water in the unlabeled buckets and the specified amounts of water
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the amount of water in the next bucket
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the amount of water in the next bucket, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - state[2][i])
   return h


print(a_star())
