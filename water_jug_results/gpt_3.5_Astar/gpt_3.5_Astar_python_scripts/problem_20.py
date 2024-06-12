
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (256, 355, 434)
    # Define the capacities of the jugs
    jugs = [35, 48, 114, 16, 77, 53, 76, 115, 29, 93]
    # Define the capacities of the buckets
    buckets = [256, 355, 434]
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Generate all possible actions from the current state
        for jug in jugs:
            for bucket_num, bucket in enumerate(state):
                # Fill the bucket from the jug
                new_state = list(state)
                new_state[bucket_num] = min(bucket + jug, buckets[bucket_num])
                # Check if the new state is valid
                if new_state[bucket_num] >= state[bucket_num]:
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket_num)], new_state))
        
        for bucket_num, bucket in enumerate(state):
            # Empty the bucket
            new_state = list(state)
            new_state[bucket_num] = 0
            new_state = tuple(new_state)
            new_cost = g + 1
            
            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                visited_costs[new_state] = new_cost
                heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', 0, bucket_num)], new_state))
    
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, presuming we can always empty the buckets if needed
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal amounts
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
