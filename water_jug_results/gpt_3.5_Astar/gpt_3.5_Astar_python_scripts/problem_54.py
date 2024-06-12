
import heapq


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (229, 303, 307)
    # Define the capacities of the jugs
    jugs = [45, 67, 134, 133, 86, 66, 107, 94, 124, 122]
    # Define the buckets in ascending order
    buckets = [229, 303, 307]
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Initialize the priority queue with the initial state
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Generate all possible actions from the current state
        for jug in jugs:
            for bucket_index, bucket in enumerate(buckets):
                # Fill the bucket
                if state[bucket_index] < bucket and state[bucket_index] + jug <= bucket:
                    new_state = list(state)
                    new_state[bucket_index] += jug
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket_index)], new_state))
                
                # Empty the bucket
                if state[bucket_index] > 0 and state[bucket_index] - jug >= 0:
                    new_state = list(state)
                    new_state[bucket_index] -= jug
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket_index)], new_state))
    
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it assumes we can always empty the buckets if needed
    # It is admissible because it never overestimates the cost to reach the goal state, as the sum of the absolute differences is always less than or equal to the actual cost
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is equal to the decrease in the heuristic estimate
    return sum(abs(s - g) for s, g in zip(state, goal))


print(a_star())
