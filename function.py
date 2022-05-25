'''
Create a new python file. 
In that file create a program that works out a grade based on marks with the use of functions.

The program should take the students name, 
homework score (/25), assessment score (/50) and final exam score (/100) as inputs, 
and output their name and final ICT grade as a percentage.

Reminder: any inputs and prints should not be included inside the function definition, 
and should strictly be done outside.

Stretch goal: Include grade boundaries such that 
the program also outputs a grade for the student (A, B, etc.)
'''



def score(homework, assessment, exam):
  final_grade = (homework + assessment + exam) / 175 * 100
  return final_grade

name = input("Your name: ")
    
homework = int(input("Homework score 0/25: "))
while homework < 0 or homework > 25:
  print("Your homework score must be between 0 and 25")
  homework = int(input("Homework score 0/25: "))
  

assessment = int(input("Assessment score 0/50: "))
while assessment < 0 or assessment > 50:
  print("Your assessment score must between 0 and 50")
  assessment = int(input("Assessment score 0/50: "))
  

exam = int(input("Final exam score 0/100: "))
while exam < 0 or exam > 100:
  print("Your exam score must between 0 and 100")
  exam = int(input("Final exam score 0/100: "))
  


print(f"{name}: {int(score(homework, assessment, exam))}%")





