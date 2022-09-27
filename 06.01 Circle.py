import math
def diameter(radius):
    return 2 * radius
def circumference(radius):
    return 2 * radius * math.pi
def area(radius):
    return math.pi * radius * radius
def main():
    file = open('06.01 Radius.txt')
    file_bracket = []
    while True:
        line = file.readline()
        if not line:
            break
        else:
            file_bracket.append(float(line))
    print('{:>15} {:>15} {:>15} {:>15}'.format('Radius','Diameter','Circumference','Area'))
    for radius in file_bracket:
        print('{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}'.format(radius,diameter(radius),circumference(radius),area(radius)))
if __name__ == "__main__":
    main()