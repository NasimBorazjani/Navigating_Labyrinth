
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle
    initial_state = 'O'
    goal_state = ['B', 'B', 'H', 'H']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'S': {'H'},
        'E': {'F', 'B', 'I', 'Z'},
        'D': {'B'},
        'Y': {'E', 'D', 'C', 'Z'},
        'F': {'B', 'O', 'U', 'I'},
        'B': {'S', 'D', 'Y', 'F', 'U', 'C'},
        'O': {'S', 'F', 'C', 'Q', 'J', 'Z'},
        'H': {'Y', 'F', 'Q', 'J'},
        'U': {'S', 'D', 'Y', 'H', 'C'},
        'I': {'O', 'Z'},
        'C': {'I'},
        'Q': {'D', 'F', 'U', 'J'},
        'Z': {'E', 'D', 'O', 'H'},
        'J': {'E', 'D', 'Y', 'F', 'U', 'Q', 'Z'}
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, tuple(goal_state))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, tuple(goal_state))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, remaining_goals = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if not remaining_goals:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for next_state in adjacency_matrix[state]:
            # If the next state is a goal state, remove it from the remaining goals
            if next_state in remaining_goals:
                new_remaining_goals = list(remaining_goals)
                new_remaining_goals.remove(next_state)
                new_remaining_goals = tuple(new_remaining_goals)
            else:
                new_remaining_goals = remaining_goals

            # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if (next_state, new_remaining_goals) not in visited_costs or new_cost < visited_costs[(next_state, new_remaining_goals)]:
                visited_costs[(next_state, new_remaining_goals)] = new_cost
                heapq.heappush(queue, (new_cost + heuristic(new_remaining_goals), new_cost, actions + [next_state], next_state, new_remaining_goals))

    return None

def heuristic(remaining_goals):
    # An admissible and consistent heuristic is the number of remaining goal states
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining goal state must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a goal state
    return len(remaining_goals)

print(a_star())
