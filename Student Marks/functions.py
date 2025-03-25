#Functions for student marks

def student_name():
    while True:
        name = input("Which student's record would you like to access?").lower() 
        try:
            with open("student_marks.txt", "r") as f:
                names = file.read().splitlines() #Opens and reads content of the file, must be executed before it does the following:
                if name in names:
                    print("Please choose the following options:")
                    #Add functions of everything down here
                else:
                    print("Name is not found in the file.")
        except FileNotFoundError:
             print("File does not exist, please check file path.")

             

def add_mark(name, mark):
    while True:
        try:
            with open("student_marks.txt", "a") as f: #Allows function to open file and then close it immediately when finished
                mark = int(input("Please input a mark you wish to add to the student."))
                lines = f.readlines() #Tells program to read the content in student.txt
                for i, line in enumerate(lines):
                    if line.startswith(name): #Find's the specific student
                if mark < 0:
                    print("Please input a mark that is non-negative.")
        except ValueError:
            print("Please input only numbers, not letters or any other characters.")
        