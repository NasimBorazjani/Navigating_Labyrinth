
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (253, 280, 448)
    # Define the capacities of the water jugs
    jugs = [111, 84, 17, 22, 63, 75, 148, 64]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for i in range(len(jugs)):
            for j in range(num_buckets):
                # Fill the jth bucket using the ith jug
                new_state = list(state)
                new_state[j] = min(state[j] + jugs[i], goal_state[j])
                # Check if the new state is valid, i.e., the amount of water in each bucket does not exceed the amount in the next bucket
                if all(new_state[k] <= new_state[k+1] for k in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state, which is the amount of water added or removed
                    new_cost = g + abs(state[j] - new_state[j])
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j+1)], new_state))

                # Empty the jth bucket using the ith jug
                new_state = list(state)
                new_state[j] = 0
                # Check if the new state is valid
                if all(new_state[k] <= new_state[k+1] for k in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    new_cost = g + state[j]
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jugs[i], j+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, presuming we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always greater than or equal to the difference between the current and goal state for that bucket
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
