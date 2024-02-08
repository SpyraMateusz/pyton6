class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Jestem {self.name} i mam {self.age} lat."

# Tworzenie instancji klasy Person
osoba = Person("Jan", 30)

# Wywołanie metody introduce()
print(osoba.introduce())