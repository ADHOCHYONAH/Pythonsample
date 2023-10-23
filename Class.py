class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def wanafunzi(self):
            print("Name: %s \nCourse: %s \nGender: %s \nAge: %d "
                  %(self.name,self.course,self.gender,self.age))

    #method
stud1=students("Adhoch Yonah","IT","Male",25)
stud2=students("Modester Atieno","comp Science","female",18)
stud3=students("Faith Achalo","Biochem","Female",19)
stud4=students("Brian Weke","Commerce","Male",35)
stud5=students("Eunice Benard","IT","female",32)


stud1.wanafunzi()
stud2.wanafunzi()
stud3.wanafunzi()
stud4.wanafunzi()
stud5.wanafunzi()