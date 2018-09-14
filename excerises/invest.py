def invest(amount, rate, time):
	print("Principal amount: $", amount)
	print("Annual rate of return:", rate)
	for i in range(1, time + 1):
		amount = amount * (1 + rate)
		print("year {}: ${}".format(i, amount))

invest(100, .05, 8)