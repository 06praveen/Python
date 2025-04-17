# Develop any converter such as Rupees to dollar, temperature convertor and
# inch to feet.
Rs=int(input("Enter the value of Rupees : "))
dollar=Rs/86
print("The value of",Rs,"Rs in dollar is : ",dollar,"$")

celcius=int(input("Enter the temperature in 'C : "))
fah=(9*celcius/5)+32
kel=celcius+273
print("The",celcius,"'C Temp. in Fahrenheit and Kelvin is",fah,"'F and",kel,"K")

inch=float(input("Enter the value in inch : "))
feet=inch/12
print("The value of ",inch,"in feet is : ",feet)