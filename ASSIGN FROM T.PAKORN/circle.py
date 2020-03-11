#circle

radius = float (input("Input Radius ")) #Input radius


def Circal(radius):
    Cir = 3.14*2*radius #สูตรหาเส้นรอบวง
    print("Cir = ",Cir) #แสดงเส้นรอบวง

def Areacal(radius):
    area = 3.14*(radius**2) #สูตรหาพื้นที่

    print("Area = ",area) #แสดงพื้นที่

Circal(radius) #function Circal
Areacal(radius) #function Area