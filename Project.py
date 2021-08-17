#MPH to KPH converter and Average Speed calculator

print("Welcome to the MPH Converter")

kmh = float(input("What is your speed in MPH: "))
kms = kmh * 1.609
kms_rounded = round(kms, 2)
print("Speed in KPH is: " + str(kms_rounded) + ".")

print("Speed Distance Calculator")

distance = kms_rounded * float(input("Input time (in hours): "))
print("Distance: " + str(distance) + " km")




