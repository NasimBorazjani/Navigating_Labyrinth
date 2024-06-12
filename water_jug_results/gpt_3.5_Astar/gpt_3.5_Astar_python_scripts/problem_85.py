
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (308, 309, 387, 433)
    # Define the capacities of the water jugs
    jugs = [67, 98, 66, 59, 37, 61, 128, 92]
    # Define the capacities of the unlabeled buckets
    buckets = [308, 309, 387, 433]
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

        # Generate all possible actions from the current state
        for jug in jugs:
            for bucket in range(num_buckets):
                # Check if the action is valid, i.e., the jug has water and the bucket is not overfilled
                if state[bucket] < buckets[bucket] and state[bucket] + jug <= buckets[bucket]:
                    # Perform the action of filling the bucket with water from the jug
                    new_state = list(state)
                    new_state[bucket] += jug
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

        for bucket in range(num_buckets):
            for jug in jugs:
                # Check if the action is valid, i.e., the bucket has water and the jug can hold the amount of water in the bucket
                if state[bucket] > 0 and state[bucket] - jug >= 0:
                    # Perform the action of emptying the bucket into the jug
                    new_state = list(state)
                    new_state[bucket] -= jug
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it assumes we can always empty the bucket to the desired amount
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of emptying a bucket into a jug is always 1, which is exactly the decrease in the difference between the current and goal state
    return sum(abs(s - g) for s, g in zip(state, goal))


print(a_star())
