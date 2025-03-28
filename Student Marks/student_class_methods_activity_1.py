# Student Name: Kyla Sofocado
# Student Number: 1034672

import datetime 

# TODO: Insert class definition:
class Student:
  """Properties include:
  name = string
  age = int
  subject major = string"""
  def __init__(self, name, age, subject_major): #Creates an instance specifically for each student 
    self.name = name
    self.age = age
    self.subject_major = subject_major

  def student_transcript(self):  #Prints out the name, age, and subject major in a neat format
    students = [s1, s2, s3]
    student = Student #Stores the variable of the class Student 

    for i in len(students):
      print(f"Student Name: {student.name}, \nAge: {student.age}, \nSubject Major: {student.subject_major}")



        

# Object Creation
    """S1, S2, S3 represent different students"""
s1 = Student("Greg", 21, "Computer Science")
s2 = Student("Lucy", 34, "Engineering")
s3 = Student("Chris", 19, "Arts")

