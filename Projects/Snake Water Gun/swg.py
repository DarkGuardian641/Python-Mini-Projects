import random

user = input("Enter your choice: ")
print("User went with ", user)

rps_choice = ["Snake", "Water", "Gun"]

comp = random.choice(rps_choice)
print("Computer went with",comp)

if user == comp:
    print("Tie!")
elif (user == "Water" and comp == "Snake") or (user == "Snake" and comp == "Gun") or (user == "Gun" and comp == "Water"):
    print("Computer Wins!")
elif (user == "Snake" and comp == "Water") or (user == "Gun" and comp == "Snake") or (user == "Water" and comp == "Gun"):
    print("User Wins!")
else:
    print("Enter a valid response!")