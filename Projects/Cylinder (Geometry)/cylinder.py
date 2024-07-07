
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

def volume(radius,height):
    volume = 3.14 * radius * radius * height 
    # vol = π r² h
    print("The volume of cylinder is: ", volume)


def surface_area(radius,height):
# surface area = 2π r h + 2π r²
    surface_area = (2 * 3.14 * radius * height) + (2 * 3.14 * radius * radius) 
    print("The surface area of cylinder is: ", surface_area)

volume(radius,height)
surface_area(radius,height)