#sets are mutable
#sets are unordered
#sets do not allow duplicates
#sets are written in curly brackets
#sets are unindexed
#can be traferred to immutable set with frozenset() method

print('--------------Sets----------------------')
product_categories = {'fruit', 'vegetable', 'grain', 'dairy', 'protein', 'dairy'}

print(product_categories)

print(type(product_categories))

empty_set={}
print(type(empty_set)) # empty set is dictionary

print('--------------Manipulate Tuple----------------------')

product_categories = {'fruit', 'vegetable', 'grain', 'dairy', 'protein', 'dairy'}

product_categories.discard('dairy')
print(product_categories) #dairy is removed

product_categories.remove('grain')
print(product_categories) #grain is removed

product_categories.add('grain')
print(product_categories) #grain is added

product_categories.add('grain')
print(product_categories) #grain is not added as it is duplicate

product_categories.pop()
print(product_categories) #random item is removed

print('--------------Logical operations----------------------')
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C= {4, 5}


#intersection
print('--------------intersection----------------------')

print(A.intersection(B))

#union
print('--------------union----------------------')
print(A.union(B))

#difference
print('--------------difference----------------------')
print(A.difference(B))

#subset
print('--------------subset----------------------')
print(A.issubset(B))

#superse
print('--------------superset----------------------')
print(B.issuperset(C))
