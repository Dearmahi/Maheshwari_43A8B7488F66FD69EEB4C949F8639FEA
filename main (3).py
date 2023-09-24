class Student:
  
def__init__(self,name,roll_number,cgpa):
self.name=name
self.roll_number=roll_number
self.cgpa=cgpa
def Sort_Students(Student_list):
  Sorted_Students=Sorted(Student_list,key=lambda Student:Student.cgpa, reverse=true)
  return Sorted_Students
  Students=[Student("raji","A123",5.5),Student("nisha","A124",6.6),Student("Priyanka","A125",7.7),Student("subha","A126",8.8)]
  Sorted_Students=Sort_Students(Students)
  for Student in Sorted_Students:
print("name:{},Roll:{},CGPA:{}". format (Student.name, Student.roll_number, Student.cgpa)
      