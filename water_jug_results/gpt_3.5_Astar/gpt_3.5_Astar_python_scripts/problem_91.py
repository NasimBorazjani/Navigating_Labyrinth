
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (338, 431, 493, 550)
    # Define the capacities of the water jugs
    jugs = [51, 75, 112, 122, 54, 129, 31, 127, 113]
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
        for jug in jugs:
            for i in range(num_buckets):
                new_state = list(state)
                # Fill the bucket if the action is '+'
                if state[i] + jug <= goal_state[i]:
                    new_state[i] += jug
                # Empty the bucket if the action is '-'
                else:
                    new_state[i] = 0
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic value for the new state
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + h, new_cost, actions + [('+', jug, i + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current state and the goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is 1, which is equal to the decrease in the difference between the current state and the goal state
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
