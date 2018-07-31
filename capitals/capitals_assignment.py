from capitals import capitals_dict
import random

def capitals_game(state, capital):
	while True:
		guess = input("What is the capital of {}?\n".format(state)).lower()
		if guess == capital.lower():
			print("Correct")
			break
		elif guess == "exit":
			print("The capital of {} is {}".format(state, capital))
			break




state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capitals_game(state, capital)

