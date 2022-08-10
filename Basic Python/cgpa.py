import math
total=int(input("enter total\n"))
attendace=int(input("enter attendance\n"))
camarks=int(input("enter ca marks\n"))
theory=int(input("enter the end term marks\n"))
weightage=5/100*attendace+45/100*(camarks/60*100)+50/100*theory
print("total weightage:",weightage)
print("your CGPA is:",weightage/total*9.5)
