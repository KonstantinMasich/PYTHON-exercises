class Student(object):
    """
    Student class.
    """
    
    def __init__(self, name, grades, project):
        self.name    = name    # Student's name
        self.grades  = grades  # List of Student's grades
        self.project = project # Student's project mark
        self.ptors   = 0       # Amount of studen'ts ptors
        for g in grades:
            if g == -1:
                self.ptors += 1
    
    def grades_mean(self, weights, mandatory_num):
        "Calculates academical mean of exercise grades (project not included)"
        # 0. Recalculating amount of mandatory exercises:
        mandatory_num = mandatory_num - self.ptors
        if mandatory_num <= 0:
            return -1 # -1 means that grades mean is redundand as this student
                      # was freed from obligation of submitting exercises
                      
        # 1. Removing ptors from grades and their corresponding weights:
        gd = []
        submitted = 0
        for g, w in zip(self.grades, weights):
            if g != -1:
                gd.append([g, w])
            if g != 0:
                submitted += 1   

        # 2. Checking if amount of submitted exercises is not less than
        # amout of mandatory exercises:
        #submitted = [x > 0 for x in ]
        if submitted < mandatory_num:
            return 0 # 0 means exercises grade is zero
            
        # 3. Sorting: getting <mandatory_num> best exercises
        gd = sorted(gd, reverse=True)[:mandatory_num]
        # print(gd)
        
        # 4. Calculating academic mean of exercises:
        g = lambda x: x[0] * x[1]
        res = sum([g(x) for x in gd]) / sum([x[1] for x in gd])
        return round(res,2)
        
        
    def total_mean(self, weights, mandatory_num):
        # if grades mean is -1, project grade is the course grade..
        exc = self.grades_mean(weights[:-1], mandatory_num)
       # print(exc)
        if exc == -1:
            return self.project
        elif exc == 0:
            res = self.project * weights[-1]
            return round(res,2)
        else:
            res = exc*(1 - weights[-1]) + self.project*weights[-1]
            return round(res,2)
     
    def update_ptors(self):
        """ Updates amount of student's ptors """
        self.ptors = 0
        for g in self.grades:
            if g == -1:
                self.ptors += 1           
    
#==============================================================================#
#======================== GETTERS and SETTERS =================================#
#==============================================================================#    
    def get_name(self):
        return self.name        
    def get_grades(self):
        return self.grades
    def get_project(self):
        return self.project
    def set_project(self, grade):
        self.project = grade
    def set_exercise_grade(self, ex_no, newgrade):
        self.grades[ex_no] = newgrade
