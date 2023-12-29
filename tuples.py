#Tuples cannot be changed like we do in list (l1.append(25))

t1 = (1,2,3,4,5)
print(t1.count(1))

# t1[0] = 20; - will throw an error in tuple but not as in list
# Tuple is immutable and hence, it will throw an error