
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (258, 261, 415, 430)
    # Define the capacities of the water jugs
    jug_capacities = [128, 67, 44, 31, 127, 15]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the j-th bucket using the i-th jug
                new_state = list(state)
                new_state[j] = min(state[j] + jug_capacities[i], goal_state[j])
                # Check if the new state is valid
                if new_state[j] <= goal_state[j]:
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Add the action to the list of actions
                        if state[j] < new_state[j]:
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j+1)], new_state))
                        else:
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current state and the goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order and that the jugs can only be used to fill or empty the buckets
    # It is admissible because the sum of the differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is equal to the decrease in the heuristic estimate
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
