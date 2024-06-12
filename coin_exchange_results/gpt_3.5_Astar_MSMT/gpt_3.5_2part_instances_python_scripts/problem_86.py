
import heapq

def initialize():
    coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
    tax_values = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
    target_sum = 490
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
