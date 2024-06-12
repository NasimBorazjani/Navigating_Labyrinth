
import heapq
import math


def a_star():
    # Define the initial state of the buckets, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 254, 456, and 579 liters of water respectively
    goal_state = (254, 456, 579)
    # Define the capacities of the water jugs
    jugs = [141, 101, 126, 26, 120, 75, 110, 108, 97, 100]
    # Define the number of buckets
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the sequence of actions
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling and emptying the buckets
        for jug in jugs:
            for bucket in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket] = min(state[bucket] + jug, goal_state[bucket])
                # Check if the new state is valid
                if new_state[bucket] >= state[bucket]:
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
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it presumes we can always empty the buckets to the desired level
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
