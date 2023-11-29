class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    # Getter and setter methods for the 'name' attribute
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # Getter and setter methods for the 'age' attribute
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    # Getter and setter methods for the 'address' attribute
    def get_address(self):
        return self._address

    def set_address(self, new_address):
        self._address = new_address

# Example usage:
person1 = Person("John Doe", 25, "123 Main St")
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())

# Modifying attributes using setter methods
person1.set_name("Jane Doe")
person1.set_age(30)
person1.set_address("456 Oak St")

# Displaying modified attributes
print("Modified Name:", person1.get_name())
print("Modified Age:", person1.get_age())
print("Modified Address:", person1.get_address())
