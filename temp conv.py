temp = float(input('enter the temperature value'))
unit = input('is the temperature in C or F').strip().upper()
if unit == 'C':
    conv_temp = (temp*9/5)+32
    print(temp,"°C is equal to",conv_temp,"°F")
elif unit == 'F':
    conv_temp = (temp-32)*5/9
    print(temp,"°F is equal to", conv_temp,"°C")
else:
    print("invalid unit")