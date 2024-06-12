
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Red', 'Green', 'Blue', 'Red', 'Blue', 'Blue'],
                     ['Red', 'Blue', 'Green', 'Green', 'Blue', 'Red'],
                     ['Green', 'Green', 'Red', 'Blue', 'Green', 'Red']]
    num_tubes = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # Check if the tubes are sorted, i.e., each tube contains balls of only one color
        if all(len(set(tube)) == 1 for tube in state):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if from_tube != to_tube and len(state[to_tube]) < 9 and state[from_tube]:
                    new_state = [list(tube) for tube in state]
                    ball = new_state[from_tube].pop(0)
                    new_state[to_tube].insert(0, ball)
                    new_state = [tuple(tube) for tube in new_state]
                    new_cost = g + 1

                    if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                        visited_costs[str(new_state)] = new_cost
                        heapq.heappush(queue, (g + heuristic(state), new_cost, actions + [(from_tube, to_tube)], new_state))

    return None


def heuristic(state):
    # The heuristic is the sum of the number of balls in each tube that are not in the correct order
    h = 0
    for tube in state:
        for i in range(len(tube) - 1):
            if tube[i] != tube[i + 1]:
                h += 1
    return h


print(a_star())
