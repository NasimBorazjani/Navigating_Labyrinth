
import heapq


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 448, 466, and 509 liters of water respectively
    goal_state = (448, 466, 509)
    # Define the capacities of the jugs
    jug_capacities = [103, 109, 146, 101, 17, 145, 68]
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

        # Generate all possible actions from the current state
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the jugs
                new_state = list(state)
                if actions and actions[-1][0] == '+' and actions[-1][2] == j:
                    continue
                if new_state[j] + jug_capacities[i] <= jug_capacities[j]:
                    new_state[j] += jug_capacities[i]
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j)], new_state))

                # Empty the jugs
                new_state = list(state)
                if actions and actions[-1][0] == '-' and actions[-1][2] == j:
                    continue
                if new_state[j] - jug_capacities[i] >= 0:
                    new_state[j] -= jug_capacities[i]
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
    # It is admissible because it never overestimates the cost to reach the goal state, as the sum of the absolute differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate if the water is moved towards the goal state
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
