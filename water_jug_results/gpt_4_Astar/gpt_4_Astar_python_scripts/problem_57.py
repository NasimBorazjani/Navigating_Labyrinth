
import heapq

def a_star():
    # Define the initial state of the buckets and the goal state
    initial_state = (0, 0, 0, 0)
    goal_state = (230, 267, 278, 318)

    # Define the capacities of the jugs
    jug_capacities = [15, 20, 141, 104, 67, 14]

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

        # Generate all possible actions from the current state, which includes filling any of the 4 buckets with any of the 5 jugs, or emptying any of the 4 buckets into any of the 5 jugs
        for i in range(len(jug_capacities)):
            for j in range(len(state)):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it and without violating the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it
                if state[j] + jug_capacities[i] <= goal_state[j] and (j == len(state) - 1 or state[j] + jug_capacities[i] <= state[j + 1]):
                    # The action is valid, generate the new state
                    new_state = list(state)
                    new_state[j] += jug_capacities[i]
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j + 1)], new_state))

                # Similarly, check if the bucket can be emptied into the jug without violating the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed before it
                if state[j] - jug_capacities[i] >= 0 and (j == 0 or state[j] - jug_capacities[i] >= state[j - 1]):
                    # The action is valid, generate the new state
                    new_state = list(state)
                    new_state[j] -= jug_capacities[i]
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j + 1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining amounts of water to be added to each bucket to reach its goal amount
    # The heuristic relaxes the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it and presumes we can add the remaining amount of water to each bucket directly
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding water to a bucket is always 1, which is exactly the decrease in the remaining amount of water to be added to the bucket, if water is added to it, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining amount of water to be added to each bucket would be 0 in the goal state
    return sum(goal[i] - state[i] for i in range(len(state)))

print(a_star())
