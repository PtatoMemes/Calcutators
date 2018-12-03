while True:
	top = int(input('Type the top Number: '))
	bottom = int(input('Type the bottom Number: '))
	percent = (top - (top - 1)) / bottom
	answer = percent * top
	print(round(answer, 3))