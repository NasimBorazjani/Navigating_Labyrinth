
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = (260, 295, 331, 394)
    jug_capacities = [12, 88, 148, 87, 143, 131]
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

        # Generate all possible actions from the current state, which includes filling any of the 4 buckets with any of the 5 jugs, or emptying any of the 4 buckets
        for jug_capacity in jug_capacities:
            for bucket_ind in range(num_buckets):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it and without violating the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
                if state[bucket_ind] + jug_capacity <= goal_state[bucket_ind] and (bucket_ind == num_buckets - 1 or state[bucket_ind] + jug_capacity <= state[bucket_ind + 1]):
                    # Generate the new state
                    new_state = list(state)
                    new_state[bucket_ind] += jug_capacity
                    new_state = tuple(new_state)
                    # The cost so far is the amount of water added to the bucket, as our objective is to minimize the amount of water used
                    new_cost = g + jug_capacity

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_ind + 1)], new_state))

                # Check if the new state would be valid, ie if the bucket can be emptied without violating the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
                if bucket_ind == 0 or state[bucket_ind - 1] <= state[bucket_ind] - jug_capacity:
                    # Generate the new state
                    new_state = list(state)
                    new_state[bucket_ind] -= jug_capacity
                    new_state = tuple(new_state)
                    # The cost so far is the amount of water removed from the bucket, as our objective is to minimize the amount of water used
                    new_cost = g + jug_capacity

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_ind + 1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining amounts of water to be added to each bucket to reach its goal amount
    # The heuristic relaxes the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it and presumes we can add water to any bucket directly to reach its goal amount
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding water to a bucket is the amount of water added, which is exactly the decrease in the remaining amount of water to be added to the bucket, if the water is added to the bucket, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining amount of water to be added to each bucket would be 0 in the goal state.
    return sum(goal[i] - state[i] for i in range(len(state)))

print(a_star())
