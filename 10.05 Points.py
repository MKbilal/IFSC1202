import math
class Point:
    def __init__(self, Xvalue, Yvalue):
        self.x = Xvalue
        self.y = Yvalue
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
def Distance(A, B):
    distance = math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)
    return distance
def Midpoint(A, B):
    mid_point = Point((A.x + B.x) / 2, (A.y + B.y) / 2)
    return mid_point
def XAngle(A, B):
    slope = (B.y - A.y) / (B.x - A.x)
    angle = math.atan(slope) * 180 / math.pi
    return angle
def main():
    file = open("10.05 Points.txt", "r")
    print("{:>20s} {:>20s} {:>20s} {:>20s} {:>20s}".format("Point A", "Point B", "Distance", "Midpoint", "Angle"))
    print(
        "{:>20s} {:>20s} {:>20s} {:>20s} {:>20s}".format('-' * 15, '-' * 15, '-' * 15, '-' * 15, '-' * 15))
    for line in file:
        values = line.rstrip('\n').split(",")
        x1 = float(values[0])
        y1 = float(values[1])
        x2 = float(values[2])
        y2 = float(values[3])
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        dist = Distance(p1, p2)
        mid = Midpoint(p1, p2)
        xAng = XAngle(p1, p2)
        print("{:>20s} {:>20s} {:>20.7f} {:>20s} {:>20.7f}".format(p1.ToString(), p2.ToString(), dist, mid.ToString(),xAng))
    file.close()
main()