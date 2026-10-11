import random
total = int(input("How many random points? "))
inside = 0
i = 0
while i < total:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        inside += 1
    i += 1
pi_approximation = 4 * inside / total
print("Approximation of pi:", pi_approximation)