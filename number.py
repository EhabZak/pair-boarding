def fibonacci(length):
    fib_sequence = [0, 1]
    if length <= 2:
        return fib_sequence[:length]
    for i in range(2, length):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(fibonacci(10))

# from itertools import islice
# def fibonacci_generator(c):
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# print(list(islice(fibonacci_generator(10), 10)))
