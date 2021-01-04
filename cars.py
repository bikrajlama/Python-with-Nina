class Car:
    runs = True
    number_of_wheels = 4


    def __init__(self, name):
        print("New Car!")
        self.name = name


    def start(self):
        if self.runs:
            print(f"{self.name} Car is started.")
        else:
            print(f"{self.name} Car is broken.")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels