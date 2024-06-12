
import heapq

def a_star():
    # Define the initial state of the buckets as a tuple of 0s
    initial_state = (0, 0, 0, 0)
    # Define the goal state of the buckets
    goal_state = (166, 239, 286, 421)
    # Define the capacities of the jugs
    jug_capacities = [60, 59, 72, 93, 39, 74, 71, 84]
    # Define the number of buckets
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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling any of the buckets with any of the jugs
        for jug_capacity in jug_capacities:
            for bucket_index in range(num_buckets):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it and without violating the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
                if state[bucket_index] + jug_capacity <= goal_state[bucket_index] and all(state[bucket_index] + jug_capacity >= state[i] for i in range(bucket_index + 1, num_buckets)):
                    # Generate the new state
                    new_state = list(state)
                    new_state[bucket_index] += jug_capacity
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_index + 1)], new_state))

                # Similarly, generate all possible actions of emptying any of the buckets
                if state[bucket_index] > 0:
                    new_state = list(state)
                    new_state[bucket_index] = 0
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_index + 1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining amounts of water to be filled in each bucket
    # The heuristic relaxes the constraint that the buckets can only be filled with the jugs and presumes we can fill the buckets directly to their goal amounts
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling a bucket is always 1, which is exactly the decrease in the remaining amount of water to be filled in the bucket, if the bucket is filled, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining amount of water to be filled in each bucket would be 0 in the goal state.
    return sum(goal[i] - state[i] for i in range(len(state)))

print(a_star())
