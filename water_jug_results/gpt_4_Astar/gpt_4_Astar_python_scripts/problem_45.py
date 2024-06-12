
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0)
    goal_state = (155, 208, 295)
    # Define the capacities of the jugs
    jug_capacities = [116, 16, 79, 75, 30, 87, 28, 96, 15, 134]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling any of the 3 buckets with any of the 9 jugs, or emptying any of the 3 buckets
        for i, jug_capacity in enumerate(jug_capacities):
            for j in range(3):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overflowing and the amount of water in each bucket does not exceed the amount of water in the bucket placed after it
                if state[j] + jug_capacity <= goal_state[j] and all(state[k] + jug_capacity <= state[k+1] for k in range(j)):
                    # The action is valid, generate the new state
                    new_state = list(state)
                    new_state[j] += jug_capacity
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, j+1)], new_state))

                # Similarly, check if the bucket can be emptied without violating the constraints
                if state[j] > 0 and all(state[k] - jug_capacity >= state[k+1] for k in range(j)):
                    new_state = list(state)
                    new_state[j] -= jug_capacity
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, j+1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal amounts of water in each bucket
    # The heuristic relaxes the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it and presumes we can add or remove water from the buckets to reach their goal amounts directly
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of performing an action is always 1, which is exactly the decrease in the heuristic cost, if the action moves the state toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the amount of water in each bucket would be equal to its goal amount in the goal state.
    return sum(abs(s - g) for s, g in zip(state, goal))

print(a_star())