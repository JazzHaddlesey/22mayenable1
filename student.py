'''
In a new Python file, create a class of students.

It should contain the following attributes: 
name, age, and class with default value "student".

It should also contain a method which takes in 3 test scores 
and prints the students average test score.
'''

# class Student:

#     def __init__(self, name = "student", age = "student", class_ = "student", test1 = 0, test2 = 0, test3 = 0):
#         self.name = name
#         self.age = age
#         self.class_ = class_
#         self.test1 = test1
#         self.test2 = test2
#         self.test3 = test3 

    
# avg = test1 + test2 + test3 / 3     
# average = Average(avg)

    
# John = Student("John", "21", "22", "84", "99")
# Jane = Student("Jane", "22", "34", "99", "78")

# print(getattr(John))
# print(average)


class Students():
    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
        
    def gradeCalc(self, t1, t2, t3):
        result = (t1 + t2 + t3) / 3
        return result
        
stud1 = Students("Jonh", 34, "Software")
t1 = 50
t2 = 50
t3 = 50

print(stud1.gradeCalc(t1, t2, t3))

