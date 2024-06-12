
import heapq

def initialize():
    coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
    tax_values = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}
    target_sum = 427
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
