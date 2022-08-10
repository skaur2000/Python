#piggybank contains 10rs,5rs,2rs,1rs coins
coin10=int(input("enter number of 10 rupee coin:"));
if type(coin10)!=int:
    print("enter valid input");
coin5=int(input("enter number of 5 rupee coins: "));
if type(coin5)!=int:
    print("enter valid input");
coin2=int(input("enter number of 2 rupee coin: "));
if type(coin2)!=int:
    print("enter valid input");
coin1=int(input("enter number of 1 rupee coin: "));
if type(coin1)!=int:
    print("enter valid input");
total_amount=coin10*10 + coin5*5 + coin2*2 + coin1*1;
print("total amount in piggybank is : ", total_amount);
          
