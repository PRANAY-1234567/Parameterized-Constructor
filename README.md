# 👤 Person Class with Parameterized Constructor (Python OOP)

## 📌 Description

This Python program demonstrates the use of a **parameterized constructor** in a class. It creates multiple `Person` objects with different names and ages, and displays their details.

---

## 🚀 Features

* Defines a `Person` class
* Uses a parameterized constructor (`__init__`)
* Stores name and age for each object
* Displays details using a method

---

## 🛠️ How It Works

1. A class `Person` is created.
2. The constructor (`__init__`) takes two parameters:

   * `name`
   * `age`
3. These values are assigned to instance variables.
4. A method `display()` is used to print the details.
5. Three objects (`p1`, `p2`, `p3`) are created with different data.
6. Each object calls the `display()` method.

---

## 💻 Code

```python id="j4x9pq"
class Person:
    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}\tAge : {self.age}")


# Main program

p1 = Person("Sakshi-1s", 20)
p2 = Person("Sakshi-2", 21)
p3 = Person("Pranay", 23)

p1.display()
p2.display()
p3.display()
```

---

## ▶️ Example Output

```id="v8l2md"
Name : Sakshi-1s	Age : 20
Name : Sakshi-2	Age : 21
Name : Pranay	Age : 23
```

---

## 📚 Concepts Used

* Class and Object
* Parameterized constructor (`__init__`)
* Instance variables
* Methods

---

## 🎯 Use Case

This program helps beginners understand:

* How to pass values during object creation
* How different objects can store different data

---

## 🔧 Future Improvements

* Take user input for name and age
* Add validation (e.g., age cannot be negative)
* Add more attributes (address, phone number)
* Store multiple persons using a list

---

## 📄 License

This project is open-source and free to use.
