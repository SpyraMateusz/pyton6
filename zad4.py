class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Przykładowe użycie
moje_kolo = Circle(5)
print("Promień koła:", moje_kolo.radius)
print("Pole koła:", moje_kolo.area())