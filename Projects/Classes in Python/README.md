
# Classes in Python

## 🌟 Description
This Python program demonstrates the concepts of Object-Oriented Programming (OOP) using classes, inheritance, and decorators. The program defines a parent class `Employee` and an inherited class `Programmer` to showcase how different types of employees can be managed and their information displayed.

<br>

<p align="center">
  <img src= "https://github.com/user-attachments/assets/24b5246d-6cce-4800-a6e9-89670824f305">
</p>

<br>

## 🔰 Features

### 💠 Parent Class: Employee
The `Employee` class serves as the parent class with basic attributes and methods.

#### 🔹 Constructor
The constructor initializes an `Employee` object with the following attributes:
- `name`: The name of the employee.
- `occupation`: The occupation of the employee.
- `networth`: The net worth of the employee.

#### 🔹 Decorator
The `greet` decorator function adds welcome and farewell messages around the execution of the `info` method.

#### 🔹 Functions inside the class
- `info(self)`: This method prints the employee's name, occupation, and net worth.

### 💠 Inherited Class: Programmer
The `Programmer` class inherits from the `Employee` class and adds additional functionality.

#### 🔹 Methods
- `showlang(self)`: This method prints the programming language the programmer codes in (default is Python).

<br>

## 🔰 Usage

### 💠 Creating Employee Objects
You can create instances of the `Employee` class with the following code:
```python
a = Employee("Harry", "Developer", 10000)
b = Employee("Riyan", "HR", 15000)
c = Employee("Shubham", "Sales Manager", 25000)
```

### 💠 Displaying Employee Information
To display the information of each employee, use the `info` method:
```python
a.info()
b.info()
c.info()
```

### 💠 Creating Programmer Objects
You can create instances of the `Programmer` class, which inherits from `Employee`:
```python
d = Programmer("Jake", "Developer", 60000)
```

### 💠 Displaying Programmer Information
To display the information and programming language of a programmer, use the `info` and `showlang` methods:
```python
d.info() 
d.showlang()
```

<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/416bb679-f053-4bdb-a586-58741cc7d84e)

<br>

## 🤖 Author
[Atharva Baikar](https://github.com/DarkGuardian641)
