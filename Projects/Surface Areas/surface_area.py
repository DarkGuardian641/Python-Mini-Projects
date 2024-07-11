shape = int(input("List of all shapes: \n 1. Cube \n 2. Cuboid \n 3. Cone \n 4. Cylinder \n 5. Sphere \n 6. Hemisphere \n Choose a shape: "))

if shape == 1:
    a = float(input("Enter side of cube : "))
    print("Lateral Surface area of cube is ", 4 * a * a)
    print("Total Surface area of cube is ", 6 * a * a)
elif shape == 2:
    l = float(input("Enter the length : "))
    b = float(input("Enter the breadth : "))
    h = float(input("Enter the height : "))
    print("Lateral Surface area of cuboid is ", 2 * h * (l + b))
    print("Total Surface area of cuboid is ", 2 * ((l * b) + (b * h) + (l * h)))
elif shape == 3:
    r = float(input("Enter the radius : "))
    l = float(input("Enter the slant height : "))
    print("Curved Surface area of cone is : ", 3.14 * r * l)
    print("Total Surface area of cone is : ", 3.14 * r * (l + r))
elif shape == 4:
    r = float(input("Enter the radius : "))
    h = float(input("Enter the height : "))
    print("Curved Surface area of cylinder is : ", 2 * 3.14 * r * h)
    print("Total Surface area of cylinder is : ", 2 * 3.14 * r * (h + r))
elif shape == 5:
    r = float(input("Enter the radius : "))
    print("Curved Surface area of sphere is : ", 4 * 3.14 * r * r)
    print("Total Surface area of sphere is : ", 4 * 3.14 * r * r)
elif shape == 6:
    r = float(input("Enter the radius : "))
    print("Curved Surface area of hemisphere is : ", 2 * 3.14 * r * r)
    print("Total Surface area of hemisphere is : ", 3 * 3.14 * r * r)
else:
    print("Enter a valid response!")
