# Day 2 Lab

print("=====Food and Calories Tracker=====")

foods = ["eggs", "chicken breast", "salad"]

calories = [280, 400, 150]

print(foods[0], "-", calories[0], "calories")
print(foods[1], "-", calories[1], "calories")
print(foods[2], "-", calories[2], "calories")

total = calories[0] + calories[1] + calories[2]
print("Total Calories: ", total)

if total > 2000:
    print("Too many calories")
else:
    print("Good calorie intake")