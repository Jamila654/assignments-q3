#type:ignore

#1. Using self
class Student:
    name = None
    marks = None
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student = Student("John", 85)
student.display()
print("assignment 1 done\n")

#2. Using cls
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
    @classmethod
    def display_count(cls):
        print("Count:", cls.count)
    #how many objects are created
    @classmethod
    def object_count(cls):
        return cls.count

counter = Counter()
counter.increment()
counter.increment()
counter.display_count()
print("Number of objects created:", Counter.object_count())
print("assignment 2 done\n")

#3. Public Variables and Methods
class Car:
    brand = None
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} car started")

car = Car("Toyota")
car.start()
print("assignment 3 done\n")

#4. Class Variables and Class Methods
class Bank:
    bank_name = "MyBank"
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()
bank1.change_bank_name("NewBank")
print("Bank 1 Name:", bank1.bank_name)
print("Bank 2 Name:", bank2.bank_name)
print("assignment 4 done\n")

#5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
print("Sum:", MathUtils.add(5, 3))
print("assignment 5 done\n")

#6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger created")
    def __del__(self):
        print("Logger destroyed")
logger = Logger()
del logger    
print("assignment 6 done\n")

#7. Access Modifiers: Public, Private, and Protected
class Employee:
    name = "Alice"
    _salary = 50000
    __ssn = "123-45-6789"
employee = Employee()
print("Name:", employee.name)
print("Salary:", employee._salary)
# The following line will raise an error because __ssn is private
# print("SSN:", employee.__ssn)
print("assignment 7 done\n")

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def display(self):
        super().display()
        print("Subject:", self.subject)
teacher = Teacher("Bob", "Math")
teacher.display()
print("assignment 8 done\n")

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # pass means no implementation
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())
print("assignment 9 done\n")

# 10. Instance Methods
class Dog:
    name = None
    breed = None
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!\nBreed: {self.breed}")
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
print("assignment 10 done\n")

# 11. Class Methods
class Book:
    total_books = 10
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book()
book2 = Book()
book1.increment_book_count()
print("Total Books:", book1.total_books)
print("Total Books:", book2.total_books)
print("assignment 11 done\n")

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
print("Celsius to Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(25))
print("Fahrenheit to Celsius:", TemperatureConverter.fahrenheit_to_celsius(77))
print("assignment 12 done\n")

# 13. Composition
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
        print("Car started")
car = Car()
car.start()
print("assignment 13 done\n")

# 14. Aggregation
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        print(f"Employees in {self.dept_name}:")
        for employee in self.employees:
            print(f"Name: {employee.name}, ID: {employee.employee_id}")
if __name__ == "__main__":
    # Create Employee objects independently
    emp1 = Employee("John Doe", 101)
    emp2 = Employee("Jane Smith", 102)
    # Create Department and add existing Employee objects
    dept = Department("Engineering")
    dept.add_employee(emp1)
    dept.add_employee(emp2)
    # Print department details
    print(dept)
    dept.display_employees()
    # Employee objects still exist independently
    print("\nIndependent employee:")
    print(emp1)
print("assignment 14 done\n")

# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B, C):
    def show(self):
        print("D")
d = D()
d.show()
print("MRO:", D.mro())
print("assignment 15 done\n")

# 16. Function Decorators
def log_function_call(func):
    print("Function is being called")
def say_hello():
    print("Hello!")
log_function_call(say_hello)
print("assignment 16 done\n")

# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        print("Hello from Decorator!")
    cls.greet = greet
    return cls
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)
person = Person("Alice")
person.display()
person.greet()
print("assignment 17 done\n")

# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Price must be positive")
    @price.deleter
    def price(self):
        del self._price
product = Product(10)
print("Price:", product.price)
product.price = 20
print("Price:", product.price)
del product.price
print("assignment 18 done\n")

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return x * self.factor
multiplier = Multiplier(3)
#callable() checks if an object appears callable
print("Is multiplier callable?", callable(multiplier))
print("3 * 5 =", multiplier(5)) 
print("assignment 19 done\n")

# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    else:
        print("Valid age:", age)
try:
    check_age(-5)
except InvalidAgeError as e:
    print("Caught an exception:", e)
print("assignment 20 done\n")

# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < 1:
            raise StopIteration
        self.start -= 1
        return self.start
countdown = Countdown(5)
print("Countdown")
for num in countdown:
    print(num)
print("assignment 21 done\n")