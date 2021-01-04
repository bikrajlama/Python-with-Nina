class Car:
    runs = True



    def __init__(self, name):
        print("New Car!")
        self.name = name


    def start(self):
        if self.runs:
            print(f"{self.name} Car is started.")
        else:
            print(f"{self.name} Car is broken.")