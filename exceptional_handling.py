try:
    age = int(input('Enter your age : '))
except Exception as e:
    print('Some error occured',e)