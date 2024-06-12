
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled with the specified amounts of water
    goal_state = (232, 401, 444, 451)
    # Define the capacities of the water jugs
    jugs = [56, 81, 132, 41, 86, 128, 57, 138]
    # Define the buckets in ascending order
    buckets = [232, 401, 444, 451]
    
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
            for i in range(4):
                # Fill the ith bucket with the jug
                new_state = list(state)
                new_state[i] = min(buckets[i], new_state[i] + jug)
                # Check if the new state is valid
                if new_state[i] <= buckets[i]:
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, i+1)], new_state))
        
        for i in range(4):
            for jug in jugs:
                # Empty the ith bucket using the jug
                new_state = list(state)
                new_state[i] = 0
                # Check if the new state is valid
                if new_state[i] <= buckets[i]:
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, i+1)], new_state))
    
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    return sum(abs(s - g) for s, g in zip(state, goal))


print(a_star())
