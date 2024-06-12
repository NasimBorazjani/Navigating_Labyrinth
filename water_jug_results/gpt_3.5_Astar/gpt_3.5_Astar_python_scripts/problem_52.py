
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (253, 337, 385)
    # Define the capacities of the jugs
    jugs = [45, 141, 50, 114, 104, 19, 78, 18, 23, 133]
    # Define the capacities of the buckets
    buckets = [253, 337, 385]
    
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
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(bucket + jug, buckets[bucket_num])
                new_state = tuple(new_state)
                new_cost = g + 1
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket_num + 1)], new_state))
                    
                # Empty the bucket
                new_state = list(state)
                new_state[bucket_num] = 0
                new_state = tuple(new_state)
                new_cost = g + 1
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket_num + 1)], new_state))
    
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it presumes we can move water between buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal amounts in the buckets
    # The cost of the goal state is 0, as the amounts in the buckets match the goal amounts
    
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
