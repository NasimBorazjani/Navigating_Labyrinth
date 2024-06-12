
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']]
    num_tubes = 3
    tube_capacity = 9

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # Check if the tubes are sorted
        if all(all(state[i][j] == state[i][0] for j in range(len(state[i]))) for i in range(num_tubes)):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j and len(state[i]) > 0 and len(state[j]) < tube_capacity:
                    new_state = [list(tube) for tube in state]
                    ball = new_state[i].pop(0)
                    new_state[j].insert(0, ball)
                    new_state = tuple([tuple(tube) for tube in new_state])
                    new_cost = g + 1

                    if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                        visited_costs[str(new_state)] = new_cost
                        heapq.heappush(queue, (g + heuristic(state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state):
    # The heuristic is the number of balls that are not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != state[i][0]:
                h += 1
    return h


print(a_star())
