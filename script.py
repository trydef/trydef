class Cat:
    def __init__(self, name, age, color , breed , owner, gender):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.owner = owner
        self.gender = gender

    def ToString(self):
        return (
            f"Cat: \n"
            f"\tName: {self.name};\n"
            f"\tAge: {self.age};\n"
            f"\tColor: {self.color};\n"
            f"\tBreed {self.breed};\n"
            f"\tOwner: {self.owner};\n"
            f"\tGender: {self.gender};\n"
        )