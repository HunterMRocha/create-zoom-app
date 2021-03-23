import random 

volunteers = ["Hunter", "William", "Le", "Miguel"]
students = ["DeJohn", "Jessica", "Dexian", "Lexian", "Rafa", "Eunbi", "Yixi", "Griffin", "Cindy", "Sabeen", "Christine", "Agnes"]

br1 = []
br2 = []
br3 = []
br4 = []

# step 1: Assign an instructor to every room so each room has someone you can ask for help
random.shuffle(volunteers) # this function will shuffle the order of volunteers
br1.append(volunteers.pop())
br2.append(volunteers.pop())
br3.append(volunteers.pop())
br4.append(volunteers.pop())

# step 2: Assign a student to each breakout room 
remaining_students = len(students)
while remaining_students > 0: 
  rc = random.choice(students) # this will store out random student so we can use access them multiple times 
  br1.append(rc)
  remaining_students -= 1
  students.remove(rc)

  rc = random.choice(students) # this will store out random student so we can use access them multiple times 
  br2.append(rc)
  remaining_students -= 1
  students.remove(rc)

  rc = random.choice(students) # this will store out random student so we can use access them multiple times 
  br3.append(rc)
  remaining_students -= 1
  students.remove(rc)

  rc = random.choice(students) # this will store out random student so we can use access them multiple times 
  br4.append(rc)
  remaining_students -= 1
  students.remove(rc)

print(br1)
print(br2)
print(br3)
print(br4)


'''
Questions: 
What's wrong with this code? 
What if we wanted to add a breakout room 
	if we added another breakout room would we need to write something like br5.append(rc)... 
	what if we added 15 breakout rooms? our while loop would be so messy. How can we fix this?
What if we wanted to remove a student from a certain room
What if we wanted to move a student from one room to another 
'''