#electricity bill calculator
meter_reading=int(input("enter the consumed units: "));
if meter_reading<=100:
    bill=meter_reading*5.95;
    print("TOTAL BILL IS :",bill);
elif meter_reading>100:
    bill=(meter_reading - 100)*6.95 + 5.95*100;
    print("TOTAL BILL IS :",bill);
else:
    print("INVALID INPUT");
