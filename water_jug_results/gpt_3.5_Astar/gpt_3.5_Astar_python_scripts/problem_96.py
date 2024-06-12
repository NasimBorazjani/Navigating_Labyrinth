
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (177, 263, 294, 462)
    # Define the capacities of the water jugs
    jug_capacities = [90, 21, 104, 111, 97, 22, 34, 15, 62, 52]
    # Define the number of buckets
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state matches the goal state, return the actions taken to reach that state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the j-th bucket using the i-th jug
                new_state = list(state)
                new_state[j] = min(state[j] + jug_capacities[i], goal_state[j])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the amount in the next bucket
                if all(new_state[k] <= new_state[k+1] for k in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of reaching the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Add the action to the list of actions
                        if state[j] < new_state[j]:
                            actions.append(('+', jug_capacities[i], j+1))
                        else:
                            actions.append(('-', jug_capacities[i], j+1))
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions[:], new_state))
                        actions.pop()

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current water levels in each bucket and the goal water levels
    # The heuristic relaxes the constraint that the water jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always greater than or equal to the difference in water levels, thus the heuristic estimate for the goal state is 0
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
