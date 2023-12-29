dict1 = {"name":"Ansh", "age":20, "school":"Delhi"}

dict1['city'] = 'Bareilly'

# print(dict1['xyz']); #error - because there's no key named as xyz
#to resolve this we use get

print(dict1.get('name'))
print(dict1.get('xyz')) # No error, will return none