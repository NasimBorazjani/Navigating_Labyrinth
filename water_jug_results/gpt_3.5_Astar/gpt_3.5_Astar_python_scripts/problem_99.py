
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (203, 429, 433, 477)
    # Define the capacities of the water jugs
    jug_capacities = [32, 73, 55, 68, 61, 107, 44, 45, 74, 113]
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
        for jug in jug_capacities:
            for bucket in range(num_buckets):
                # Fill the bucket with the jug
                new_state = list(state)
                new_state[bucket] = min(state[bucket] + jug, goal_state[bucket])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the amount in the next bucket
                if all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state, which is the amount of water added or removed
                    new_cost = g + abs(state[bucket] - new_state[bucket])
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket+1)], new_state))

                # Empty the bucket using the jug
                new_state = list(state)
                new_state[bucket] = 0
                new_state = tuple(new_state)
                # Calculate the cost of the new state, which is the amount of water emptied
                new_cost = g + state[bucket]
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in a specific order and presumes we can fill the buckets in any order to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always greater than or equal to the difference between the current and goal state for that bucket
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
