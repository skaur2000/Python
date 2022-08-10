# employee salary calculator
name=str(input("enter name of the employee:"));
salary=int(input("enter the salary of the employee:"));
if salary>=10000 and salary <=20000:
    total_salary=salary*30/100;
    print(total_salary)
    print("Name of the employee :{} salary is: {}".format(name,total_salary));
if salary>=30000 and salary <=40000:
    total_salary=salary*40/100;
    print("Name of the employee :{} salary is: {}".format(name,total_salary));
if salary>=50000 and salary <=60000:
    total_salary=salary*50/100;
    print("Name of the employee :{} salary is: {}".format(name,total_salary));
if salary>60000:
    total_salary=salary*60/100;
    print("Name of the employee :{} salary is: {}".format(name,total_salary));

