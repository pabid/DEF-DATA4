

#create a class of students.

#should contain the following attributes: name, age, and class with 
# default value "student".

#should also contain a method which takes in 3 test scores and 
# prints the students average test sc


class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_score(self, s1, s2, s3):
        self.s1 =s1
        self.s2 =s2
        self.s3 =s3

        ave = (s1 + s2 + s3)/3
        return (ave)



student1 = Student("A","20")
name1= getattr(student1, "name")
age1= getattr(student1, "age")
averagescore =student1.get_student_score(10,20,30)

print(f"{name1}, aged {age1}, average score is {averagescore}")
 

