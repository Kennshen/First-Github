def length_conversion(value, units):
    if units == "mm":
        new_value = float(value)*25.4
        return new_value
    elif units == "in":
        new_value = float(value)/25.4
        return new_value
    else:
        print("Please use mm or in")
        return False

Success = False
while Success == False:
    ask_value = input("What is the value you want to convert?: ")
    ask_unit = input("What is the value you want to convert?: ")
    Success = length_conversion(ask_value, ask_unit)

print(f"The converted value is {Success} {ask_unit}")

print("I am making a change to github :)")

