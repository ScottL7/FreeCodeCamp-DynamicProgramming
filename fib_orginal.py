def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(f'fib(6)={fib(6)}')
print(f'fib(7)={fib(7)}')
print(f'fib(8)={fib(8)}')
print(f'fib(50)={fib(50)}')
