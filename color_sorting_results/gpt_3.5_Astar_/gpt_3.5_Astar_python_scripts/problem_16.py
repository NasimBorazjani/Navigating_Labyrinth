
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Red', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Red', 'Blue'], ['Blue', 'Red', 'Green', 'Blue']]
    goal_state = [['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue']]
    
    # Encoding other variables given in the problem statement
    num_tubes = 3
    tube_capacity = 6

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

        # Generate all valid actions from the current state, which includes moving a ball from one tube to another
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if from_tube != to_tube:
                    new_state = [list(tube) for tube in state]
                    # Check if the from_tube is not empty and the to_tube is not at capacity
                    if new_state[from_tube] and len(new_state[to_tube]) < tube_capacity:
                        ball = new_state[from_tube].pop(0)
                        new_state[to_tube].insert(0, ball)
                        new_state_str = str(new_state)
                        new_cost = g + 1

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(from_tube, to_tube)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of balls that are not in the correct position
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
