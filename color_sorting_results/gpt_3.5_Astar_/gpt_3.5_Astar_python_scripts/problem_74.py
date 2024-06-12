
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Green', 'Red', 'Green', 'Red', 'Green'], ['Blue', 'Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue', 'Blue']]
    goal_state = [['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
    num_tubes = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if the move is valid, i.e., the tube from which the ball is taken is not empty and the tube to which the ball is moved is not full
                    if state[i] and len(state[j]) < 8:
                        new_state = [list(tube) for tube in state]
                        ball = new_state[i].pop(0)
                        new_state[j].insert(0, ball)
                        new_state_str = str(new_state)
                        new_cost = g + 1

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
