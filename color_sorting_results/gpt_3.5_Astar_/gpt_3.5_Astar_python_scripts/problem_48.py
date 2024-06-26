
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Red', 'Blue', 'Blue', 'Red'], ['Blue', 'Green', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Red']]
    goal_state = [['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green']]
    num_tubes = 3
    tube_capacity = 7

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if moving a ball from tube i to tube j is a valid action
                    if state[i] and len(state[j]) < tube_capacity:
                        new_state = [list(tube) for tube in state]
                        new_state[j].append(new_state[i].pop(0))
                        new_state = [tuple(tube) for tube in new_state]
                        new_cost = g + 1

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of balls not in the correct position in each tube
    # The heuristic relaxes the constraint that only one ball can be moved at a time, presuming we can move multiple balls at once to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to the correct position is always 1, which is exactly the decrease in the number of balls not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
