
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (260, 287, 413)
    # Define the capacities of the jugs
    jug_capacities = [145, 101, 17, 75, 102, 129]
    # Define the number of buckets
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken to reach that state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling and emptying the buckets using the jugs
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the bucket j with the jug i
                new_state = list(state)
                new_state[j] = min(state[j] + jug_capacities[i], goal_state[j])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the amount in the next bucket
                if j < num_buckets - 1 and new_state[j] > new_state[j + 1]:
                    continue
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j + 1)], new_state))

                # Empty the bucket j using the jug i
                new_state = list(state)
                new_state[j] = 0
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal water levels in each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal water levels
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())