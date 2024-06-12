
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled with the specified amounts
    goal_state = (257, 260, 269, 291)
    # Define the capacities of the water jugs
    jug_capacities = [34, 98, 27, 19, 52, 53]
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

        # Generate all possible actions from the current state, which includes filling and emptying the buckets
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the j-th bucket with the i-th jug
                new_state = list(state)
                new_state[j] = min(state[j] + jug_capacities[i], jug_capacities[i])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the amount in the next bucket
                valid_state = True
                for k in range(num_buckets - 1):
                    if new_state[k] > new_state[k + 1]:
                        valid_state = False
                        break
                if valid_state:
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j + 1)], new_state))

                # Empty the j-th bucket with the i-th jug
                new_state = list(state)
                new_state[j] = 0
                # Check if the new state is valid
                valid_state = True
                for k in range(num_buckets - 1):
                    if new_state[k] > new_state[k + 1]:
                        valid_state = False
                        break
                if valid_state:
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
