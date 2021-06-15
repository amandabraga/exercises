def classify_triangles(sides):
    if is_triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return "Equilateral Triangle"
        if (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]):
            return "Isosceles Triangle"
        return "Scalene Triangle"
    else:
        return "Not a triangle"

def is_triangle(sides):
    return (sides[0] + sides[1] > sides[2]) and\
           (sides[0] + sides[2] > sides[1]) and\
           (sides[1] + sides[2] > sides[0])

def read_triangle_sides():
    try:
        side1 =  int(input("Type in the 1st side: "))
        side2 =  int(input("Type in the 2nd side: "))
        side3 =  int(input("Type in the 3rd side: "))
    except:
        raise ValueError("Sides should be an integer value")

    sides = [side1, side2, side3]

    return sides

if __name__ == "__main__":
    try:
        sides = read_triangle_sides()
        print(classify_triangles(sides))
    except ValueError as error:
        print(f"Error: {error}")