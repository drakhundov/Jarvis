import random


def generate(sz): # TODO: add symbols
	letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

	pw = str()

	while sz > 0:
		if random.randint(0, 1) == 0:
			pw += letters[random.randint(0, 51)]
		else:
			pw += str(random.randint(0, 9))

		sz -= 1

	return pw