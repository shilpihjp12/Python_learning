

acronyms = ['lol', 'brb', 'smh', 'lmk', 'tbh']

#Add new in list
acronyms.append('idk')
acronyms.append('imho')

print(acronyms[0])
print(acronyms[6])
print(acronyms)

#remove item from list
acronyms.remove('smh')
print(acronyms)

#check for item is available in list
if 'smh' in acronyms:
  print('smh is in the list')
else:
  print('smh is not in the list')

#print items in seperate lint 
print('print items in seperate list:')
for acronym in acronyms:
  print(acronym)



products = ['apple', 'banana', 'orange', 'grape', 'melon']
print(products)

prices = [1.2, 2.3, 3.4, 4.5, 5.6]
print(max(prices)) #max value in a list
quantities = [10, 20, 30, 40, 50]
print(sum(quantities)) #sum of all values in a list

basket = [['apple', 1.2, 10], ['banana', 2.3, 20], ['orange', 3.4, 30], ['grape', 4.5, 40], ['melon', 5.6, 50]]
print(basket)

#accessing list items
#we can access list items using index
print('basket 2nd item', basket[1])
#slicing list
print('basket 2nd - 4th item', basket[1:4])

# -1 index value will give last elemnt in the list
print('basket -1 index value', basket[-1])

# +ve index value that does not exist in the list will give index error
# print('basket 10th index value', basket[10])

#replace item in list
basket[0] = ['apple1', 1.3, 11]

#copying list
A= [1, 2, 3, 4, 5]
B = A #Aliacing, they refer same memory location for data and one list value change imapct the other one
B= list(A) #cloning, they refer different memory location for data and one list value change does not imapct the other one

#List methods
# list.append(item) - add item to the end of the list
# list.remove(item) - remove item from the list
# list.index(item) - get the index of the item in the list
# list.sort(reverse=true) - sort the list
# list.reverse() - reverse the list
# list.count(item) - count the number of times item appears in the list
# list.clear() - remove all items from the list
# text.split() - split the list into a list of lists. e.g. sentence to words list

