class Student:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def classification(self):
        if 14 <= self.age <= 16:
            return "Biennium"
        if 17 <= self.age <= 19:
            return "Triennium"
        return "Other"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, living in {self.city}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def search_by_last_name(self, last_name):
        last_name = last_name.lower()
        return [student for student in self.students if student.last_name.lower() == last_name]

    def search_by_age(self, age):
        return [student for student in self.students if student.age == age]

    def count_students(self):
        return len(self.students)

    def __len__(self):
        return self.count_students()


class Classroom:
    def __init__(self, section, year):
        self.section = section
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_list(self):
        return self.students


if __name__ == "__main__":
    high_school = School("Greenwood Academy")

    high_school.add_student(Student("Osto", "Talpa", 15, "Africa"))
    high_school.add_student(Student("Mattia", "Fasc", 17, "Casablanca"))
    high_school.add_student(Student("Tuma", "Puma", 19, "Cesena"))
    high_school.add_student(Student("Cesa", "dingdong", 17, "Cesenatico"))

    print(f"Total students in school: {high_school.count_students()}")

    for student in high_school.search_by_last_name("smith"):
        print(student)
        print(f"Level: {student.classification()}")

    print("Students aged 17:")
    for student in high_school.search_by_age(17):
        print(f"- {student.first_name} {student.last_name}")

    senior_class = Classroom("6B", 2026)
    senior_class.add_student(high_school.students[1])
    senior_class.add_student(high_school.students[3])
    print(f"Classroom {senior_class.section}: {len(senior_class.get_list())} students")