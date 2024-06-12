
import heapq

def initialize():
    coins = [19, 11, 3, 37, 9, 29, 42, 12, 2, 13, 15, 11, 25, 14, 31, 17, 24, 45, 5, 18, 42, 21, 28, 23, 26, 40, 27, 42, 12, 13, 16, 14, 31, 38, 9, 24, 27, 36, 13, 27, 15, 43, 9, 14, 34, 7, 15, 12, 31, 44]
    tax_values = {37: 7, 45: 7, 29: 6, 27: 2, 2: 2, 40: 6, 13: 9, 17: 2, 9: 2, 15: 12, 36: 2, 26: 18, 44: 5, 42: 4, 38: 8, 43: 2, 12: 4, 24: 20, 28: 15, 16: 7, 21: 13, 23: 5, 19: 4, 25: 16, 3: 2, 18: 13, 34: 16, 31: 2, 5: 4, 14: 2, 7: 1, 11: 8}
    target_sum = 449
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
