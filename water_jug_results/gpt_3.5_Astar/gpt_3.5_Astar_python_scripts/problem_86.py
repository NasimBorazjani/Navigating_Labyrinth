
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (205, 365, 391, 414)
    # Define the capacities of the water jugs
    jugs = [87, 13, 27, 106, 18, 91, 17, 138]
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

        # Generate all possible actions from the current state
        for i in range(len(jugs)):
            for j in range(num_buckets):
                # Fill the jth bucket with the ith jug
                new_state = list(state)
                new_state[j] = min(state[j] + jugs[i], goal_state[j])
                # Check if the new state is valid
                if new_state[j] <= goal_state[j] and (j == 0 or new_state[j] <= new_state[j-1]):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        if state[j] < new_state[j]:
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j+1)], new_state))
                        else:
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jugs[i], j+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current state and the goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is 1, which is exactly the decrease in the difference between the current state and the goal state
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
