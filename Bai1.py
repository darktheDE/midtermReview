class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    @property
    def yob(self):
        return self._yob
    @yob.setter
    def yob(self,value):
        if value > 0:
            self._yob = value
        else:
            print("yob < 0")
    def describe(self):
        print("Name: ", self.name)
        print("Year of birth: ", self.yob)
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self,value):
        self._subject = value
    def describe(self):
        super().describe()
        print("Subject: ", self._subject)
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist
    @property
    def specialist(self):
        return self._specialist
    @specialist.setter
    def specialist(self,value):
        self._specialist = value
    def describe(self):
        super().describe()
        print("Specialist: ", self._specialist)     
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,value):
        self._grade = value
    def describe(self):
        super().describe()
        print("Subject: ", self._grade)
class Ward:
    wardList = []
    def __init__(self, name):
        self._name = name
        self._wardList = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    def addPerson(self, person):
        self._wardList.append(person)
    def describe(self):
        print("Name of Ward: ", self.name)
        for person in self._wardList:
            person.describe()
    def countDoctor(self):
        count = 0
        for person in self._wardList:
            if type(person) == Doctor:
                count += 1
        return count

    def sortAge(self):
        self._wardList.sort(key= lambda person: person.yob, reverse=True)
    def avgTeacherYOB(self):
        totalYOB = 0
        countTeacher = 0
        for person in self._wardList:
            if type(person) == Teacher:
                totalYOB += person.yob
                countTeacher +=1
        return totalYOB/countTeacher
def main():
    ward = Ward("LinhXuan")
    
    ps1 = Student("Hung", 2005, 12)
    ps2 = Teacher("Hien", 1980, "Math")
    ps3 = Teacher("Lan", 1975, "Physics")
    ps4 = Doctor("Quan", 1990, "Cardiology")
    ps5 = Doctor("An", 1985, "Neurology")
    
    ward.addPerson(ps1)
    ward.addPerson(ps2)
    ward.addPerson(ps3)
    ward.addPerson(ps4)
    ward.addPerson(ps5)
    
    ward.describe()
    ward.sortAge()
    ward.describe()
    print("Number of Doctor: ", ward.countDoctor())
    print("Avg year of birth of teacher: ", int(ward.avgTeacherYOB()))
    
main()