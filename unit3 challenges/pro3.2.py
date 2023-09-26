class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
  

def sort_students(student_list):

    sorted_students = sorted(student_list,
                            key=lambda student: student. cgpa,
                            reverse=True)
    
    return sorted_students
    
     
    
    


students = [
      Student("Thirisha", "ST12", 8.7),
      Student("Farsana", "ST13", 8.5),
      Student("Abirami", "ST14", 8.7),
      Student("Parameshwari", "ST15", 8.3),
      Student("Priysdharshini", "ST16", 8.5)
]

sorted_students = sort_students(students)


for student in sorted_students:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
student.roll_number,                                            
                                                      student.cgpa))