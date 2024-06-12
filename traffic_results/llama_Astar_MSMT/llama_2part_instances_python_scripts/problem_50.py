
import heapq

def initialize():
    initial_state = (('x', '12', '17', '10', 'x', 'x', 'x', '9', '15', '5'), ('x', 'x', 'x', 'x', 'x', '12', '20', '9', '19', '8'), ('9', 'x', 'x', '2', 'x', '2', '1', '9', '8', '14'), ('19', 'x', '1', '20', '7', '9', '18', 'x', '18', '7'), ('5', '2', '11', '9', 'x', '5', '4', '16', 'x', '1'), ('10', '8', '8', '4', '11', '11', 'x', 'x', '5', 'x'), ('15', '15', 'x', 'x', '13', '5', '19', 'x', 'x', '15'), ('15', '16', '9', '18', 'x', 'x', '16', 'x', 'x', 'x'), ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'), ('x', 'x', '14', '14', 'x', 'x', '15', '6', '6', 'x'), ('x', 'x', 'x', 'x', '8', '14', 'x', '5', 'x', 'x'), ('x', '6', '15', 'x', 'x', 'x', 'x', 'x', '8', 'x'))
    start_workshop = (0, 9)
    end_workshop = (7, 1)
    districts = [(0, 3), (4, 6), (7, 11)]
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
