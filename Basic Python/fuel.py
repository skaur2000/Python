#fuelconsumption calculator

fuel=int(input("Enter the quantity of the fuel:"))
distance=int(input("Enter the distance :"))
print("----------------------------------------------------------");
if fuel<1:
    print(" Invalid input")
if fuel<0:
    print("Invalid input")
if distance<0:
    print("invalid input")
if distance<1:
    print("invalid input")
#result in liters
consumption=(fuel/distance)*100
#print("the fuel consumption is: ",consumption)
print("fuelconsuption in liters is : {: .2f}" .format(consumption))
print("----------------------------------------------------------")
#result in miles
consumption1=consumption*0.6214
#print("fuel consumption in miles: ",consumption1)
print("fuelconsuption in miles is : {: .2f}" .format(consumption1))
print("----------------------------------------------------------")
#result in gallons
consumption2=consumption*0.264172
print("fuelconsuption in gallons is: {: .2f}" .format(consumption2))



