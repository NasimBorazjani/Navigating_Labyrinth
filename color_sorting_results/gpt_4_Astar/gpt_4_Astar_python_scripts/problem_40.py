
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 3x4 tuples
    initial_state = (('Blue', 'Green', 'Green', 'Blue'), ('Red', 'Blue', 'Green', 'Green'), ('Red', 'Red', 'Red', 'Blue'))
    goal_state = (('Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Green', 'Green', 'Green'), ('Red', 'Red', 'Red', 'Red'))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the moves required to get to each state in a list; no moves performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes moving the top ball from any tube to the top of any other tube
        for from_tube in range(3):
            for to_tube in range(3):
                # Check if the move is valid, ie if the from_tube is not empty and the to_tube is not full
                if state[from_tube] and len(state[to_tube]) < 7:
                    # The move is valid, generate the new state
                    new_state = list(list(tube) for tube in state)
                    ball = new_state[from_tube].pop(0)
                    new_state[to_tube].insert(0, ball)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(from_tube, to_tube)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of misplaced balls in each tube
    # The heuristic relaxes the constraint that a ball can only be moved to the top of another tube and presumes we can move the balls to their goal position by moving them to any position in the tube
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to a neighboring tube is always 1, which is exactly the decrease in the number of misplaced balls, if the ball is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the number of misplaced balls would be 0 in the goal state.
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h

print(a_star())
