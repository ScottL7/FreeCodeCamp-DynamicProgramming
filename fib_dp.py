"""
    Using memoization to retain previously calculated fib(n)
    Data Structure: Dictionary {n, fib(n) results}
"""


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


print(f'fib(6)={fib(6)}')
print(f'fib(7)={fib(7)}')
print(f'fib(8)={fib(8)}')
print(f'fib(50)={fib(50)}')
