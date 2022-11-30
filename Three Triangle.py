from math import acos,pi,degrees
import math

class Triangle:
    def __init__(self, side1,side2,side3):
        self.s1=side1
        self.s2=side2
        self.s3=side3
    
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        area = (s * (s - self.s1) * (s-self.s2) * (s-self.s3)) ** 0.5
        return area
        
    def type(self):
        if(self.s1==self.s2 and self.s2==self.s3):
            return "Equilateral"
        elif(self.s1==self.s2 or self.s2==self.s3 or self.s1==self.s3):
            return "Isoceles"
        else:
            return "Scalene"
    
    
    def angles(self):
        a = self.s1
        b = self.s2
        c = self.s3
        A = 180/pi*math.acos((b*b+c*c-a*a)/(2*b*c))
        B = 180/pi*math.acos((c*c+a*a-b*b)/(2*c*a))
        C = 180/pi*math.acos((a*a+b*b-c*c)/(2*a*b))
        list = [A,B,C]
        return list

file = open('Exam Three Triangles.txt')
TriangleList=[]
for line in file:
    x = line.split(",")
    x[-1] = x[-1].strip()
    obj = Triangle(float(x[0]),float(x[1]),float(x[2]))
    TriangleList.append(obj)

print("Type\t\tSide 1\t\tSide 2\t\tSide 3\t\tPerimeter\t\tArea\t\tAngle 1\t\tAngle 2\t\tAngle 3")
for x in TriangleList:
    anglesList = x.angles()
    print(x.type()+"\t         "+str(x.s1)+"\t         "+str(x.s2)+"\t          "+str(x.s3)+"\t          "+str(x.perimeter())+"\t            "+str(x.area())+"\t"+str(anglesList[0])+"\t"+str(anglesList[1])+"\t"+str(anglesList[2]))
    