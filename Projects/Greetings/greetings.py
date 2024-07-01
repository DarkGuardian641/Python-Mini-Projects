import time

def greeting(name):
    current_hour = time.localtime().tm_hour
    current_time = time.strftime("%I:%M %p")
    
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
    
    return greeting + ", " + name + "! It is " + current_time + "."

# Get the user's name
name = input("Enter your name: ")

# Generate and print the greeting
greeting_message = greeting(name)
print(greeting_message)
