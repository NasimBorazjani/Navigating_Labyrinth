#trampoline_matrix

import math

class Search_Node():
   def __init__(self, parent=None, position=None):
        self.parent = parent
        #parameters of a game state
        #in this case the position of the current trampoline in the grid of trampolines encoded as (x, y)
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

   def __eq__(self, other):
       return self.position == other.position


def initialize():
   #any actions required to start the game
   #create start and end node
   
    trampoline_map = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (8, 8)
    
    start_node = Search_Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Search_Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    
    return trampoline_map, start_node, end_node



def is_final_state(node, end_node):
  
   #if we are at a final state
   if node == end_node:
       path = []
       current = node
       # creating a list of intermediate node names as the solution 
       while current is not None:
           path.append(current.position)
           current = current.parent
       return path[::-1]



def generate_children_nodes(trampoline_map, parent_node):
   #generate children
  
   children = []
   #adjacent positions
   for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        #calculate child node position
        child_position = (parent_node.position[0] + new_position[0], parent_node.position[1] + new_position[1])

        # Make sure within range
        if child_position[0] > (len(trampoline_map) - 1) or child_position[0] < 0 or child_position[1] > (len(trampoline_map[len(trampoline_map)-1]) -1) or child_position[1] < 0:
            continue

        # Make sure walkable terrain
        if trampoline_map[child_position[0]][child_position[1]] != 0:
            continue

        new_node = Search_Node(parent_node, child_position)
        children.append(new_node)
      
   return children



def cost(parent_node):
   #cost of getting to the child node
   child_cost = parent_node.g + 1
   return child_cost



def heuristic_cost_estimate(child_node, end_node):
   #in this case the heuristic is euclidean dist (consistent)
   child_heuritic = math.hypot((child_node.position[0] - end_node.position[0])
                    , (child_node.position[1] - end_node.position[1]) )
  
   return child_heuritic



def astar():

    trampoline_map, start_node, end_node = initialize()

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    open_list.append(start_node)

    #Astar loop
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        path = is_final_state(current_node, end_node)
        if path:
            return path
        
        #generate children
        children = generate_children_nodes(trampoline_map, current_node)

        for child in children:
        
            # Create the f, g, and h values
            child.g = cost(current_node)
            child.h = heuristic_cost_estimate(child, end_node)
            child.f = child.g + child.h
            
            skip_child = False
            for closed_child in closed_list:
                if child == closed_child and closed_child.f < child.f:
                    skip_child = True
                    break  

            for open_node in open_list:
                if child == open_node and open_node.f < child.g:
                    skip_child = True
                    break  

            if not skip_child:
                open_list.append(child)
            

def main():
    path = astar()
    print(path)
    
main()