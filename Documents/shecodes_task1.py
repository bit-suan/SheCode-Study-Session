class Student:
   def __init__(self,name,age,grade):
      self.name=name
      self.age=age
      self.grade=grade
   def Display(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentSystem:
   def __init__(self):
      self.students=[]
   def addStudents(self):
    n=int(input("how many students you want to add: "))
    for i in range(n):
      name=input("what is the student name:")
      age=int(input("age: "))
      grade=float(input("Grade: "))
      student_obj = Student(name, age, grade)
      self.students.append(student_obj)
    return " the student added sucessfully. "
   def Display(self):
    if self.students:
        print("\nList of Students:")
        for stud in self.students:
         print(stud.Display())
    else:
      print("\n No students to display.")
   def deleteStudent(self):
      remove= input("\n Enter the name of the student you want to delete: ")
      for student in self.students:
       if student.name==remove:
         self.students.remove(student)
         return f"Student '{remove}' deleted successfully."
      return f"Student '{remove}' not found."
   def displayfiltered(self):
    condition = input("Enter the condition (e.g., '>', '<', '>=', '=', '<='): ")
    val = float(input("Enter the Grade condition value: "))
    if condition == ">":
            filtered = [student for student in self.students if student.grade > val]
    elif condition == "<":
            filtered = [student for student in self.students if student.grade < val]
    elif condition == ">=":
            filtered = [student for student in self.students if student.grade >= val]
    elif condition == "<=":
            filtered = [student for student in self.students if student.grade <= val]
    elif condition == "=":
            filtered = [student for student in self.students if student.grade == val]
    else:
            print("Invalid condition. Please try again.")
            return
    if filtered:
            print(f"\nFiltered Students with grade {condition} {val}:")
            for student in filtered:
                print(student.Display())
    else:
            print(f"No students found with grade {condition} {val}.")
def main():
    system = StudentSystem() 
    while True:
       print("\n Wellcome to Student Information system.")
       print(" 1.Add a student.\n 2.View all students.\n 3.Delete a student.\n 4.To get filtered list \n 5.Exit the program.")
       choice=int(input("Enter your choice: "))
       if choice==1:
         print(system.addStudents())
       elif choice==2:
         system.Display()
       elif choice==3:
         print(system.deleteStudent())
       elif choice==4:
         system.displayfiltered()
       elif choice==5:
         print("Exiting the program.")
         break
       else:
         print("Invalid choice, please try again.")
main()
   
