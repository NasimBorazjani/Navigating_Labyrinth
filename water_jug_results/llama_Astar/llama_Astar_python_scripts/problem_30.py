
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = (111, 84, 17, 22, 63, 75, 148, 64, 0, 0, 0)
   goal_state = (0, 0, 0, 253, 280, 448)
  
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
       if state[8:] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes filling or emptying each unlabeled bucket with each jug
       for i in range(len(state) - 3):
           for j in range(len(state) - 3):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the bucket placed after it
               if state[i] <= state[i + 1] and state[i] + state[j] <= state[j + 1]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[i], new_state[j + 8] = new_state[j + 8], new_state[i]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', i, j)], tuple(new_state)))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the unlabeled buckets in the current state and the amounts in the goal state
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied by at least one action
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the amount of water moved, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state) - 3):
       h += abs(state[i + 8] - goal[i])
   return h


print(a_star())
