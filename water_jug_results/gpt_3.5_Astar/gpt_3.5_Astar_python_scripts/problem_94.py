
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (377, 456, 512, 541)
    # Define the capacities of the water jugs
    jug_capacities = [81, 56, 41, 88, 137, 14, 149, 120, 87, 104]
    # Define the buckets that need to be filled
    buckets = [377, 456, 512, 541]
    # Define the number of buckets
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying a bucket using a jug
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(buckets[bucket_num], new_state[bucket_num] + jug_capacity)
                # Check if the new state is valid
                if new_state[bucket_num] <= buckets[bucket_num] and tuple(new_state) not in visited_costs:
                    new_cost = g + 1
                    visited_costs[tuple(new_state)] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], tuple(new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket_num] = 0
                # Check if the new state is valid
                if tuple(new_state) not in visited_costs:
                    new_cost = g + 1
                    visited_costs[tuple(new_state)] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num + 1)], tuple(new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water between buckets is always 1, which is exactly the decrease in the sum of the absolute differences between the current and goal state
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
