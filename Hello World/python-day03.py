#Return statement
# def square(number):
#     return number * number


# print(square(3))

#Creating a Reusable Function
# def emoji_converter(message):
#     words = message.split(" ")
#     emoji = {
#         ":)": "😀",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emoji.get(word, word) + " "
#     return output

# message = input(">")
# print(emoji_converter(message))

#Exceptions
# try:
#     age = int(input('Age: '))
#     income = 2000
#     risk = income / age
#     print(age)
# except ZeeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

#Comments
# print Sky is blue
# print("Sky is blue")

# Calculates and returns the square of a number 
# def square(number):
#     return number * number

#Classes
# class Point:
#     def move(self):
#         print("move")
        
#     def draw(self):
#         print("draw")
        
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

#Constructors
# class Point:
#     def _init_(self, x, y):
#         self.x = x
#         self.y - y
#     def move(self):
#         print("move")
        
#     def draw(self):
#         print("draw")
              
# point = Point(10, 20)
# point.x = 11
# print(point.x)