# 1️⃣ Variables and Data Types
name = "Abdul Samad"
age = 200
weight = 190.76
is_active = True

print(f"Hello, my name is {name} and I am {age} years old.")  # String Formatting

# 2️⃣ Taking Input from User
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# 3️⃣ Conditional Statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4️⃣ Loops (for, while)
print("\nUsing a for loop:")
for i in range(1, 6):
    print(f"Number {i}")

print("\nUsing a while loop:")
counter = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1

# 5️⃣ Functions
def greet(name):
    return f"Hello, {name}!"

print(greet(user_name))

# 6️⃣ Lists (Arrays in Python)
fruits = ["Apple", "Mango", "Banana"]
fruits.append("Orange")  # Adding item
fruits.remove("Mango")   # Removing item
print("\nFruits List:", fruits)

# 7️⃣ Dictionaries (Key-Value Pairs)
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}
print("\nPerson's Info:", person)
print(f"Name: {person['name']}, Age: {person['age']}")

# 8️⃣ File Handling (Writing & Reading)
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:", content)

# 9️⃣ Exception Handling (Try-Except)
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

# 🔟 Object-Oriented Programming (OOP)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        return f"Car: {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
print("\n", car1.show_details())

