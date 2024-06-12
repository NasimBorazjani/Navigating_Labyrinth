
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       ['F', 'I', 'O', 'J', 'K', 'D', 'N', 'R', 'M', 'B'],
       ['0', '0', '0', '1', '1', '0', '0', '0', '1', '0'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['0', '0', '0', '1', '0', '1', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
       ['0', '1', '1', '0', '0', '0', '0', '1', '0', '0'],
       ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0'],
       ['0', '0', '0', '1', '0', '0', '0', '0', '1', '0'],
       ['1', '1', '0', '1', '0', '0', '0', '0', '0', '0'],
       ['1', '0', '0', '1', '0', '1', '0', '0', '1', '0']]


   # Encoding other variables of the problem
   num_cities = 10
   start_city = 'N'
   goal_cities = ['D', 'F']
   goal_count = 2


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, num_cities, start_city, goal_cities, goal_count, visited_costs, queue
  
def a_star():
  
   adj_matrix, num_cities, start_city, goal_cities, goal_count, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       city, d_count, f_count = state


       # If we have visited both goal cities exactly twice, and the current city is the start city, return the path
       if d_count == goal_count and f_count == goal_count and city == start_city:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(1, num_cities):
           if adj_matrix[i][0] == '1':
               # To generate the new state, we must update the counts of the goal cities visited
               # In the new state, the counts of the goal cities visited will include the current city, if it is one of the goal cities
               d_count_new = d_count
               f_count_new = f_count
               if adj_matrix[i][0] == 'D':
                   d_count_new += 1
               elif adj_matrix[i][0] == 'F':
                   f_count_new += 1
               # Generate the new state
               new_state = (adj_matrix[i][0], d_count_new, f_count_new)
               # Cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The city of the new state must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(state, goal_cities, goal_count), new_cost, path + [new_state[0]], new_state))
   return None




def heuristic(state, goal_cities, goal_count):
   # An admissible and consistent heuristic for this problem is the number of cities left to visit, including the goal cities
   # The heuristic relaxes the constraints that we can only visit each city once on our path; ie it presumes we can visit the cities multiple times
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, the decrease in the number of cities left to visit
   return len([city for city in goal_cities if state.count(city) < goal_count])


print(a_star())
