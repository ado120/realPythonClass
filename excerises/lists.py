desserts = ['ice cream', 'cookies']
desserts.sort()
print(desserts)

food = desserts[:]
food.append('broccoli')
food.append('turnip')
print(desserts)
print(food)

food.remove('cookies')
print(food[0:2])

breakfast = "cookies, cookies, cookies"
breakfast_list = breakfast.split(', ')
print(breakfast_list)

def list_numbers(list_of_nums):
	for i in list_of_nums:
		if i > 0 and i < 21:
			print(i)

list_of_numbers = [2, 4, 8, 16, 32, 64]
list_numbers(list_of_numbers)