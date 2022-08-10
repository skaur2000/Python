import java.util.*;
class student
{
int fees=80000;
synchronized void registration(int fees)
{
System.out.println("going to take addmision in lpu.....!!!!");
if(this.fees<fees)
{
System.out.println("less balance....please wait !!!!");

try{
wait();
}
catch(Exception e)
{
}
}
this.fees-=fees;
System.out.println("SUCCESSFULLY GOT ADMISSION...!!!");
}
synchronized void payfees(int fees)
{
System.out.println("going to pay fees");
this.fees+=fees;
System.out.println("FEES PAID SUCESSFULL..!!");
notify();
}
}
class maininter
{
public static void main(String args[])
{
final student S1=new student();
new Thread(){
public void run()
{
S1.registration(850000);
}
}
.start();
new Thread(){
public void run(){
S1.payfees(80000);
}
}
.start();
}
}