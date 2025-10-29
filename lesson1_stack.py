def funcA():
	print("Начали выполнять А")
	funcB()
	print("Закончили выполнять А")

def funcB():
	print("Начали выполнять B")
	funcC()
	print("Закончили выполнять B")

def funcC():
	print("Начали выполнять C")
	funcD()
	print("Закончили выполнять C")

def funcD():
	print("Начали выполнять D")
	print("Закончили выполнять D")

funcA()