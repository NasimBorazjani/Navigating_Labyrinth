
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 394, 425, and 426 liters of water respectively
    goal_state = (394, 425, 426)
    # Define the capacities of the jugs
    jugs = [117, 128, 36, 129, 103, 53, 21, 119, 105, 26]
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

        # Generate all possible actions from the current state, which includes filling and emptying the buckets using the jugs
        for jug in jugs:
            for bucket in range(num_buckets):
                # Check if the action is valid, i.e., the jug has enough water to fill or the bucket has water to empty
                if (jug <= state[bucket] or state[bucket] == 0) and (bucket == num_buckets - 1 or state[bucket] <= state[bucket + 1]):
                    # Calculate the new state after performing the action
                    new_state = list(state)
                    if state[bucket] == 0:
                        new_state[bucket] = jug
                    else:
                        new_state[bucket] = 0
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the difference between the current and goal state
    # The cost of the goal state is 0, as the buckets are filled with the desired amounts of water
    h = sum(abs(s - g) for s, g in zip(state, goal))
    return h


print(a_star())
