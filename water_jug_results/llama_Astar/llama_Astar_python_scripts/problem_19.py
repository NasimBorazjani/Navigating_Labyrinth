
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = ((21, 62, 98, 143, 61, 110, 140, 40), (280, 338, 353), (0, 0, 0))
   goal_state = ((0, 0, 0), (0, 0, 0), (280, 338, 353))
  
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
       if state[1] == goal_state[1] and state[2] == goal_state[2]:
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket, or removing water from a bucket to a jug
       for i in range(len(state[0])):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the bucket placed after it
               if state[2][j] + state[0][i] <= state[1][j]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]), list(state[2]))
                   new_state[1][j] += state[0][i]
                   new_state[2][j] += state[0][i]
                   new_state[0][i] = 0
                   new_state = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', state[0][i], j + 1)], new_state))


                   # Generate the new state by removing water from the bucket to the jug
                   new_state = (list(state[0]), list(state[1]), list(state[2]))
                   new_state[0][i] += state[1][j]
                   new_state[1][j] -= state[1][j]
                   new_state[2][j] -= state[1][j]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', state[0][i], j + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amounts of water in the unlabeled buckets and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by at least 1
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the difference between the amounts of water in the two buckets, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the difference between the amounts of water in the two buckets) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
