
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Green'],
                     ['Blue', 'Red', 'Green', 'Green', 'Green', 'Red'],
                     ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Green']]
    num_tubes = 3
    tube_capacity = 9

    visited_costs = {}
    visited_costs[tuple(tuple(tube) for tube in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the tubes are sorted
        if all(all(ball == state[0][0] for ball in tube) for tube in state):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if moving a ball from tube i to tube j is a valid action
                    if state[i] and len(state[j]) < tube_capacity:
                        new_state = [list(tube) for tube in state]
                        new_state[j].insert(0, new_state[i].pop(0))
                        new_state = tuple(tuple(tube) for tube in new_state)
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
