
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (231, 288, 342, 410)
    # Define the capacities of the water jugs
    jugs = [82, 91, 135, 11, 12, 19, 143, 60]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the sequence of actions
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using each jug
        for i in range(len(jugs)):
            for j in range(4):
                new_state = list(state)
                # Fill the j-th bucket using the i-th jug
                if actions and j > 0 and new_state[j] + jugs[i] > new_state[j-1]:
                    continue
                new_state[j] += jugs[i]
                # Ensure the bucket does not overflow
                if new_state[j] > goal_state[j]:
                    continue
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j+1)], new_state))

                new_state = list(state)
                # Empty the j-th bucket using the i-th jug
                new_state[j] = 0
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jugs[i], j+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it presumes we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal amounts in the bucket
    # The cost of the goal state is 0, as the amounts in each bucket match the goal amounts

    h = sum(abs(state[i] - goal[i]) for i in range(4))
    return h


print(a_star())
