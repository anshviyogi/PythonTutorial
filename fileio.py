# Writing to a file -----------------

# with open('test.txt','w') as f:
#     f.write('Hey new line')

# fp = open('test.txt','w')
# fp.write('New Line')
# fp.close()

# Reading to a file ----------------
# with open('test.txt','r') as f:
#     s = f.read()
#     print(s);
#
# fr = open('test.txt','r')
# string = fr.read()
# print(string)
# fr.close()

# Appending to a file
fr = open('test.txt','a')
fr.write('Appending something here')