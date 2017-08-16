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
        self.weights  = weights       # Weights for excercises and project
        """
        temp = []                     # Weights for excercises and project
        for w in weights:
            temp.append(float(w))
        self.weights = temp
        """
        
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
   
            
    def get_course_data(self):
        """
        Returns string with course data: course name, amount of students and homeworks,
        weights, and each student's means.     
        """
        s =  "Course name: " + self.name + "\n"
        s += "Amount of students: " + str(self.stud_no) + "\n"
        s += "Amount of mandatory excercises: " + str(self.mand_no) + "\n"
        s += "\nWeights:\n"
        index = 1
        for w in self.weights:
            s += "Ex" + str(index) + " : weight = " + str(w) + "\n"
            index += 1
        s += "\n\nSTUDENTS DATA:\n\n"
        s += "====================================\n"
        for ID, student in self.students.items():
            s += student.get_name() + " (" + ID + ")\n"
            s += "    Exercises mean is: " + str(student.grades_mean(self.weights, self.mand_no)) + "\n"
            s += "    Project grade  is: " + str(student.get_project()) + "\n"
            s += "    Total mean     is: " + str(student.total_mean(self.weights, self.mand_no)) + "\n"
            s += "====================================\n"
        return s
        
    def print_course_data(self):
        """ Prints course data on the screen """
        print(self.get_course_data())
        
    def get_grades_data(self):
        """ Returns data about students grades """
        s = ""
        for ID, student in self.students.items():
            s += str(ID) + "," + student.get_name() + ","
            s += ",".join(str(e) for e in student.get_grades()) + ","
            s += str(student.get_project()) + "\n"
        return s
        
    def print_grades_data(self):
        """ Prints grades data on the screen """
        print(self.get_grades_data())    

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
