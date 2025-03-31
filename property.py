class Student:
    def __init__(self, physics, chemistry, maths):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        #self.percentage = Just added percentage sign

        #When attribute value is dependent on percentage then make the function a property

    @property
    def percentage(self):
        return str((self.physics + self.chemistry + self.maths) / 3) + "%" 

stu1 = Student(98, 99, 95)
print(stu1.percentage)

stu1.physics = 86
print(stu1.percentage)