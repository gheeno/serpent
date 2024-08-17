class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def printFirstName(self):
        print(f"First name of the player is {self.name}")

    def printLastName(self):
        print(f"Last name of the player is {self.lastName}")

    def bmi(self, weight: float) -> str:
        return f"weight : {weight * 0.88}"

# Create an instance of Person
person1 = Person("Gheeno", "San Pascual")

# Print first and last names
person1.printFirstName()
person1.printLastName()

# Calculate and print BMI
weight = 70  # Example weight in kg
bmi_result = person1.bmi(weight)
print(f"The BMI of {person1.name} {person1.lastName} is {bmi_result}")
