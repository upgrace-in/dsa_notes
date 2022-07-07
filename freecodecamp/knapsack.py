def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        opt1 = max_profit_recursive(weights, profits, capacity, idx+1)
        opt2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
        return max(opt1, opt2)
        
def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(n):
        for c in range(1, capacity+1):
            if weights[i] > c:
                table[i+1][c+1] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], 
                                    profits[i] + table[i][c-weights[i]])
    return table[-1][-1]
    
print(max_profit_dp([4,5,1,3,2,5], [2,3,1,5,4,7], 15))