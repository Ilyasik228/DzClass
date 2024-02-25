class Student:

    def __init__(self):
        self.Name = "Ilyas"
        self.Age = 14
        self.Class = "9D"
        self.School = 276
        self.BirthYear = 2009
        self.Height = 200


    def AboutMe(self):
        print("My name is " + self.Name)
        print("My age is " + self.Age.__str__())
        print("My class is " + self.Class.__str__())
        print("My school is " + self.School.__str__())
        print("My birth year is " + self.BirthYear.__str__())
        print("My height is " + self.Height.__str__())

abc = Student()

abc.AboutMe()