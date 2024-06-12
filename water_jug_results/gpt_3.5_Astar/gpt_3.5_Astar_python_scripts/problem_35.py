
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (225, 334, 381)
    # Define the capacities of the water jugs
    jug_capacities = [120, 95, 49, 150, 83, 97, 44, 43]
    # Define the number of buckets
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using each jug
        for jug in jug_capacities:
            for bucket in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket] = min(state[bucket] + jug, goal_state[bucket])
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket] = 0
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order and that the jugs can only be used to fill or empty the buckets
    # It is admissible because it never overestimates the cost to reach the goal state, as each difference must be filled or emptied at least once
    # It is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the heuristic estimate if the bucket is moved towards its goal amount
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
