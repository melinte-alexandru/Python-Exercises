# 1. Fibonacci
def fibonacci(n):
    res = [0, 1]
    for i in range(2, n):
        res.append(res[-1] + res[-2])
    return res[:n]

   # 1*. N-term Fibonacci
def n_term_fibonacci(num_terms, n):
    res = [0] * (n - 1) + [1]
    for i in range(n, num_terms):
        res.append(sum(res[-n:]))
    return res[:num_terms] 