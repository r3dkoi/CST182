#Functions for student marks

def add_mark():
    while True:
        try:
            with open("student_marks.txt", "a") as f: #Allows function to open file and then close it immediately when finished
                mark = int(input("Please input a mark you wish to add to the student."))
                if mark < 0:
                    print("Please input a mark that is non-negative.")
        except ValueError:
            print("Please input only numbers, not letters or any other characters.")
                