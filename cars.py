class Car:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} Car is started.")
        else:
            print(f"{self.name} Car is broken.")