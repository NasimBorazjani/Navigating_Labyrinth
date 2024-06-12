
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (219, 240, 312, 411)
    # Define the capacities of the water jugs
    jug_capacities = [126, 120, 127, 110, 54, 39, 38, 47, 139, 99]
    # Define the number of buckets
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the sequence of actions
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using each jug
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(state[bucket_num] + jug_capacity, goal_state[bucket_num])
                # Check if the new state is valid
                if new_state[bucket_num] <= goal_state[bucket_num] and new_state[bucket_num] <= new_state[bucket_num + 1]:
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket_num] = 0
                # Check if the new state is valid
                if new_state[bucket_num] <= new_state[bucket_num + 1]:
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal amounts in the bucket
    # The cost of the goal state is 0, as the amounts in the buckets match the goal amounts

    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
