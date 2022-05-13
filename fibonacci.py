def fibonnaci(num):
	try:
		num=int(num)
	except:
		print("Invalid Input")
	else:
		a, b = 0, 1
		print("1:", a)
		print("2:", b)
		
		for i in range(3, num+1):
			b = a + b
			a = b - a
			print(f"{i}: {b}")


if __name__=="__main__":
	userInput=input("Enter the position of the fibonnaci number you want: ") or 10
	fibonnaci(userInput)