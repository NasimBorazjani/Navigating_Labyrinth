
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = (245, 252, 264, 314)
    # Define the capacities of the jugs
    jug_capacities = [19, 42, 18, 127, 106, 32, 22, 137]
    num_buckets = 4

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

        # Generate all possible actions from the current state, which includes filling any of the 4 buckets with any of the 7 jugs, and emptying any of the 4 buckets
        for i in range(num_buckets):
            for j in range(len(jug_capacities)):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it and without violating the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it
                if state[i] + jug_capacities[j] <= goal_state[i] and all(state[i] + jug_capacities[j] >= state[k] for k in range(i + 1, num_buckets)):
                    # The action is valid, generate the new state
                    new_state = list(state)
                    new_state[i] += jug_capacities[j]
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[j], i + 1)], new_state))

                # Similarly, check if the bucket can be emptied without violating the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it
                if state[i] > 0 and all(state[i] - state[i] <= state[k] for k in range(i + 1, num_buckets)):
                    # The action is valid, generate the new state
                    new_state = list(state)
                    new_state[i] = 0
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', state[i], i + 1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal amounts of water in each bucket
    # The heuristic relaxes the constraint that the buckets can only be filled with the jugs and presumes we can add or remove any amount of water to/from the buckets to reach their goal amounts
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water to/from a bucket is always 1, which is exactly the decrease or increase in the difference between the current and goal amounts of water in the bucket, if the bucket is filled or emptied, respectively, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the current and goal amounts of water in each bucket would be 0 in the goal state.
    return sum(abs(a - b) for a, b in zip(state, goal))

print(a_star())