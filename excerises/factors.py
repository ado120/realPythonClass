factors = int(input("Enter a positive integer: "))

def find_factors(factors):
	for divisor in range(1, factors + 1):
		if factors % divisor == 0:
			print(f"{divisor} is a divisor of {factors}")

find_factors(factors)