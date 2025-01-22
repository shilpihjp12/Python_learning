
# Get details of loan
money_owned = float(input("Enter the amount of money you owe, in dollar$: ")) #50,000

apr = float(input("Enter the annual interest rate of the loan, in percentage: ")) #3%
payment = float(input("Enter the monthly payment you make, in dollar$: ")) # $1,00
months = int(input("Enter the number of months the loan is for: ")) #24

monthly_rate = apr / 100 / 12

for i in range(months):
  #calculate the monthly payment
  interest_paid = money_owned * monthly_rate
  #Add in interest
  money_owned = money_owned + interest_paid
  #make payment
  money_owned = money_owned - payment

  if money_owned - payment < 0:
    print('The last payment is', money_owned + payment)
    
    

print('paid $', payment, 'of which $', interest_paid, 'was interest.')
print('Now I owe $', money_owned)