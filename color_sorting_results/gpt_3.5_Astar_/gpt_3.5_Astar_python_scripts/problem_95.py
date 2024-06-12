
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Green', 'Green', 'Green', 'Red', 'Blue', 'Blue'],
                     ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'],
                     ['Blue', 'Green', 'Blue', 'Red', 'Red', 'Blue']]
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
                if i != j and len(state[i]) > 0 and len(state[j]) < tube_capacity:
                    new_state = [list(tube) for tube in state]
                    ball = new_state[i].pop(0)
                    new_state[j].insert(0, ball)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state):
    # An admissible and consistent heuristic is the sum of the number of balls that are not in the correct position in each tube
    # The heuristic relaxes the constraint that only one ball can be moved at a time, presuming that all balls can be moved to their correct position in one step
    # Thus, the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to the correct position is always 1, which is exactly the decrease in the number of balls not in the correct position
    h = 0
    for tube in state:
        for i in range(len(tube)):
            if tube[i] != tube[0]:
                h += 1
    return h


print(a_star())
