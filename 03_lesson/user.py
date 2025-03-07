class User:
    first_name = "No first_name"
    last_name = "No last_name"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_name(self):
        return f"Моё имя: {self.first_name}"

    def say_last_name(self):
        print(f"Моя фамилия: {self.last_name}")

    def say_full_name(self):
        print(f"Моё имя и фамилия: {self.first_name} {self.last_name}")