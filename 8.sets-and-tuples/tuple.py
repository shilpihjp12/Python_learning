#tuples arenot in square bracket rather than they are in normal braces
#tupels are immutable. But it can contain and object with mutable properties
#tuples are faster than lists

#why and when use? - when we dont want to alter the data, when we want to use multiple values from a function
#tuples also support indexing, slicing and membership operations

#e.g.
print('------------------------------------')
products = ('apple', 'banana', 'orange', 'grape', 'melon') #parantheses are optional
print(products)

products = 'apple', 'banana', 'orange', 'grape', 'melon'
print('without paranthese:', products)


print('----------------Immutable Behaviour--------------------')

product_information = ('apple', 1.2, [10, 20])
print(product_information)
#convert tuple to list
product_information = list(product_information)
#update value from 1.2 to 1.8
product_information[1] = 1.8

#convert list to tuple
product_information = tuple(product_information)

print(product_information)

#tuples are immutable.BUt tuple inside any object is there that can be mutable.
product_information[2][0] = 15
print(product_information)


print('--------------Manipulate Tuple----------------------')
mango_information = ('mango', 2.3, [10,15])
lemon_information = ('lemon', 3.4, [20,25])
print(dir(mango_information))

product_information = mango_information + lemon_information
print(product_information)

print('slicing 2-5:', product_information[2:5])

print('--------------Unpacking tuple----------------------')
#unpacking, first variable of left have first value of right
#unpacking should have both sides equal elements in tuples

prices = (1.2, 2.3, 3.4, 4.5, 5.6) #packing
(apple, banana, orange, grape, melon) = prices #unpacking, first variable of left have first value of right
print('apple: ', apple)


(apple, banana, *orange) = prices #* asterick can be used if we have less variables in left side in unpacking
print('orange: ', orange)







