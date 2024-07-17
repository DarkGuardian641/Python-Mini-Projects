x1 = int(input("Enter x-axis of first coordinate: "))
y1 = int(input("Enter y-axis of first coordinate: "))

x2 = int(input("Enter x-axis of second coordinate: "))
y2 = int(input("Enter y-axis of second coordinate: "))

def slope(x1,y1,x2,y2):
    # For finding slope from two points of a line (x₁, y₁) and (x₂, y₂), we use the formula (y₂ - y₁) / (x₂ - x₁)

    print("Slope of the line is",(y2 - y1) / (x2 - x1))

slope(x1,y1,x2,y2)