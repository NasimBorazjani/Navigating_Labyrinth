
import heapq

def initialize():
    # Define the initial state of the tubes, represented as a list of lists
    initial_state = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
    num_tubes = 3
    tube_capacity = 6

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))

    return initial_state, num_tubes, tube_capacity, visited_costs, queue

def a_star():
    initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the state is the goal state, where all balls are sorted by color in each tube
        if all(all(ball == state[0][0] for ball in tube) for tube in state):
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if it's possible to move a ball from tube i to tube j
                    if state[i] and len(state[j]) < tube_capacity:
                        new_state = [list(tube) for tube in state]
                        new_state[j].insert(0, new_state[i].pop(0))
                        # Encode the new state as a string to use it as a key in the visited_costs dictionary
                        new_state_key = str(new_state)
                        new_cost = g + 1

                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                        if new_state_key not in visited_costs or new_cost < visited_costs[new_state_key]:
                            visited_costs[new_state_key] = new_cost
                            heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j)], new_state))

    return None

print(a_star())
