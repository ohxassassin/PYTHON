#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
current_year = 2023 
turn_100_year = current_year + (100 - age)
print(f"Hello, {name} You will turn 100 years old in the year {turn_100_year}.")
