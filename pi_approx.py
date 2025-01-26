import random
import math

def estimate_pi(num_samples):
    num_inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_inside_circle += 1
    return 4 * num_inside_circle / num_samples

num_samples = 1000000
pi_estimate = estimate_pi(num_samples)
print("Estimated value of pi:", pi_estimate)
print("Actual value of pi:", math.pi)
print("Error:", abs(pi_estimate - math.pi))