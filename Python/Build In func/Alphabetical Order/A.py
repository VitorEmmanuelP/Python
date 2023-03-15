# Abs: Turn any number into posite value
# print(abs(-7))
# print(abs(-5.20))
# lista = [1,-2,5,-6,9,8,-78]
# lista = [abs(number) for number in lista]

# All: return True if all the elements of the iterable are true or if the iterable is empty

# all(1)
# Error
#all('hello')
#True
#all('')
# True
#all([False])
# False
#
# listSame = [1,1,1]
# listDiff = [1,2,3]
#
# all([x == 1 for x in listSame])
# # True
# all([x == 1 for x in listDiff])
#False


# Any: Return True if any element of the iterable is true,( if iterable is empty return False )

# any('')
# # False
# any(['',False,0])
# # False
# any(['',False,1])
# # True
#
# names = ['Vitor', 'Kevem', 'Joao']
# any([x == 'Vitor' for x in names])
# True

# ASCII: Returns a string with the representation of an object
# https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/ASCII-Table.svg/1261px-ASCII-Table.svg.png

#print(ascii('caçada'))
# 'ca\xe7ada'