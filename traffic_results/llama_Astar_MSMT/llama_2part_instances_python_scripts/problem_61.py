
import heapq

def initialize():
    initial_state = (('13', '13', '16', '8', 'x', '19', '1', '18', '13', '8', 'x', '7', 'x'), ('x', '13', 'x', '15', 'x', '12', '20', '1', '13', '19', '4', '17', 'x'), ('x', '12', '9', '11', '13', '12', '2', '12', '19', '5', '19', '16', '8'), ('x', '12', '18', '19', 'x', '7', 'x', '12', '3', '2', 'x', '16', '11'), ('x', '7', 'x', 'x', '8', '13', '15', '3', '1', 'x', '15', '15', 'x'), ('11', '9', 'x', '16', '2', '10', '1', '2', '16', '1', 'x', '10', '12'), ('x', 'x', '9', '9', '7', 'x', '6', 'x', 'x', '10', '7', '2', 'x'), ('x', '13', '10', '8', '1', '11', 'x', 'x', 'x', 'x', 'x', 'x', 'x'), ('11', '14', 'x', 'x', 'x', 'x', '4', '8', 'x', 'x', '18', 'x', 'x'), ('13', '14', 'x', '10', 'x', 'x', '16', 'x', 'x', 'x', 'x', 'x', 'x'), ('x', 'x', '16', 'x', '10', 'x', '17', 'x', 'x', 'x', 'x', '10', 'x'), ('9', 'x', '10', '19', '16', 'x', '6', '9', 'x', 'x', '8', '11', 'x'))
    start_workshop = (3, 12)
    end_workshop = (6, 2)
    districts = [(0, 3), (4, 5), (6, 9)]
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
