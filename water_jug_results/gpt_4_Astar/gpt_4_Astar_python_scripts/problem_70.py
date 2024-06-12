
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = (283, 295, 428, 428)
    # Define the capacities of the jugs
    jug_capacities = [44, 128, 127, 85, 40, 125]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions performed to reach the goal state
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state, which includes filling each bucket with each jug
        for jug_capacity in jug_capacities:
            for bucket_index in range(len(state)):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it and without violating the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
                if state[bucket_index] + jug_capacity <= goal_state[bucket_index] and all(state[bucket_index] + jug_capacity >= state[i] for i in range(bucket_index + 1, len(state))):
                    # Generate the new state
                    new_state = list(state)
                    new_state[bucket_index] += jug_capacity
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_index + 1)], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal amounts of water in each bucket
    # The heuristic relaxes the constraint that the buckets can only be filled with the jugs and presumes we can add the exact amount of water required to reach the goal state to each bucket
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one state to a successor state is always 1, which is exactly the decrease in the heuristic cost, if the successor state is closer to the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the current and goal amounts of water in each bucket would be 0 in the goal state
    return sum(goal[i] - state[i] for i in range(len(state)))

print(a_star())
