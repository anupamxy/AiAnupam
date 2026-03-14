# infinite generator is a generator that can produce an infinite sequence of values. It is typically implemented using a while loop that never terminates, yielding values indefinitely. Here's an example of an infinite generator that produces the Fibonacci sequence:
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# fib_gen = fibonacci()
# for _ in range(10):
#     print(next(fib_gen))

def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1
counter = infinite_counter()
counter1 = infinite_counter()
for _ in range(10):
    print(next(counter))
    
for _ in range(10):
    print(next(counter1))
    
# sending data to a generator
def echo():
    while True:
        received = yield
        print(f"Received: {received}")
echo_gen = echo()
next(echo_gen)  # Start the generator
echo_gen.send("Hello, generator!")  # Send data to the generator
# close the generator
echo_gen.close()