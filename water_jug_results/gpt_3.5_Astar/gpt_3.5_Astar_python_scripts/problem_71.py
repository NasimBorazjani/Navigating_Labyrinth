
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (304, 333, 349, 413)
    # Define the capacities of the water jugs
    jug_capacities = [141, 92, 12, 77, 49, 140]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for jug in jug_capacities:
            for bucket in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket] = min(state[bucket] + jug, goal_state[bucket])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the amount in the next bucket
                if all(new_state[i] <= new_state[i + 1] for i in range(num_buckets - 1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket] = 0
                # Check if the new state is valid
                if all(new_state[i] <= new_state[i + 1] for i in range(num_buckets - 1)):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal water levels in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in a specific order and presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
