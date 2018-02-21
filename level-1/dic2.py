def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
a = int(input('enter n: '))
print(list(fib(a)))