جب آپ ایک کلاس کو کال کرتے ہیں اور ایک object بناتے ہیں، تو سب سے پہلے جو چیز trigger ہوتی ہے وہ کلاس کا **constructor** ہوتا ہے۔ Python میں، یہ constructor `__init__` method کے طور پر جانا جاتا ہے۔

### **Explanation:**
- جب بھی آپ کسی کلاس کا object بناتے ہیں، Python خود بخود `__init__` method کو کال کرتا ہے۔
jab b ap Kisi class ka object banate Hain  to python hud ba hud __init__` method ko call karta hai.
__init__` method ka Kam object ki initialization Yani object ki initial state ko set karta Hain 
- `__init__` method کا کام object کی initialization کرنا ہوتا ہے، یعنی اس object کی ابتدائی حالت (initial state) کو سیٹ کرنا۔
- آپ `__init__` method کے اندر object کے attributes کو define کر سکتے ہیں اور انہیں ابتدائی values دے سکتے ہیں۔

### **Example:**

```python
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
```

### **Explanation:**
- جب `my_car = Car("Toyota", "Corolla")` execute ہوا، تو `__init__` method سب سے پہلے trigger ہوا اور `brand` اور `model` کو initialize کیا گیا۔
- `__init__` کی وجہ سے "Toyota Corolla is created." message print ہوا۔ 

یہی وہ چیز ہے جو کلاس کا object بناتے وقت سب سے پہلے trigger ہوتی ہے۔





`super()` کا استعمال Python میں inheritance کے دوران parent class کے methods اور attributes کو child class میں access کرنے کے لیے کیا جاتا ہے۔ یہ خاص طور پر اس وقت مفید ہوتا ہے جب آپ parent class کے behavior کو override کر رہے ہوں، لیکن پھر بھی آپ کو parent class کا original behavior استعمال کرنا ہو۔

### **`super()` کے استعمال کے طریقے:**

1. **Parent Class کا Constructor (`__init__`) Call کرنا:**
   - جب آپ child class کے constructor میں parent class کے constructor کو call کرنا چاہتے ہیں تاکہ parent class کے attributes یا methods کو properly initialize کیا جا سکے۔

2. **Parent Class کے Methods کو Override کرتے وقت Original Method کو Access کرنا:**
   - جب آپ child class میں کسی method کو override کر رہے ہوں اور ساتھ ہی parent class کے original method کو بھی call کرنا ہو۔

### **Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Parent class کا constructor call کر رہے ہیں
        self.breed = breed
    
    def speak(self):
        parent_speak = super().speak()  # Parent class کا method call کر رہے ہیں
        return f"{parent_speak} And it barks."

# Dog class کا object بنا رہے ہیں
my_dog = Dog("Buddy", "Golden Retriever")

# Methods کو call کر رہے ہیں
print(my_dog.speak())
```

### **Output:**
```
Buddy makes a sound. And it barks.
```

### **وضاحت:**

1. **Constructor (`__init__`) میں `super()` کا استعمال:**
   - `Dog` class کے `__init__` method میں `super().__init__(name)` کے ذریعے `Animal` class کا constructor call کیا گیا تاکہ `name` attribute کو initialize کیا جا سکے۔

2. **Method Override کرتے وقت `super()` کا استعمال:**
   - `Dog` class میں `speak` method کو override کیا گیا ہے، لیکن `super().speak()` کے ذریعے `Animal` class کے original `speak` method کو بھی call کیا گیا، جس سے parent class کا behavior بھی برقرار رہا۔

`super()` کا استعمال آپ کو parent class کے methods اور attributes کو child class میں access کرنے کی flexibility دیتا ہے، جس سے code کو reusability اور maintainability بہتر ہوتی ہے۔
