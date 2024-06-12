
import heapq

def initialize():
    initial_state = (('x', 'x', 'x', 'x', 'x', '8', '15', '18', '10'), ('4', '5', '10', '6', '20', '2', '12', 'x', 'x', 'x'), ('19', '6', '19', '7', '6', '2', 'x', '15', 'x', '14'), ('16', '17', 'x', '2', '3', '7', '4', 'x', '18', '6'), ('x', '2', '1', '19', '7', '10', '18', '5', '3', '19'), ('8', '5', 'x', '1', 'x', '10', '17', 'x', '13', '5'), ('18', '1', '3', '4', 'x', 'x', '8', 'x', '5', 'x'), ('15', 'x', 'x', '13', 'x', '11', 'x', '2', 'x', 'x'), ('4', 'x', 'x', '4', '1', 'x', 'x', 'x', 'x', 'x'), ('x', '10', '8', 'x', 'x', '7', '19', 'x', 'x', 'x'))
    start_workshop = (5, 8)
    end_workshop = (3, 0)
    districts = [(0, 2), (3, 4), (5, 9)]
    moves = [((- 1), 0), (1, 0), (0, (- 1)), (0, 1)]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], start_workshop)]
    return (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue)

def a_star():
    (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, current_workshop) = heapq.heappop(queue)
        if (current_workshop == end_workshop):
            return actions
        for move in moves:
            new_workshop = ((current_workshop[0] + move[0]), (current_workshop[1] + move[1]))
            if ((0 <= new_workshop[0] < len(initial_state)) and (0 <= new_workshop[1] < len(initial_state[0])) and (initial_state[new_workshop[0]][new_workshop[1]] != 'x') and any(((district[0] <= new_workshop[0] <= district[1]) for district in districts)) and any(((district[0] <= current_workshop[0] <= district[1]) for district in districts))):
                new_cost = (g + 1)
                if ((new_workshop not in visited_costs) or (new_cost < visited_costs[new_workshop])):
                    visited_costs[new_workshop] = new_cost
                    h = heuristic(new_workshop, end_workshop)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [new_workshop]), new_workshop))
    return None

def heuristic(current_workshop, end_workshop):
    return ((((current_workshop[0] - end_workshop[0]) ** 2) + ((current_workshop[1] - end_workshop[1]) ** 2)) ** 0.5)
print(a_star())
