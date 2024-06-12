
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Blue', 'Green', 'Red', 'Red'],
                     ['Green', 'Blue', 'Green', 'Blue', 'Blue'],
                     ['Red', 'Green', 'Red', 'Red', 'Green']]
    num_tubes = 3
    tube_capacity = 8

    visited_costs = {}
    visited_costs[tuple(tuple(row) for row in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the tubes are sorted by color
        if all(all(ball == state[0][0] for ball in tube) for tube in state):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    new_state = [list(row) for row in state]
                    if new_state[i] and len(new_state[j]) < tube_capacity:
                        ball = new_state[i].pop(0)
                        new_state[j].insert(0, ball)
                        new_state = tuple(tuple(row) for row in new_state)
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (g + heuristic(state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state):
    # An admissible and consistent heuristic is the number of balls that are not in the correct position
    # The heuristic relaxes the constraint that only one ball can be moved at a time, presuming we can move multiple balls at once to sort them
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to the correct position is always 1, which is exactly the decrease in the number of balls not in the correct position
    return sum(sum(ball != state[i][0] for ball in tube) for i, tube in enumerate(state))


print(a_star())
