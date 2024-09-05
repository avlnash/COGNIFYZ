def generate_fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = generate_fibonacci(num_terms)
    print(f"Fibonacci sequence up to {num_terms} terms: {fib_sequence}")
