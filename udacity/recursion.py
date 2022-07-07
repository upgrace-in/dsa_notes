"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # 0 1 1 2 3 5 8 13 21
    if position == 0:
        return 0
    count = 0
    series = []
    series.append(0)
    def populate_series(count, prev_num, next_num, position, series):
        if count != position:
            series.append(next_num)
            num = prev_num + next_num
            prev_num = next_num
            populate_series(count+1, prev_num,  num,  position, series)
        else:
            return series
    populate_series(count, 0, 1, position, series)
    return series[position]

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
