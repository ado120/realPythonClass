from random import randint

trial = 10000
total = 0
for roll in range(0,trial):
	total += randint(1,6)

avg_result = total/trial

print("the average result of the tosses is {}".format(avg_result))

