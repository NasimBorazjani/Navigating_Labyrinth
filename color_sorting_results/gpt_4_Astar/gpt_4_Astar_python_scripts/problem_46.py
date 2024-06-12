
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
    initial_state = (('Red', 'Blue', 'Red', 'Red'), ('Blue', 'Green', 'Green', 'Blue'), ('Green', 'Blue', 'Green', 'Red'))
    goal_state = (('Red', 'Red', 'Red', 'Red'), ('Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Green', 'Green', 'Green'))   

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

        # Generate all valid actions from the current state, which includes moving any of the balls from one tube to another
        for i in range(3):
            if state[i]:  # if tube i is not empty
                for j in range(3):
                    if i != j and len(state[j]) < 7:  # if tube j is not full and not the same as tube i
                        # The action is valid, generate the new state
                        new_state = list(map(list, state))  # copy the current state
                        ball = new_state[i].pop(0)  # remove the top ball from tube i
                        new_state[j].insert(0, ball)  # and place it on top of tube j
                        new_state = tuple(map(tuple, new_state))  # convert the new state back to a tuple
                        # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
                        new_cost = g + 1

                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of misplaced balls in each tube
    # The heuristic relaxes the constraint that a ball can only be moved to the top of another tube and presumes we can move the balls to their goal position by moving them to any position in the tube
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to a neighboring tube is always 1, which is exactly the decrease in the number of misplaced balls, if the ball is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the number of misplaced balls would be 0 in the goal state.
    h = 0
    for i in range(3):
        for ball in state[i]:
            if ball != goal[i][0]:  # if the ball is not in its goal tube
                h += 1
    return h

print(a_star())
