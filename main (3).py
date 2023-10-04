class student:
     def __init__(self,name, roll_number,cgpa):
         self.name = name
         self.roll_number = roll_number
         self.cgpa = cgpa

     def sort_students(student_list):
         sorted_students = sorted(student_list,key=lambda 
       student: student.cgpa, reverse=True)
  
       return sorted_students

students = [ student("hari","A123", 7.8),
             student("abi","A124",2.2)]
sorted_students  = sort_students(students)
for student in sorted_students:
  print("name: {}, Rollnumber:{}, cgpa:{}".format(student.name, student.roll_number,student.cgpa))

