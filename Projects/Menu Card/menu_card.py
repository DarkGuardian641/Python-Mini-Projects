prices = {"Soup": "Rs 100", "Fried Rice": "Rs 140", "Noodles": "Rs 130", "Burger": "Rs 80", "Pizza": "Rs 180"}

more = "yes"

while more == "yes":
    choice = int(input("Choose an item to order \n Press 1 for Soup \n Press 2 for Fried Rice \n Press 3 for Noodles \n Press 4 for Burger \n Press 5 for Pizza \n Press 0 to exit \n"))
    
    if choice == 1:
        print("Soup costs", prices["Soup"])
    elif choice == 2:
        print("Fried Rice costs", prices["Fried Rice"])
    elif choice == 3:
        print("Noodles costs", prices["Noodles"])
    elif choice == 4:
        print("Burger costs", prices["Burger"])
    elif choice == 5:
        print("Pizza costs", prices["Pizza"])
    elif choice == 0:
        break
    else:
        print("Enter a valid input")
        
    more = input("Do you want to order anything else? (yes/no): ")

print("Thank you for your order!")