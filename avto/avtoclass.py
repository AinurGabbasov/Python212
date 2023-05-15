class AvtoClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def show_avto(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.probeg} км")


# для того чтоб эти выводы е(экз класса) были только здесь
# и не отрабатывали в других файлах
if __name__ == "__main__":
    e = AvtoClass("Tesla", "T", 2018, 99000)
    e.show_avto()
