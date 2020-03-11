#bmi cal

weight = int (input("Input Weight: ")) #Input น้ำหนัก
height = float (input("Input Height: Cm/Meter")) #Input เมตร

if height > 3:         #ถ้าใส่ความสูงมากกว่า 3 ให้เอาความสูงไปหาร 100 เพื่อจะได้ค่าที่ถูกต้องเพราะไม่มีใครสูงกว่า 3 เมตรแล้ว
    height=height/100


def BMIcal(weight,height): #ประกาศ Function

    return(weight/(height*height))
    

bmi = BMIcal(weight,height) #เรียกใช้ Function
print("BMI = ",bmi) #แสดง BMI

if bmi < 18.5:  #  ถ้า BMI < 18.5 แสดง Underweight
    print("Underweight")

elif  bmi == 18.5 or bmi <24.9: # ถ้า BMI = 18.5 หรือ < 24.9 แสดง Normal Weight
    print("Normal Weight")

elif bmi >= 24.9: # ถ้า bmi >= 24.9 หรือ ถ้า Bmi < 29.9 

    if bmi < 29.9:   #ถ้า bmi < 29.9 ให้แสดง Overweight
        print("OverWeight")

    else:print("Obesity") # ถ้า bmi > 29.9 แสดง Obesity
    

    
  

        

       
  




