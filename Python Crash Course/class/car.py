class Car: 
    """ A simple class that defines a car."""

    def __init__(self, make: str, model: str, year:int):
        """Initialize the attributes of a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def get_odometer(self) -> None:
        """Print a statement showing the car's odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, mileage: int) -> None:
        """Update current odometer reading"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles: int) -> None:
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


car1 = Car("Totoya", "86", 1989)
print(car1.get_descriptive_name())
car1.get_odometer()
car1.set_odometer(2000)
car1.get_odometer()
car1.increment_odometer(1)
car1.get_odometer()

