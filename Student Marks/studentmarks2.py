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

   #Methods section
   def add_mark(self): #Takes a single value and adds it to the list of marks
         new_mark = int(input("Enter a new mark:"))
         self.marks.append(new_mark) #appends to the list of marks in the student instance
         print(f"New mark added: to {self.name}'s list of marks: {self.marks}")
   
   def calculate_GPA(self): #Calculates the GPA of the student
      total = sum(self.marks)
      average = total/len(self.marks)
      print(f"{self.name}'s GPA is: {average}")

   def student_transcripts(self): #Prints out the student name and their new list of marks
      print(f"Student Name: {self.name}")
      print(f"Marks: {self.marks}")
      print(f"GPA: {sum(self.marks)/len(self.marks)}")

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

#User Menu section
def main():
      students = [student1, student2, student3, student4, student5, 
                  student6, student7, student8, student9, student10] #List of the students in Student Class
      
      print("The students currently under your class: ")
      for i, student in enumerate(students, start = 1):
           print(f"{i}. {student.name}") #Creates a descending numbered list of the students from the Students instances section. Begins at index 1.

      while True:
               try:
                    choice = int(input("Enter the corresponding number from the list above to access their records: "))
                    if 1 <= choice <= len(students): #Checks if choice is within the length of the list of students
                        """Each student has a list of marks and the user can choose to add a mark, calculate their GPA or print their transcript"""
                        selected_student = students[choice - 1] #Subtracts 1 from the choice to get the index of the student in the list
                        print("1. Add a mark")
                        print("2. Calculate their GPA")
                        print("3. Print their transcript")
                        print("4. Exit the entire program")

                        option = int(input("Enter the corresponding number to choose an option: "))
                        if option == 1:
                              selected_student.add_mark()
                        elif option == 2:
                              selected_student.calculate_GPA()
                        elif option == 3:
                              selected_student.student_transcripts()
                        elif option == 4:
                              break
                        else:
                              print("Invalid option. Please try again.")
               except ValueError:
                  print("Please only input numbers, not letters or symbols.")
               


# Debugging statements
student1.student_transcripts() #Shows that it prints out the student's name and marks
main()





