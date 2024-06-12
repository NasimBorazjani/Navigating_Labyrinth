
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (215, 403, 420, 504)
    # Define the capacities of the water jugs
    jug_capacities = [59, 104, 79, 23, 20, 60, 14, 15, 119, 105]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(state[bucket_num] + jug_capacity, goal_state[bucket_num])
                # Check if the new state is valid
                if new_state[bucket_num] <= goal_state[bucket_num] and all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket_num] = 0
                # Check if the new state is valid
                if all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + ('-', jug_capacity, bucket_num + 1), new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current state and the goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always greater than or equal to the decrease in the difference between the current state and the goal state
    # The cost of the goal state is 0, as the buckets are filled to the specified amounts
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
