# Day 2 Lab

print("=====Food and Calories Tracker=====")

foods = ["eggs", "chicken", "rice", "mixed vegies", "Sandwich", "Coffee"]
calories = [364, 204, 204, 42, 420, 280]

for i in range(len(foods)):
    print(f"{foods[i]} → {calories[i]} calories")

total = 0

for x in range(len(calories)):
    total += calories[x]
print("Total calories consumed = ", total)

if total > 2000:
    print("You have consumed more than 2000 calories today. Consider exercising to burn some calories.")
else:
    print("You have consumed less than 2000 calories today. Keep up the good work!")