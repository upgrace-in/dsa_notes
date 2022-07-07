s = ["h","e","l","l","o"]
m = 0
n = len(s)-1
d = [i for i in s]

def reverse_it(data, m, n):
    if m == len(data):
        return None
    reverse_it(data, m+1, n-1)
    data[m] = d[n]

# reverse_it(s, m, n)
print(5//2)
