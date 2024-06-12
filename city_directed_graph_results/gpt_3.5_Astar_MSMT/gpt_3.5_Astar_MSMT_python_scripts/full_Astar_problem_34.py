
import heapq


def initialize():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are the connections to other cities
   adjacency_matrix = {
       'J': {'N': 1},
       'S': {'W': 1, 'G': 1},
       'T': {'B': 1},
       'W': {'J': 1, 'S': 1, 'G': 1, 'P': 1, 'U': 1},
       'G': {'S': 1, 'W': 1, 'B': 1},
       'N': {'T': 1, 'W': 1, 'G': 1, 'P': 1, 'U': 1},
       'M': {'W': 1},
       'Z': {'N': 1, 'B': 1, 'U': 1},
       'B': {'J': 1, 'G': 1, 'Z': 1},
       'P': {'T': 1, 'N': 1, 'U': 1},
       'U': {'S': 1, 'W': 1, 'N': 1}
   }
  
   # Define the start city and the cities to visit twice
   start_city = 'T'
   cities_to_visit_twice = ['N', 'W']
  
   # Initialize the visited_costs dictionary with the start city and a cost of 0
   visited_costs = {}
   visited_costs[start_city] = 0
  
   # Initialize a priority queue with the start city as the first element
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, cities_to_visit_twice, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, cities to visit twice)
   adjacency_matrix, start_city, cities_to_visit_twice, visited_costs, queue = initialize()


   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # Check if we have visited all cities twice
       if all(city in path for city in cities_to_visit_twice):
           return path

       # Generate all possible actions from the current city, which are the cities directly connected to the current city
       for next_city in adjacency_matrix[current_city]:
           # Check if the next city has not been visited yet to avoid revisiting cities
           if next_city not in path:
               # Calculate the new cost by adding the cost of moving to the next city
               new_cost = g + 1
               # Update the path with the next city
               new_path = path + [next_city]

               # If the new city is one of the cities to visit twice, double the cost as we need to visit it twice
               if next_city in cities_to_visit_twice:
                   new_cost *= 2

               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, new_path, next_city))
                  
   return None


print(a_star())
