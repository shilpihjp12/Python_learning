
expenses = [10.5,20.5,4,6,4,8,3,17,15,9]

sum = 0

for expense in expenses:
  sum = sum + expense

#this function is from python to sum directly
# total = sum(expenses)

# we can use , and seperator in print too
print('you spent $', sum, '')

# we can use , and seperator in print too
# print('you spent by sum function $', float(total), '')


# get list from user
# range function of python
for i in range(7):
  print('Enter an expense:')
  total1 = expenses.append(float(input(" Enter an expense: ")))

print('you spent by range function $', total, '')