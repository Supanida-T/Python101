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