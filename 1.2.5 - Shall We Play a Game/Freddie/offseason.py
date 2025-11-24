import random as rand
global week
week = 1
upDown = 1
milage = 20

def weekPicker():
  global week, upDown, milage
  for i in range(12):
    print(upDown)
    if upDown == 5:
      upDown = 0
    print("Week " + str(week))
    if week != 12:
      print("Weekly milage is " + str(round(milage)))
    else:
      print("Weekly milage is 0")
    upDown = upDown + 1
    if upDown < 5:
      milage = 1.1*milage
    else: 
      milage = milage/1.1

    if i == 0:
      weeklyWorkout1 = "Repititions"
      weeklyWorkout2 = "Threshold"
    if i == 1:
      weeklyWorkout1 = "Intervals"
      weeklyWorkout2 = "Hill Repeats"
    if i == 2:
      weeklyWorkout1 = "Threshold"
      weeklyWorkout2 = "Intervals"
    if i == 3:
      weeklyWorkout1 = "Hill Repeats"
      weeklyWorkout2 = "Repititions"
    if i == 4:
      weeklyWorkout1 = "Intervals"
      weeklyWorkout2 = "Repititions"
    if i == 5:
      weeklyWorkout1 = "Threshold"
      weeklyWorkout2 = "Hill Repeats"
    if i == 6:
      weeklyWorkout1 = "Repititions"
      weeklyWorkout2 = "Threshold"
    if i == 7:
      weeklyWorkout1 = "Intervals"
      weeklyWorkout2 = "Hill Repeats"
    if i == 8:
      weeklyWorkout1 = "Threshold"
      weeklyWorkout2 = "Intervals"
    if i == 9:
      weeklyWorkout1 = "Hill Repeats"
      weeklyWorkout2 = "Repititions"
    if i == 10:
      weeklyWorkout1 = "Intervals"
      weeklyWorkout2 = "Repititions"
    if i == 11:
      weeklyWorkout1 = "Threshold"
      weeklyWorkout2 = "Hill Repeats"
    if i / 8 == 1:
      print("Monday Rest")
      print("Tuesday Rest")
      print("Wednesday Rest")
      print("Thursday Rest")
      print("Friday Rest")
      print("Saturday Rest")
      print("Sunday Rest")
      print("")
    if i % 2 == 0:
      print("Monday Easy")
      print("Tuesday " + weeklyWorkout1)
      print("Wednesday Easy")
      print("Thursday " + weeklyWorkout2)
      print("Friday Easy")
      print("Saturday Long")
      print("Sunday Rest")
    else: 
      print("Monday " + weeklyWorkout1)
      print("Tuesday Easy")
      print("Thursday " + weeklyWorkout2)
      print("Thursday Easy")
      print("Friday Easy")
      print("Saturday Long")
      print("Sunday Rest")
    print("")
    week = week + 1

for i in range(3):
  print(upDown)
  print("Week " + str(week))
  print("Weekly milage is " + str(round(milage)))
  print("Monday Easy")
  print("Tuesday Easy")
  print("Wednesday Easy")
  print("Thursday Easy")
  print("Friday Easy")
  print("Saturday Long")
  print("Sunday Rest")
  print("")
  week = week + 1
  upDown = upDown + 1
  milage = milage + milage/10

weekPicker()

print(upDown)
print("Week " + str(week))
print("Weekly milage is " + str(round(milage)))
print("Monday Easy")
print("Tuesday Repititions")
print("Wednesday Easy")
print("Thursday Threshold")
print("Friday Easy")
print("Saturday Long")
print("Sunday Rest")
print("")
