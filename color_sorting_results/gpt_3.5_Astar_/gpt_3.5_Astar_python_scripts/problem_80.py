
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Red', 'Blue', 'Green', 'Blue', 'Green'],
                     ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red'],
                     ['Green', 'Blue', 'Red', 'Red', 'Red', 'Red']]
    num_tubes = 3
    tube_capacity = 9

    visited_costs = {}
    visited_costs[tuple(tuple(tube) for tube in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the tubes are sorted, i.e., each tube contains balls of only one color
        if all(len(set(tube)) == 1 for tube in state):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if moving a ball from tube i to tube j is a valid action
                    if state[i] and len(state[j]) < tube_capacity:
                        new_state = [list(tube) for tube in state]
                        new_state[j].append(new_state[i].pop())
                        new_state = tuple(tuple(tube) for tube in new_state)
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (g + heuristic(state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state):
    # An admissible and consistent heuristic is the sum of the number of balls in each tube that are not in the correct order
    # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to sort the tubes
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to the correct tube is always 1, which is exactly the decrease in the number of balls not in the correct order
    h = 0
    for tube in state:
        for i in range(len(tube) - 1):
            if tube[i] != tube[i + 1]:
                h += 1
    return h


print(a_star())
