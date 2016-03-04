error = True
while error == True:
	number = input("What number should I double? ")

	try: 
		number = float(number)
	except ValueError:
			print("Sorry, that's not a number.")
			error = True

	else:
		print("{} doubled is {}".format(number, number * 2))
		error = False