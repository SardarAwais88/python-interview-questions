class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} {self.model} is created.")

# Creating an object of Car class
my_car = Car("Toyota", "Corolla")
```

### **Output:**
```
Toyota Corolla is created.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of the Person class
person1 = Person("Alice", 30)

# The __init__ method is called, and the object's attributes are initialized:
# person1.name = "Alice"
# person1.age = 30

In this example, when you create the person1 object, the __init__ method is called, and the name and age attributes are assigned the values "Alice" and 30, respectively.

Note: The __init__ method is optional, but it's commonly used to initialize objects and provide flexibility in how they are created.