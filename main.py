'''
Text Type (String)
'''

#s = 'this is a single line string'
#print (s)
#print (type(s))

#==========================

#s = """ this is a multi line 
#string example"""
#print (s)

#================================

#Find character by index 
#s =  'string sample'
#print (s[5])

# slicing 
#s= 'string sample'
#print (s[1:6])

#=========================
#immutable

#s= 'string sample'
#s = s[2] = '0'
#print ()


''''
Numeric Type (Integer, Float, Complex )
'''
#x = 1234534567459586
#print (type(x))
# accurate up to 15 - 16 decimal places 
#x = 0.12345678987654321
#print(type(x))
#print (x)

# complex number 
#x = 1+2j 
#print (type(x))
'''
Sequence Type (List, Tuple, Range )
''' 
#List 
#homogeneous means the same 
#x = [10,2.5,'hello']
#print (x[2])
#print (x[1:3])

#mutable 
#x[2] = 'python'
#print (x)

#Tuple provides different types of data 
#heterogeneous means different 
#tuple = ()
#tuple = ('cat', [4,3,2], (1,2,3))


#=========================
# both of examples below are tuples, without comma makes it a string.
#tuple = ("hello",)
#tuple = "hello",
#print (type(tuple))

#=========================

#tuple = ('cat', [4,3,2], (1,2,3))
#print (tuple [2])
#=========================
# immutable 

#tuple = ('cat', [4,3,2], (1,2,3))
#tuple [2] = 10
#print (tuple)

#====================

# range 

# x = range [20]
# for n in x : 
# print (n)

 

#dict = {}
#print (type(dict))

#=====================
#dict is mutable 

#dict = {'name': 'Solomon', 'age': 27}

#print (dict['age'])

#print (dict.get('name'))

#dict ['age'] = 26 
#print (dict)

''''
set type 
'''
#empty set having set = {} is an empty dict 
#set = set() 
#print (type(set))

#====================

#mixed data types ( all immutable)
#set = {3.2, "hi", (1,2,3)}
#print (type(set))
#print (set[0])

#===================
# sets has no duplicates 
#set = {3.2, "hi", (1,2,3), "hi"}
#print (set)

#===========================
# cannot have multiple (list) on a set 
#set = {3.2, "hi", (1,2,3),[1,2,3]}
#unhashable type: 'list'
#print(set)

''''
Boolean Type (true or false )
'''
#print (type(True))

#boolean as numbers 
#print (True == 1)
#print (False == 0)

#interesting logic
#print (True + True)
# not boolean operator
#print ( not True )
#print ( not False )

# and boolean operator 

#print (True and False)
#print (True and True)
#print ( True or False)

# for boolean operator
# print ( True or False)
print ( False or False)

