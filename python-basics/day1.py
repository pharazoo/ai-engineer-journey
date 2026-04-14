print("Day 1 - AI Engineer Journey Started")

name = "Faraz"
age = 47
city = "San Leandro"
weight = 200
goal_weight = 180
height_ft = 6

height_in = height_ft * 12

bmr = (4.54 * weight) + (15.88 * height_in) - (5 * age) + 5
print("BMR is ", bmr)