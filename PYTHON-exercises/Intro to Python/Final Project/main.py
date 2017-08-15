#=============================#
# Main
# Konstantin Masich
#=============================#
import csv
import fileworks
import student
import course

GRADES_FILE_PATH   = "grades.csv"   # Default location of Grades file
SETTINGS_FILE_PATH = "settings.csv" # Default location of Settings file

# Choice constants (C is for Choice)
C_SHOW_ALL_GRADES = "1"
C_UPDATE_GRADES   = "2"
C_PROJECT         = "p"
C_QUIT            = "q"
INT_QUIT          = -999
INT_PROJECT       = -998
MAX_GRADE         = 100


def is_number(num):
    """Returns True if Object is a number, False otherwise"""
    try:
        num = int(num)
        return True
    except ValueError:
        return False
        
        
def is_non_negative_number(num):
    """Returns True if Object is a non-negative number, False otherwise"""
    try:
        num = int(num)
        if num < 0:
            return False
        return True
    except ValueError:
        return False
        
        
def show_menu():
    "Simply shows Main Menu."
    print("\n               Menu:")
    print("    1. Print all students' grades")
    print("    2. Update student's grades or ptors")
    print("    3. Res")
    print("    Enter 'q' to Quit.\n")        

      
# 0. Loading Students' Grades and Settings from file
gd = fileworks.read_csv(GRADES_FILE_PATH, "Grades") # grades dictionary
settings = fileworks.read_csv(SETTINGS_FILE_PATH, "Settings")
# if Grades and/or Settings do not exist, exit the program
if gd==None or settings==None:
    exit()
   
# 1a Creating Students dictionary and service variables
for k, v in gd.items():
    name    = v[0]
    grades  = [int(x) for x in v[1:-1]]
    project = int(v[-1])
    gd[k] = student.Student(name, grades, project)
COURSE_NAME   = settings[0]   
MANDATORY_NUM = int(settings[1])
WEIGHTS = list(map(float, settings[2:]))


# 1b. Creating a Course object
course = course.Course(settings[0], gd, settings[1], settings[2:])


# TESTED
def print_students_list(stud_dict):
    """Returns+prints list of students in the form of: index - ID- name"""
    dictlist = []
    index    = 0
    for ID, student in stud_dict.items():
        print(index, ID, student.get_name()) 
        temp = [index, ID, student.get_name()]
        dictlist.append(temp)
        index += 1
    return dictlist
    

# TESTED
def get_numeric_choice(low, hi):
    """
    Gets a numeric input from user. Input must be within [low..hi] interval
    and must be numeric as well, or it can be C_QUIT. Return values:
    number - if an entered number is a valid integer in [low..hi] interval
    -1     - if input is invalid or input is not a number
    INT_QUIT    - if input is C_QUIT
    INT_PROJECT - if input is C_PROJECT
    """
    choice = input("")
    if choice == C_QUIT:
        return INT_QUIT
    elif choice == C_PROJECT:
        return INT_PROJECT   
    else:
        if is_number(choice):
            choice = int(choice) # Cast to integer
            if choice < low or choice > hi:
                print("Error: illegal choice!")
                return -1
            else:
                return choice
        else:
            print("Error: illegal choice!")
            return -1


def update_grades():
    """
    Updates grades and ptors of a selected student.
    """
    # 1. Selecting a student:
    print("\nWhich student's grades do you wish to update?")
    dictlist = print_students_list(course.get_students());
    print("\nOr enter '",C_QUIT,"' to Quit")
    choice = get_numeric_choice(0, len(dictlist)-1)
    if choice < 0:
        return
    stud_data = [x for x in dictlist if x[0]==choice]
    stud_id   = stud_data[0][1]
    stud_name = stud_data[0][2] 
    # 2. Selecting an grade to alter:
    print("\nWorking with student", stud_name, "(", stud_id, "):")
    print("Which grade do you want to alter?\n")
    grades = course.get_student_grades(stud_id);
    index = 0
    for el in grades:
        print(index, ": Ex", index+1, "Grade = ", el)
        index += 1
    print("Final project grade: ", course.get_student_project(stud_id))
    print("To alter the final project grade, enter '", C_PROJECT, "'")
    choice = get_numeric_choice(0, len(grades)-1)
    if choice == INT_QUIT:
        # Quit option activated
        return    
    elif choice == INT_PROJECT:
        # Changing PROJECT GRADE:
        newgrade = input("Enter updated project grade: ")
        if is_non_negative_number(newgrade):
            newgrade = int(newgrade)
            if newgrade <= MAX_GRADE:
                course.set_student_project(stud_id, newgrade)
                print("Project grade updated.")
                return
            else:
                print("Error: illegal grade!")
                return
        else:
            print("Illegal input!")
       
    else:
        # Illegal choice:
        if choice < 0:
            print("Error: illegal excerice number!")
            return
        # Changing EXERCISE GRADE:
        print("\nEnter updated grade for Ex", choice+1, ": ")
        print("(grades: -1 for ptor, 0 for homework that was not submitted)")
        newgrade = input("")
        if is_non_negative_number(newgrade):
            newgrade = int(newgrade)
            if newgrade <= MAX_GRADE:
                course.set_student_ex(stud_id, choice, newgrade)
                print("Exercise grade updated.")
                return
            else:
                print("Error: illegal grade!")
                return
        else:
            print("Illegal input!")
        
            
        
    
    

# 1. Displaying menu and getting user's choice
choice = ""

choice = C_QUIT
course.print_course_data()

while choice != C_QUIT:
    show_menu()
    choice = input("")
    #================== SHOW ALL GRADES =====================#
    if choice   == C_SHOW_ALL_GRADES:
       course.print_all_grades()
    #============== UPDATE STUDENT'S GRADES =================#    
    elif choice == C_UPDATE_GRADES:
        update_grades()
    elif choice == "3":
        pass
