import random

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

def create_automatic_rooms(students2, all_rooms):

    number_of_students = len(students2) # how many students do we have
    total_rooms = len(all_rooms) # how many rooms do we have available
    current_room = 0 # what breakout room idex are we currently adding to

    while(number_of_students > 0):
      # this check will make sure we continue looping through every single breakout room multiple times
      if current_room > total_rooms-1: 
        current_room = 0

      random_student = random.choice(students2)
      add_to_room(random_student, all_rooms[current_room])
      remove_from_list(random_student, students2)

      number_of_students -= 1
      current_room += 1

      # How can we clean this code up EVEN MORE?? 
    # HINT: use % to update current_room instead of using if statement (I know right, pretty crazy!!)
    
    return all_rooms

def display_room_info(all_rooms):

  for room in all_rooms:
    print(room)


def main():
  br_1 = []
  br_2 = []
  br_3 = []
  br_4 = []
  all_rooms = [br_1, br_2, br_3, br_4] # list of every single room 

  # volunteers2 = ["Hunter", "William", "Le", "Miguel"]
  students2 = ["DeJohn", "Jessica", "Dexian", "Lexian", "Rafa", "Eunbi", "Yixi", "Griffin", "Cindy", "Sabeen", "Christine", "Agnes"]
  random.shuffle(students2) # this function will shuffle the order of volunteers (not really necc. if we're using random.choice)
  create_automatic_rooms(students2, all_rooms)
  display_room_info(all_rooms)


main()








'''
Questions: 
How do we improve this EVEN MORE??
What if we want to add a room ? The way we did it in the last example was KIND OF awkward and not efficient 

'''