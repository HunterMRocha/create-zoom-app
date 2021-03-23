import random

'''
In this version we're going to create functions:
Main Function: This is where all of the Main logic will take place :)
Function 1: Create a function in charge of adding students to a breakout room (aka a list)
Function 2: Create a function in charge of removing students from the student list 

'''

def add_to_room(student_name, breakout_room):
  '''
  student Name: Represents which students we want to add
  breakout_room: Represents which breakout room we want to add to
  Return: Our updated breakout room with our newly added student
  '''
  breakout_room.append(student_name)
  return breakout_room

def remove_from_list(student_name, student_list):
  '''
  student Name: Represents which students we want to add
  student_list: Represents our entire list of students
  '''
  student_list.remove(student_name)
  return student_list

def main():
  br_1 = []
  br_2 = []
  br_3 = []
  br_4 = []
  
  # now if we add a breakout room we can just add it to a list that keeps track of every other list
  all_rooms = [br_1, br_2, br_3, br_4] # list of every single room 

  # volunteers2 = ["Hunter", "William", "Le", "Miguel"]
  students2 = ["DeJohn", "Jessica", "Dexian", "Lexian", "Rafa", "Eunbi", "Yixi", "Griffin", "Cindy", "Sabeen", "Christine", "Agnes"]
  random.shuffle(students2) # this function will shuffle the order of volunteers (not really necc. if we're using random.choice though)

  number_of_students = len(students2) # how many students do we have
  total_rooms = len(all_rooms) # how many rooms do we have available
  current_room = 0 # what breakout room idex are we currently adding to

  while(number_of_students > 0):
    # this check will make sure we continue looping through every single breakout room multiple times
    if current_room > total_rooms-1: 
      current_room = 0

    random_student = random.choice(students2)
    add_to_room(random_student, all_rooms[current_room]) # now instead of doing stuff like br3.append() we can just call this function to add to a certain room 
    remove_from_list(random_student, students2)

    number_of_students -= 1
    current_room += 1
    
  print(br_1)
  print(br_2)
  print(br_3)
  print(br_4)



main()



















'''
Questions: 
Now how can we clean this up even more? 
HINT: we don't want to have a lot of logic going on inside of our main function, especially if feature logic 

'''