
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 287, 394, and 455 liters of water respectively
    goal_state = (287, 394, 455)
    # Define the capacities of the water jugs
    jugs = [75, 20, 64, 106, 88, 13, 107, 131]
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

        # Generate all possible actions from the current state, which includes filling and emptying the buckets using the water jugs
        for jug in jugs:
            for bucket in range(num_buckets):
                # Check if the action is valid, ie the water from the jug can be added to or removed from the bucket without exceeding its capacity
                if (actions and actions[-1][2] <= bucket) or not actions:
                    new_state = list(state)
                    if actions and actions[-1][0] == '+':
                        new_state[bucket] += jug
                    elif actions and actions[-1][0] == '-':
                        new_state[bucket] -= jug
                    new_state = tuple(new_state)

                    # Calculate the cost of the new state, which is the amount of water added or removed
                    new_cost = g + jug

                    if all(x >= 0 for x in new_state) and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost using the sum of differences between the current and goal state
                        h = sum(abs(x - y) for x, y in zip(new_state, goal_state))
                        heapq.heappush(queue, (g + h, new_cost, actions + [('+', jug, bucket)], new_state))

    return None


print(a_star())
