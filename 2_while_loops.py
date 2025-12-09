# # notes on while loops
# # while smth true = while loop keep runing

# name = input("Enter your name: ")
# if name == "":
#     print("You did not enter a name.")
# else:
#     print(f"Hello {name}")

# # WHile loop!!!!
# # infintae loop =  if you dont put anything it will run forever

# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter a name.")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# # example 2

# age  = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative.")
#     age  = int(input("Enter your age: ")) # gives user a chance to escape the loop
# print(f"You are {age} years old.)

# #example 3:

# food  = input("Enter a food you like (q to quit)")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit)")
# print("Bye.")
# foods = []
# food  = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     foods.append(food)
#     food = input("Enter a food you like (q to quit): ")
# print(foods)

# # example 4

# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print("Your number is not valid")
#     num = int(input("Enter a number between 1 - 10: "))
# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1 # prevents infinate loop