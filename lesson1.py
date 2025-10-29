# # name = "Саша"
# # print("Дима")
# # print("Привет, " + name)
# # print("Как прошел день, " + name)
# # random_bool = True
# # print(random_bool)

# # names = ["Дима", "Саша", "Вика"]
# # print(names)

# names = [
#     "Дима",
#     "Саша",
#     "Вика"]
# # length_of_list = len(names)
# print(len(names))  # выведет: 3

# def add(a, b):
#     return a + b
# result = add(3, 5)
# print(result)

# def add(a, b):
#     return a - b
# result = add(8, 3)
# print(result)

# # name = "John"
# # age = 25
# # text = "Меня зовут {name}, мне {age} лет."
# # result = text.format(name=name, age=age)
# # print(result)

# # names = [
# #     "Дима",
# #     "Саша",
# #     "Вика"]
# # print(names[0])
# # print(names[-1])

# def greet(name):
# 	print("Привет," + name)

# greet("Alex")


globalVar = 1

def printGlobal():
	print(globalVar)

def printLocal():
	local = 2
	print(local)

printGlobal()
printLocal()