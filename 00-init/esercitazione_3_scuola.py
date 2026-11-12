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

