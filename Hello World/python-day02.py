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