import random
from print_inline import print_inline

sides = []
one = ' _____\n|     |\n|     |\n|  O  |\n|     |\n|_____|'
two = ' _____\n|     |\n| O   |\n|     |\n|   O |\n|_____|'
three = ' _____\n|     |\n| O   |\n|  O  |\n|   O |\n|_____|'
four = ' _____\n|     |\n| O O |\n|     |\n| O O |\n|_____|'
five = ' _____\n|     |\n| O O |\n|  O  |\n| O O |\n|_____|'
six = ' _____\n|     |\n| O O |\n| O O |\n| O O |\n|_____|'

sides.append(one)
sides.append(two)
sides.append(three)
sides.append(four)
sides.append(five)
sides.append(six)

def roll():
	num = random.randint(1, 6)
	return num
	
def roll_dice(num_dice):
	total = 0
	results = []
	for i in range(num_dice):
		num = roll()
		results.append(num)
		print(sides[num-1])
		total += num
	print("You rolled: " + str(results))
	print("Total: " + str(total))
