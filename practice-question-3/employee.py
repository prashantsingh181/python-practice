class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        if name.count(" ") < 1:
            raise Exception("full_name should have atleast 2 words")
        name_array = name.split()
        self.first_name = name_array[0]
        self.last_name = " ".join(name_array[1:])

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("amount should be a number greater than 0")

        self._salary = amount


emp = Employee("John", "Doe", 50000)
print(emp.full_name)
emp.full_name = "Jane Smith"
print(emp.first_name)
emp.salary = -100
