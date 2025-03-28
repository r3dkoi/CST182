#Functions for student marks

def student_name():
    while True:
        name = input("Which student's record would you like to access?").lower() 
        try:
            with open("student_marks.txt", "r") as f:
                names = f.read().splitlines() #Opens and reads content of the file, must be executed before it does the following:
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
                new_mark = int(input("Please input a mark you wish to add to the student."))
                r_and_a_file()
                if new_mark < 0:
                    print("Please input a mark that is non-negative.")
        except ValueError:
            print("Please input only numbers, not letters or any other characters.")
    

def r_and_a_file(): #Function for reading the file and appending new marks
    lines = f.readlines() #Tells program to read the content in student.txt
    for i, line in enumerate(lines):
                if line.startswith(name): #Find's the specific student
                        parts = line.split() #Splits into the name and marks
                        name = parts[0] #Extracts the student name
                        marks = parts[1] #Extracts the student's marks
                        marks.append(str(new_mark)) #Adds the new mark into the current mark list
                        lines[i] = " ".join([name] + marks) + "\n" #Reformats the line
                f.seek(0) #Moves to start of the file
                f.writelines(lines) #Writes updated content into the original file to be saved
                f.truncate() #Ensures no leftover content from previous data

def calculate_GPA():
     