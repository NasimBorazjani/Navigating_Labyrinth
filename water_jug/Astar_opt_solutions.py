from heapq import heappush, heappop
import sys

def a_star(jugs, goal_state):
  goal_state = tuple(goal_state)
  initial_state = tuple([0] * len(goal_state))
  num_buckets = len(goal_state)

  # Initialize a dictionary to store the cost of reaching each visited state
  visited_costs = {}
  visited_costs[initial_state] = 0

  # Initialize a priority queue with the initial cost + heuristic, cost, actions and state
  queue = []
  heappush(queue, (0, 0, [], initial_state))  

  while queue:
      #print(num_states_generated, end = " ")
      _, g, actions, state = heappop(queue)

      # If the current state is the goal state, return the actions that led to it
      if state == goal_state:
          return actions

      # Generate all possible actions from the current state, which includes adding or subtracting water using any of the 6 jugs to any of the 3 buckets
      for jug in jugs:
          for bucket_ind in range(num_buckets):
              # Check if adding water using the current jug results in a valid state without overflowing any of the buckets
              if (state[bucket_ind] + jug <= goal_state[bucket_ind]):
                  temp_state = list(state)[:]
                  temp_state[bucket_ind] += jug
                  # Check if the new state maintains the constraint on the relative amount of water in the buckets based on their order
                  if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                      new_state = tuple(temp_state)
                      new_cost = g + 1
                      # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                      if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                          visited_costs[new_state] = new_cost
                          h = heuristic(state, goal_state, jugs)
                          heappush(queue, (g + h, g + 1,  actions + [('+', jug, bucket_ind+1)], new_state))

              # Check if removing water using the current jug is possible
              if state[bucket_ind] - jug >= 0:
                  temp_state = list(state)[:]
                  temp_state[bucket_ind] -= jug
                  if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                      new_state = tuple(temp_state)
                      if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                          visited_costs[new_state] = new_cost
                          h = heuristic(state, goal_state, jugs)
                          heappush(queue, (g + h, g + 1, actions + [('-', jug, bucket_ind+1)], new_state))
  return None


def heuristic(buckets_state, buckets_goal, jugs):
   h = 0
   jugs = sorted(jugs, reverse=True)
   for i in range(len(buckets_state)):
       bucket_fill = buckets_state[i]
       goal = buckets_goal[i]
       # Fill the bucket using the largest jug possible as long as the bucket does not overflows
       for jug in jugs:
           while bucket_fill + jug < goal:
               bucket_fill +=  jug
               h += 1 
   return h

import time

def main():
    # Read the initial state from the command line
    
    jugs = eval(sys.argv[1])
    goal_state = eval(sys.argv[2])
    
    final_answer = []
    
    for i in range(len(goal_state) -1, -1, -1):
        answer_this_bucket = a_star(jugs, [goal_state[i]])
        answer_this_bucket = list(list(item) for item in answer_this_bucket)
        for a in answer_this_bucket:
            a[2] = i + 1
        answer_this_bucket = tuple(tuple(item) for item in answer_this_bucket)
        final_answer += answer_this_bucket
        
    print(final_answer)

    """start_time = time.time()
    print(a_star(jugs, goal_state))
    end_time = time.time()

    print(end_time - start_time)"""
    
if __name__ == "__main__":
    main()