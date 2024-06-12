
import heapq


def a_star():
   # Define the initial state of the problem, as a list of the capacities of the unlabeled buckets
   initial_state = [0, 0, 0, 0]
   # Define the goal state, as a list of the amounts of water in the unlabeled buckets
   goal_state = [307, 384, 555, 575]
   # Define the capacities of the labeled jugs
   capacities = [146, 45, 136, 13, 148, 17, 42, 137, 141, 31]
   # Define the maximum number of actions allowed
   max_actions = 100


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


       # Generate all possible actions from the current state, which includes adding water to any of the 4 unlabeled buckets from any of the 10 jugs
       for capacity in capacities:
           for i in range(4):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if state[i] + capacity <= (state[i + 1] if i < 3 else 0):
                   # Generate the new state
                   new_state = [state[j] + (capacity if j == i else 0) for j in range(4)]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacity, i + 1)], new_state))


                   # Also consider removing water from the unlabeled bucket
                   if state[i] - capacity >= 0:
                       new_state = [state[j] - (capacity if j == i else 0) for j in range(4)]
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                           visited_costs[tuple(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacity, i + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the capacity of the jugs
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jugs, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = sum(abs(state[i] - goal[i]) for i in range(4))
   return h


print(a_star())
