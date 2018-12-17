import sys

unit_array = ['Fahrenheit', 'Celsius', 'Kelvin', 'Rankine']
for idx, val in list(enumerate(unit_array)):
    print("{}: {}".format(idx, val))

try:
    source_unit = int(raw_input('Choose the source unit:'))
    target_unit = int(raw_input('Choose the target unit:'))
    number_unit = float(raw_input("Enter a temperature in {}: ".format(unit_array[source_unit])))
    student_response = float(raw_input('Enter your response: '))
except:
    print("invalid")
    sys.exit(1)

def convert(number, source_unit, target_unit):
    temp = None
    if source_unit == "Fahrenheit" and target_unit == 'Celsius':
        temp = (number - 32)  / 9.0 * 5.0
    if source_unit == "Celsius" and target_unit == 'Fahrenheit':
        temp = 9.0 / 5.0 * number + 32
    if source_unit == "Fahrenheit" and target_unit == 'Kelvin':
        temp = (number - 32) * 5.0 / 9.0 + 273.15
    if source_unit == "Kelvin" and target_unit == 'Fahrenheit':
        temp = (number - 273.15) * 9.0 / 5.0 + 32
    if source_unit == "Fahrenheit" and target_unit == 'Rankine':
        temp = number + 459.67
    if source_unit == "Rankine" and target_unit == 'Fahrenheit':
        temp = number - 459.67
    if source_unit == "Celsius" and target_unit == 'Kelvin':
        temp = number + 273.15
    if source_unit == "Kelvin" and target_unit == 'Celsius':
        temp = number - 273.15
    if source_unit == "Celsius" and target_unit == 'Rankine':
        temp = number * 9.0 / 5.0 + 491.67
    if source_unit == "Rankine" and target_unit == 'Celsius':
        temp = (number - 491.67) * 5.0 / 9.0
    if source_unit == "Kelvin" and target_unit == 'Rankine':
        temp = number * 1.8
    if source_unit == "Rankine" and target_unit == 'Kelvin':
        temp = number * 5.0 / 9.0
    return round(temp, 2)

try:
    temp = convert(number_unit, unit_array[source_unit], unit_array[target_unit])
    if temp == student_response:
        print("correct")
    else:
        print("incorrect")
except:
    print("invalid")
    sys.exit(1)
