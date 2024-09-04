جب آپ ایک کلاس کو کال کرتے ہیں اور ایک object بناتے ہیں، تو سب سے پہلے جو چیز trigger ہوتی ہے وہ کلاس کا **constructor** ہوتا ہے۔ Python میں، یہ constructor `__init__` method کے طور پر جانا جاتا ہے۔

### **Explanation:**
- جب بھی آپ کسی کلاس کا object بناتے ہیں، Python خود بخود `__init__` method کو کال کرتا ہے۔
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
