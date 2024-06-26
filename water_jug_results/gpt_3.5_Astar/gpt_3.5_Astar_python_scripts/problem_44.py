
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (192, 247, 479)
    # Define the capacities of the water jugs
    jugs = [67, 55, 84, 148, 107, 114, 17, 143, 40, 39]

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
            for j in range(1, 4):
                # Fill the jth bucket with the ith jug
                new_state = list(state)
                new_state[j-1] = min(state[j-1] + jugs[i], goal_state[j-1])
                # Check if the new state is valid
                if new_state[j-1] >= state[j-1] and (j == 3 or new_state[j-1] <= new_state[j]):
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j)], new_state))

                # Empty the jth bucket using the ith jug
                new_state = list(state)
                new_state[j-1] = 0
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jugs[i], j)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between the buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal amounts
    # The cost of the goal state is 0, as the amounts in the buckets match the goal amounts

    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
