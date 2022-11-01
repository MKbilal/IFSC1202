class Car:
    def _init_(self, Year, Make): #constructor
        self.Year = Year
        self.make = Make
        self.Sspeed = 0

    def Accelerate(self, value):
        self.Speed = self.speed + value

    def Brake(self, value):
        self.Speed = self.Speed - value
        if self.Speed < 0: #if speed goes below 0, assign 0 to speed
            self.Speed = 0

def changespeed(x):
    if x > 0:
        cari.Accelerate(x)
    else:
        cari.Brake(-x) #-x as the function accepts positive deceleration values

feopen("10.03 Cars.txt", "r") #open file car.txt in reading mode

fl =f.readlines() #readlines() reads the file untill EOF is encountered, and returns a List containing the Lines
l1 = fl{o].split(” *) #read the first record which contains the car year and the make
car1 = Car(11[0],11[1]) #instantiate a car object with the first record extracted from the file

for x in fl[1:]: #loop through the Lines extracted from car.txt, skip first Line
    changespeed( float (x))

print(f'vear : {car1.Year}')

print(f'Make : {car1.Make}')

print(f'Speed : {car1.Speed}')

f.close() #close file once we are done working with it, always a good practice
