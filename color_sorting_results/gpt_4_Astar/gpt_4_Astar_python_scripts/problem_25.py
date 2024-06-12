
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
    initial_state = (('Green', 'Green', 'Red', 'Red'), ('Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Red', 'Green', 'Red'))
    goal_state = (('Green', 'Green', 'Green', 'Green', None, None), ('Blue', 'Blue', 'Blue', 'Blue', None, None), ('Red', 'Red', 'Red', 'Red', None, None))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes moving the top ball from any tube to the top of any other tube
        for i in range(3):
            for j in range(3):
                # Check if the move is valid, ie if the tube to move from is not empty and the tube to move to is not full
                if state[i] and state[j] and (len(state[j]) < 6 or state[j][0] is None):
                    # The move is valid, generate the new state
                    new_state = [list(tube[:]) for tube in state]
                    ball_to_move = new_state[i].pop(0)
                    # If the tube to move to is empty, replace the None with the ball to move
                    if new_state[j][0] is None:
                        new_state[j][0] = ball_to_move
                    else:
                        new_state[j].insert(0, ball_to_move)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of balls in the wrong tube
    # The heuristic relaxes the constraint that a ball can only be moved to the top of another tube and presumes we can move the balls to their goal tube directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to a neighboring tube is always 1, which is exactly the decrease in the number of balls in the wrong tube, if the ball is moved toward its goal tube, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the number of balls in the wrong tube would be 0 in the goal state.
    h = 0
    for i in range(3):
        for ball in state[i]:
            if ball is not None and ball != goal[i][0]:
                h += 1
    return h

print(a_star())
