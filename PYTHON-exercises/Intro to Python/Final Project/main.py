#=============================#
# Main
# Konstantin Masich
#=============================#
import csv
import fileworks
import student
import course

GRADES_FILE    = "grades.csv"   # Default location of Grades file
SETTINGS_FILE  = "settings.csv" # Default location of Settings file
OUTFILE        = "output"       # Default location of Output file
TESTFILE       = "gradeys.csv"  # Testfile

# Choice constants (C is for Choice)
C_SHOW_ALL_GRADES = "1"
C_UPDATE_GRADES   = "2"
C_PRINT_DATA      = "3"
C_PROJECT         = "p"
C_PTOR            = "f"
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
    print("    3. Print course data")
    print("    Enter 'q' to Quit.\n")        

      
# 0. Loading Students' Grades and Settings from file
stud_dict = fileworks.read_csv(GRADES_FILE, "Grades") # grades dictionary
settings  = fileworks.read_csv(SETTINGS_FILE, "Settings")
# if Grades and/or Settings do not exist, exit the program
if stud_dict==None or settings==None:
    exit()
   
# 1a Creating Students dictionary and service variables
for k, v in stud_dict.items():
    name    = v[0]
    grades  = [int(x) for x in v[1:-1]]
    project = int(v[-1])
    stud_dict[k] = student.Student(name, grades, project)
COURSE_NAME   = settings[0]   
MANDATORY_NUM = int(settings[1])
WEIGHTS = list(map(float, settings[2:]))


# 1b. Creating a Course object
course = course.Course(COURSE_NAME, stud_dict, MANDATORY_NUM, WEIGHTS)
#course = course.Course(settings[0], gd, settings[1], settings[2:])


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
        newgrade = input("Enter updated project grade:")
        if is_non_negative_number(newgrade):
            newgrade = int(newgrade)
            if newgrade <= MAX_GRADE:
                course.set_student_project(stud_id, newgrade)
                print("Project grade updated.")
                commit_changes()
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
        print("(grades: enter '", C_PTOR,"' for ptor, 0 for homework that was not submitted)")
        newgrade = input("")
        # Ptor case:
        if newgrade == C_PTOR:
            course.set_student_ex(stud_id, choice, -1)
            print("Ptor granted.")
            commit_changes()
            return
        # Non-ptor case:    
        if is_non_negative_number(newgrade):
            newgrade = int(newgrade)
            if newgrade <= MAX_GRADE:
                course.set_student_ex(stud_id, choice, newgrade)
                print("Exercise grade updated.")
                commit_changes()
                return
            else:
                print("Error: illegal grade!")
                return
        else:
            print("Illegal input!")
        
            
def commit_changes():
    """ Commits changes into GRADES and OUTPUT files. """
    # Commiting changes into GRADES file
    if fileworks.write_to_file(GRADES_FILE, course.get_grades_data()) == False:
        print("Error: failed to commit changes!")
        return
    # Commiting changes into OUTPUT file
    if fileworks.write_to_file(OUTFILE, course.get_course_data()) == False:
        print("Error: failed to commit changes!")
    

# 1. Displaying menu and getting user's choice
choice = ""
while choice != C_QUIT:
    show_menu()
    choice = input("")
    #================== SHOW ALL GRADES =====================#
    if choice   == C_SHOW_ALL_GRADES:
       course.print_all_grades()
    #============== UPDATE STUDENT'S GRADES =================#    
    elif choice == C_UPDATE_GRADES:
        update_grades()
    #============== PRINT COURSE DATA =======================#    
    elif choice == C_PRINT_DATA:
        course.print_course_data()
