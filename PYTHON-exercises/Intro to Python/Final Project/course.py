#=============================#
# Course
# Konstantin Masich
#=============================#
import student

class Course(object):
    """
    Course class.
    """
    
    def __init__(self, name, students, mandatory, weights):
        self.name     = name          # Course name
        self.students = students      # Students dictionary
        self.stud_no  = len(students) # Amount of Students enlisted to course
        self.mand_no  = int(mandatory)# Amount of mandatory excercises
        temp = []                     # Weights for excercises and project] 
        for w in weights:
            temp.append(float(w))
        self.weights = temp    
     
    
    
    
    
    
    
        
    def print_all_grades(self):
        """
        Prints students' grades from Grades dictionary (in RAM
        during runtime; not from file)
        """
        print("================================\nSTUDENTS GRADES TABLE:")
        print("================================")
        for k, v in self.students.items():
           print(k, v.get_name(), ":", v.get_grades(), "Project:", v.get_project())
        print("================================")
    
    
    def print_course_data(self):
        print("Course name:", self.name)
        print("Amount of students:", self.stud_no)
        print("Amount of mandatory excercises:", self.mand_no)
        print("\nWeights:")
        index = 1
        for w in self.weights:
            print("Ex", index, ": weight =", w)
            index += 1
        print("\n\nStudents data:\n")
        print("==============================================")
        for ID, student in self.students.items():
            print(student.get_name(), "(", ID, "):")
            print("Exercises mean is: ", student.grades_mean(self.weights, self.mand_no))
            print("Project grade  is: ", student.get_project())
            print("Total mean     is: ", student.total_mean(self.weights, self.mand_no))
            print("==============================================")
            
            
#==============================================================================#
#======================== GETTERS and SETTERS =================================#
#==============================================================================#
    def get_students(self):
        return self.students
    
    def get_student_grades(self, stud_id):
        return self.students.get(stud_id).get_grades()
        
    def get_student_project(self, stud_id):
        return self.students.get(stud_id).get_project()
        
    def set_student_project(self, stud_id, grade):
        self.students.get(stud_id).set_project(grade)
        
    def set_student_ex(self, stud_id, ex_no, newgrade):
        """ Changes student's exercise grade """
        self.students.get(stud_id).set_exercise_grade(ex_no, newgrade)
        self.students.get(stud_id).update_ptors()
