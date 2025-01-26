import random
import math

def estimate_pi_monte_carlo(num_samples):
    num_inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_inside_circle += 1
    return 4 * num_inside_circle / num_samples

def estimate_pi_gregory_leibniz(num_terms):
    pi = 0.0
    sign = 1.0
    for i in range(num_terms):
        term = sign / (2 * i + 1)
        pi += term
        sign *= -1.0
    return pi * 4

def main():
    print("Select an option:")
    print("1. Monte Carlo method")
    print("2. Gregory-Leibniz series")
    option = input("Enter option: ")

    if option == "1":
        num_samples = int(input("Enter number of samples: "))
        pi_estimate = estimate_pi_monte_carlo(num_samples)
    elif option == "2":
        num_terms = int(input("Enter number of terms: "))
        pi_estimate = estimate_pi_gregory_leibniz(num_terms)
    else:
        print("Invalid option.")
        return

    print("Estimated value of pi:", pi_estimate)
    print("Actual value of pi:", math.pi)
    print("Error:", abs(pi_estimate - math.pi))

if __name__ == "__main__":
    main()