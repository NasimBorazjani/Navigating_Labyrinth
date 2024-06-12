
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 201, 202, and 233 liters of water respectively
    goal_state = (201, 202, 233)
    # Define the capacities of the jugs
    jugs = [36, 72, 16, 80, 45, 67, 38, 32, 149, 37]
    # Define the capacities of the unlabeled buckets
    buckets = [201, 202, 233]
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

        # Generate all possible actions from the current state, which includes filling or emptying the unlabeled buckets using the jugs
        for jug in jugs:
            for bucket in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket] += jug
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the capacity and the water in each bucket does not exceed the water in the next bucket
                if all(0 <= new_state[i] <= buckets[i] for i in range(num_buckets)) and all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket+1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket] -= jug
                # Check if the new state is valid
                if all(0 <= new_state[i] <= buckets[i] for i in range(num_buckets)) and all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current water levels in the buckets and the goal water levels
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always 1, which is exactly the decrease in the heuristic estimate if the water level is moved towards the goal level
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
