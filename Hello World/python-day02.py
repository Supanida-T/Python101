#While Loop
# i = 1
# while 1 <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")

#Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won')
#         break
# else: 
#     print('Sorry you false')

#Car Game
# command = ""
# started = False
# while True:
#     command = input("> ")
#     if command.lower() == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#         print("Car started...")
#     elif command.lower() == "stop":
#         if not started:
#             print("Car is already stopped!")
#         print("Car stopped.")
#     elif command == "help":
#         print("""
#             start - to start the car
#             stop - to stop the car
#             quit - to quit
#             """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understad the command")

#For Loop
# for item in ['Tonmint', 'Tar', 'Not']:
#     print(item)
    
# for item in range(10):
#     print(item)
    
# for item in range(5, 10):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total = total += price
# print(f"Total: {total}")

#Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y}')

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

#Lists
# names = ['Tonmint', 'Tar', 'Mosh', 'Sarah', 'Bob']
# names[0] = 'Jon'
# print(names)
# print(names[2:4])

# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0] [1] = 20
# print(matrix[0] [1])
# for row in matrix:
#     for item in row:
#         print(item)

#List Methods
# numbers = [5, 2, 1, 7,4]
# numbers.append(5)
# numbers.pop(0)
# numbers.index()
# print(numbers)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

#Tuples
# numbers = (1, 2, 3)
# numbers [0] = 10
# print(numbers[0])

#Unpacking
# coordinates = (1, 2, 3)
# x, y, z = coordinates 
# print(y)

#Dictionaries
# customer = {
# "name": "Tonmint",
# "age": 20,
# "is_verified": True
# }
# customer["birthday"] = "Jan 1 1980"
# print(customer["birthday"])

#Emoji Converter
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😀", 
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, words) + " "
# print(output)

#Functions
# def greet_user(name):
#     name = "John"
#     print(f'Hi {name}')
#     print('Welcome aboard')
    
    
# print("Start")
# greet_user("John")
# print("Finish")