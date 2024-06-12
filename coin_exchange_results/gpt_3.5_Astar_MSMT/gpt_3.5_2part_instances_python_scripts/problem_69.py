
import heapq

def initialize():
    coins = [28, 11, 40, 15, 21, 6, 20, 6, 12, 22, 8, 18, 34, 24, 22, 30, 35, 41, 6, 39, 5, 15, 19, 8, 26, 38, 11, 29, 31, 14, 37, 28, 8, 11, 28, 27, 38]
    tax_values = {40: 1, 41: 13, 8: 5, 28: 2, 21: 18, 15: 7, 5: 4, 14: 13, 37: 12, 22: 12, 29: 3, 30: 15, 35: 4, 26: 19, 39: 7, 31: 14, 11: 7, 20: 3, 6: 2, 12: 8, 27: 13, 19: 19, 34: 5, 18: 9, 38: 16, 24: 17}
    target_sum = 423
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
