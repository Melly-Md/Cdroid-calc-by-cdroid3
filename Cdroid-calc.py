import time
import math

print("WELCOME TO CDROID-CALC")

username = input("Enter a Username, Example (Melly): ")

select = int(input(f"{username}, Pls Select an Option from the list of available choices below: \n" "Pls Note that Options 12 & 13 are not available in this version, Pls do well to stay tuned for Cdroid-calc_v2\n" "(01):Addition of Numbers\n" "(02):Multiplication of Numbers\n" "(03):Subtraction of Numbers\n" "(04):Division of Numbers\n"  "(05):Square of numbers\n" "(06):Sine of Numbers\n" "(07):Cosine of Numbers\n" "(08):Tan of Numbers\n" "(09):Logarithm of Numbers\n" "(10):Anti-logarithm of Numbers\n" "(11):Square root of Numbers\n" "(12):Differentiation of Numbers\n" "(13):Integration of Numbers\n" "(14):Area of  a Triangle\n" "(15):Area of a Rectangle\n" "(16):Area of a Square\n" "(17):Area of a Circle\n" "(18):Contact Developer\n" "(19):EXIT\n"))

if select == int(1):
     fnum = (int(input("Addition!, Enter the first mumber you would like to Add ")))
     snum = (int(input("Enter the Second number you would like to add: ")))
     addition = int(fnum) + int(snum)
     print(f"{addition} is the sum of {fnum} and {snum}")
  

elif select == int(2):
     mfnum = int(float(input("Multiplication!, Enter the first number you would like to Multiply ")))
     msnum = int(input("Enter the Second number you would like to Multiply: "))
     multiply = int(mfnum) * int(msnum)
     print(f"{multiply} is the product of {mfnum} and {msnum}")
  
elif select == int(3):
     sfnum = int(input("Subtraction!, Enter the First number you want to Subtract from (note:Greater numbers first, then followed by the least number) "))
     ssnum = int(input(f"Enter the number you want to subtract from {sfnum}: "))
     subtract = int(sfnum) - int(ssnum)
     print(f"{sfnum} minus {ssnum} is equal to {subtract}.")
  
elif select == int(4):
     dfnum = int(input("Division!,Enter the number you want to divide: "))
     dsnum = int(input(f"Enter the number you want {dfnum} to be divided by... "))
     division = int(dfnum) / int(dsnum)
     print(f"{dfnum} divided by {dsnum} is {division} ")
     time.sleep(float(0.99))

  
elif select == int(5):
     sqfnum = int(input("Enter the number you want to square: "))
     square = int(sqfnum) * int(sqfnum)
     print(f"{square} is the square of {sqfnum} ")
     time.sleep(float(0.99))
     print("CODED BY 71MELLY")
  
  
elif select == int(6):
     sine_num = int(input("Sine of Numbers!, Enter the number: "))
     num_rad = math.radians(sine_num)
     sine = math.sin(num_rad)
     print(f"The Sine of {sine_num} degrees is {sine}° ")
  
elif select == int(7):
     cosine_num = int(input("Cosine of Numbers!, Enter the Number: "))
     cosine_num_rad = math.radians(cosine_num)
     cosine = math.cos(cosine_num_rad)
     print(f"The Cosine of {cosine_num} degrees is {cosine}°")
  
elif select == int(8):
     tan_num = int(input("Tangent of Numbers!,Enter the Number: "))
     tan_num_rad = math.radians(tan_num)
     tangent = math.tan(tan_num_rad)
     print(f"The Tan of {tan_num} degrees is {tangent}° ")
  
  
elif select == int(9):
     num = int(input("Enter the Number: "))
     base = int(input("Enter the base: "))
     log_with_base = math.log(num,base)
  
     print(f"The Logarithm of {num} and {base} is {log_with_base}")
  
  
elif select == int(10):
     anti_num = int(input("Enter the Number:  "))
     anti_base = int(input("Enter the Base:"))
  
     antilog_with_base = math.pow(anti_base,anti_num)
  
     print(f"The Anti-Logarithm of {anti_num} and {anti_base} is {antilog_with_base} ")

elif select == int(11):
     rt_num = int(input("Enter the Number: "))
     sqrt = math.sqrt(rt_num)
     print(f"The Square root of {rt_num} is {sqrt} ")

elif select == int(12):
      print("Sorry this feature has Crashed!, Pls Check out other Options")
  
elif select == int(13):
     print("Sorry this feature has Crashed,Pls Check out other options")

elif select == int(14):
     base_of_triangle = int(input("Enter the base of the triangle: "))
     height_of_triangle = int(input("Enter the height of the triangle: "))
  
     base_height = int(base_of_triangle)*int(height_of_triangle)
  
     Area_of_triangle = int(base_height)/2
  
     print(f"The Area of The triangle with base {base_of_triangle}cm and height {height_of_triangle}cm is {Area_of_triangle}cm² ")

elif select == int(15):
     length_of_rectangle = int(input("Enter the Length of the Rectangle "))
     width_of_rectangle = int(input("Enter the Width of the Rectangle "))
     Area_of_rectangle = int(length_of_rectangle)*int(width_of_rectangle)
     print(f"The Area of Rectangle with Length {length_of_rectangle}cm and Width {width_of_rectangle}cm is {Area_of_rectangle}cm²")


elif select == int(16):
     length_of_square = int(input("Enter the Length (side) of the Square "))
     Area_of_Square = int(length_of_square)*int(length_of_square)
     print(f"The Area of the Square with side {length_of_square}cm is {Area_of_Square}cm²")

elif select == int(17):
  
     pie_const = float(3.14159)
  
     circle_radius = int(input("Enter the Radius of the Circle "))
     radius_square = int(circle_radius)*int(circle_radius)
     Area_of_Circle = int(pie_const)*int(radius_square)
     print(f"The Area of the Circle with Radius {circle_radius}cm is {Area_of_Circle}cm²")
  
elif select == int(18):
     print("Message via Whatsapp: +2349046239064\n" "Message via Telegram: +2349046239064\n" "Github Handle: Soon\n")
     
else:
     print("Pls Kindly Select From the Options numbered 1 to 18 excluding numbers 12 & 13!!")
     
def tell():
  time.sleep(int(1))
  print("CODED BY 71 MELLY")
tell()
time.sleep(float(0.45))
tell()
time.sleep(float(0.7))
tell()
time.sleep(float(0.9))
print("join our whatsapp group for more info and updates on our tools")
 
 #built by MELLY
 #use codes but give credits to Developer
 #####
def dots():
 print(".............................................................................................................................................................................................\n")
dots()

select = int(input(f"{username}, Thank you for using CDROID-CALC, What Calculations would you like us to help you with? \n" "Pls Note that Options 12 & 13 are not available in this version, stay tuned for Cdroid-calc_v2\n" "(01):Addition of Numbers\n" "(02):Multiplication of Numbers\n" "(03):Subtraction of Numbers\n" "(04):Division of Numbers\n"  "(05):Square of numbers\n" "(06):Sine of Numbers\n" "(07):Cosine of Numbers\n" "(08):Tan of Numbers\n" "(09):Logarithm of Numbers\n" "(10):Anti-logarithm of Numbers\n" "(11):Square root of Numbers\n" "(12):Differentiation of Numbers\n" "(13):Integration of Numbers\n" "(14):Area of  a Triangle\n" "(15):Area of a Rectangle\n" "(16):Area of a Square\n" "(17):Area of a Circle\n" "(18):Contact Developer\n" "(19):EXIT\n"))

if select == int(1):
     fnum = (int(input("Addition!, Enter the first mumber you would like to Add ")))
     snum = (int(input("Enter the Second number you would like to add: ")))
     addition = int(fnum) + int(snum)
     print(f"{addition} is the sum of {fnum} and {snum}")
  

elif select == int(2):
     mfnum = int(float(input("Multiplication!, Enter the first number you would like to Multiply ")))
     msnum = int(input("Enter the Second number you would like to Multiply: "))
     multiply = int(mfnum) * int(msnum)
     print(f"{multiply} is the product of {mfnum} and {msnum}")
  
elif select == int(3):
     sfnum = int(input("Subtraction!, Enter the First number you want to Subtract from (note:Greater numbers first, then followed by the least number) "))
     ssnum = int(input(f"Enter the number you want to subtract from {sfnum}: "))
     subtract = int(sfnum) - int(ssnum)
     print(f"{sfnum} minus {ssnum} is equal to {subtract}.")
  
elif select == int(4):
     dfnum = int(input("Division!,Enter the number you want to divide: "))
     dsnum = int(input(f"Enter the number you want {dfnum} to be divided by... "))
     division = int(dfnum) / int(dsnum)
     print(f"{dfnum} divided by {dsnum} is {division} ")
     time.sleep(float(0.99))

  
elif select == int(5):
     sqfnum = int(input("Enter the First number you want to square: "))
     square = int(sqfnum) * int(sqfnum)
     print(f"{square} is the square of {sqfnum} ")
     time.sleep(float(0.99))
     print("CODED BY 71MELLY")
  
  
elif select == int(6):
     sine_num = int(input("Sine of Numbers!, Enter the number: "))
     num_rad = math.radians(sine_num)
     sine = math.sin(num_rad)
     print(f"The Sine of {sine_num} degrees is {sine}° ")
  
elif select == int(7):
     cosine_num = int(input("Cosine of Numbers!, Enter the Number: "))
     cosine_num_rad = math.radians(cosine_num)
     cosine = math.cos(cosine_num_rad)
     print(f"The Cosine of {cosine_num} degrees is {cosine}°")
  
elif select == int(8):
     tan_num = int(input("Tangent of Numbers!,Enter the Number: "))
     tan_num_rad = math.radians(tan_num)
     tangent = math.tan(tan_num_rad)
     print(f"The Tan of {tan_num} degrees is {tangent}° ")
  
  
elif select == int(9):
     num = int(input("Enter the Number: "))
     base = int(input("Enter the base: "))
     log_with_base = math.log(num,base)
  
     print(f"The Logarithm of {num} and {base} is {log_with_base}")
  
  
elif select == int(10):
     anti_num = int(input("Enter the Number:  "))
     anti_base = int(input("Enter the Base:"))
  
     antilog_with_base = math.pow(anti_base,anti_num)
  
     print(f"The Anti-Logarithm of {anti_num} and {anti_base} is {antilog_with_base} ")

elif select == int(11):
     rt_num = int(input("Enter the Number: "))
     sqrt = math.sqrt(rt_num)
     print(f"The Square root of {rt_num} is {sqrt} ")

elif select == int(12):
      print("Sorry this feature has Crashed!, Pls Check out other Options")
  
elif select == int(13):
     print("Sorry this feature has Crashed,Pls Check out other options")

elif select == int(14):
     base_of_triangle = int(input("Enter the base of the triangle: "))
     height_of_triangle = int(input("Enter the height of the triangle: "))
  
     base_height = int(base_of_triangle)*int(height_of_triangle)
  
     Area_of_triangle = int(base_height)/2
  
     print(f"The Area of The triangle with base {base_of_triangle}cm and height {height_of_triangle}cm is {Area_of_triangle}cm² ")

elif select == int(15):
     length_of_rectangle = int(input("Enter the Length of the Rectangle "))
     width_of_rectangle = int(input("Enter the Width of the Rectangle "))
     Area_of_rectangle = int(length_of_rectangle)*int(width_of_rectangle)
     print(f"The Area of Rectangle with Length {length_of_rectangle}cm and Width {width_of_rectangle}cm is {Area_of_rectangle}cm²")


elif select == int(16):
     length_of_square = int(input("Enter the Length (side) of the Square "))
     Area_of_Square = int(length_of_square)*int(length_of_square)
     print(f"The Area of the Square with side {length_of_square}cm is {Area_of_Square}cm²")

elif select == int(17):
  
     pie_const = float(3.14159)
  
     circle_radius = int(input("Enter the Radius of the Circle "))
     radius_square = int(circle_radius)*int(circle_radius)
     Area_of_Circle = int(pie_const)*int(radius_square)
     print(f"The Area of the Circle with Radius {circle_radius}cm is {Area_of_Circle}cm²")
  
elif select == int(18):
     print("Message via Whatsapp: +2349046239064\n" "Message via Telegram: +2349046239064\n" "Github Handle: Soon\n")
     
else:
     print("Pls Kindly Select From the Options numbered 1 to 18 excluding numbers 12 & 13!!")
     
     
def tell_them():
  print("exited with code 0, press exit then run (python Cdroid-calc.py) command to go back to main menu")

tell()
tell()
tell()
dots()
tell_them()
dots()
 
 