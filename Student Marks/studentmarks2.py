# Student Name:   KYLA SOFOCADO
# Student Number: 1034672

class Student:
   """Properties of the class incude:
    name = string
    marks = a list of integers
    """
   def __init__(self, name, marks): #Creates instance for each student
      self.name = name
      self.marks = marks

   def student_transcripts(self):  
       print(f"Student Name: {self.name}")
       print(f"Marks: {self.marks}")

#Student Instances section
student1 = Student("Alice", [85, 90, 78, 92]) 
student2 = Student("Bob", [75, 80, 85, 79])
student3 = Student("Charlie", [88, 92, 94, 89])
student4 = Student("David", [70, 65, 80, 74])
student5 = Student("Emma", [95, 98, 97, 96])
student6 = Student("Frank", [60, 55, 70, 65])
student7 = Student("Grace", [82, 87, 85, 90])
student8 = Student("Hannah", [90, 88, 84, 91])
student9 = Student("Ian", [78, 80, 76, 79])
student10 = Student("Jack", [85, 82, 88, 86])

#Functions section
def choose_student(): #Allows user to choose a student instance
    while True:
        try:
         choice = int(input("Choose a student from 1-10: "))
         for choice in range(1, 10 - 1):
             if choice == 1: 
                 




def add_mark(): #Takes a single value and adds it to the list of marks
      new_mark = int(input("Enter a new mark:"))
      student


#User Menu section
def main():
      print("Choose a student from the list below:")
      while True:
         try:
            if choice == 1:
               print("1. Alice")
            elif choice == 2:
               print("2. Bob")
            elif choice == 3:
               print("3. Charlie")
            elif choice == 4:
               print("4. David")
            elif choice == 5:
               print("5. Emma")
            elif choice == 6:
               print("6. Frank")
            elif choice == 7:
               print("7. Grace")
            elif choice == 8:
               print("8. Hannah")
            elif choice == 9:
               print("9. Ian")
            elif choice == 10:
               print("10. Jack")
            else:
               print("Invalid choice. Please try again.")
         except ValueError:
            print("Please input a number from 1-10. Not letters or symbols.")
      


# Debugging statements
student1.student_transcripts() #Shows that it prints out the student's name and marks






