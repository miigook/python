# data = {'name': 'Peter', 'age': 30}
# person = data.copy()
# print(id(data) == id(person))
# print(id(data), id(person))


#1.  Which exception class is the base class for all built - in exceptions in Python?
# BaseException

# data = (1, 2, 3)
# print(data.__len__())

# cube = [[[1, 2],[3, 4]],[[5, 6],[7, 8]]]
# print(cube[1][1][1])

# Create a 3D cube (2x2x3 - depth x rows x columns)
# cube = [
#     # First layer (depth 0)
#     [[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]]

# # Accessing elements: cube[depth][row][column]
# # first_element = cube[0][0][0]  # = 1
# # middle_element = cube[1][0][1]  # = 8

# # Modifying elements
# # cube[0][1][2] = 99  # Changes 6 to 99

# # Iterating through the cube
# for depth in range(len(cube)):
#     print('depth', cube[depth])
#     for row in range(len(cube[depth])):
#         print('row',cube[row])
#         for col in range(len(cube[depth][row])):
#             print('col',col)
#             print("'") #Position [{depth}][{row}][{col}] = {cube[depth][row][col]}

# a = 1 
# b = 0 
# a = a ^ b
# print('first',a)
# b = a ^ b
# print('second',b)
# a = a ^ b
# print('third',a)

# print(a,b)


# lst = [[x for x in range(4)] for y in range(3)]
# print(lst)
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")

# try:
#     raise ValueError
# except TypeError:
#     print('ss')

# my_list = [1,2]

# for v in range(2):
#     print(v)
#     my_list.insert(-1, my_list[v])
# print(my_list)

#Output [1, 1, 1, 2]

# list = [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(list))
#Output [0, 1, 4, 9]

# def fun(x,y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)

# print(fun(0, 3))
# my_tuples=(5,2,7,4)
# my_tuples = my_tuples[1] + my_tuples[0]

# print(my_tuples)

# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# print(nums)
# print(vals)
#Output of nums and vals will be [ ] empty, del vals slicing deletes both lists 
# values because it points to same list 

# lst = [i for i in range(-3, -1)]
# print(lst)
#Output: [ ]

# try:
#     value = input ("Enter a value: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Bad input....")
# except ZeroDivisionError:
#     print("Very bad input... ")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Boo! ")

# Number works
# but with characters you get a ValueError and print “Bad input”

# try:
#     print(5/0)
# except:
#     print("Sorry, something went wrong... ")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")
#Output: SyntaxError: 'break' outside loop. 

# and except: must be a last:

# dct = {'one':'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)
# #Output is : one

# dct = {}
# dct['1'] = (5, 6)
# dct['2'] = (3, 4)

# for x in dct.keys():
#     print(dct[x][1], end="")


#Output is : 21 comes from dct keys values second index: because 
# it is in dct[x][1], end””

# combines it n one line

# foo = (1, 2, 3)
# foo.index(0)



# def fun(x):
#     if x % 2 == 0:
#         return 1 
#     else:
#         return 7

# print(fun(fun(2)))

# Function gets invoked 2 times, just like double indexing

# first time invoke fun(2) gets return which is 1 and that doesn’t 
# meet the condition so else: condition executed and we get #Output 2


# print(-6 // 4 )
#Output -2 roundig goes to the lesser integer in this case it's negative -2
# lst = [3, 1, -2]
# print(lst[lst[-1]])
#Output: 1 , because it's double indexing

# var = 1
# while var < 10:
#     print(var)
#     var = var << 1
    
# lst = [[0, 1, 2, 3] for i in range(2)]
# print(lst)
# print(lst[2][0])

# for i in range(1):
#     print("#")
# else:
#     print("#")
    
# a = 1
# b = 0
# c = a & b # 0
# d = a | b  # 1
# e = a ^ b  # 1

# print(c + d + e )
#output is 2

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

#Output: # # # 

# var = 2
# while var < 10:
#     print("#")
# var = var >> 1
# print(var)
#Output : NameError: name 'var' is not defined, 
# <<>> shifting is just adds and doubles

# list = [i for i in range(-1, 2)]
# print(list)

# lst = [[0, 1, 2, 3] for i in range(2)]
# print(lst[2][0])

# IndexError: list index out of range, because list inside list will double in for 
# loop range which is 0,1 so 2 lists will be create and index[2] not exist


# t = [[3-i for i in range (3)] for j in range(3)]
# # 3, 2, 1  3, 2 1  3, 2, 1 
# s = 0
# for i in range(3):
#     # 0 1 2
#     s += t[i][i]
#     # 3,2, 1
# print(s)
#output is 6

# lst = [1, 2, 3, 4]
# print(lst[-3:-2])
#output: 2

# vals = [5, 1, 2]
# vals.insert(0, 1)
# del vals[1]

# print(vals)
#output [1, 1, 2] sum 4

# lst = [1, 2, 3]
# for v in range(len(lst)):
#     3
#     lst.insert(1, lst[v])
#     # 1  1,1,1 2,3

# print(lst)  #output: [1, 1, 1, 1, 2, 3]

# lst = ['Mary', 'had', 'a', 'little', 'lamb']

# def lst(lst):
#     # del lst[3]
#     # lst[3] = 'ram'
#     pass

# print(type(lst(lst)))
#runtime Error

# dictionary = {}
# lst = ['a', 'b', 'c', 'd']

# for i in range(len(lst)-1):
#     dictionary[lst[i]] = (lst[i],)
# # print(dictionary)

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(dictionary[i][0])
#     print(dictionary[i] [0])

# it makes choose keys which prints values as a tuple, and indexing them with 0
# will print a b c

# def fun(x):
#     x+= 1 
#     return x

# x = 2 
# x = fun(x + 1)
# print(x)
#Output is 4 , first x declared 2 then added +1 in invoking function

# in function it adds +1 , prints after all operations is 4

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup [0]
# print(tup)

#output is: 2 , tuple get assigned new elements from index 1 and last index-1 which are 2,4

# then, it gets reassigned index 0, which is 2 , prints out single integer 2 , 
# cause to make it tuple we need ,


# a = 5
# b = 1 
# c = a > b and b < a or a == 1
# print(c)
#output is True: because or condition comes first to compare everything after it 
# condition for condition.  

# for x in 'I am having fun today':
#     print(x)

# try:
#     val = int(input("provide num: "))
#     print(val/val)
# except TypeError:
#     print('a')
# except ValueError:
#     print('b')
# except ZeroDivisionError:
#     print('c')
# except:
#     print('d')

#output b

# x = 4
# y = 4 
# z = 3
# print(x == y or z)

#Output: 3
# my_lst = [ x * x for x in range(5)]

# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_lst))
#Output: [0, 1, 4, 9] because of double indexing

# a = 1
# b = 0

# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)
#Output: 0 1

# val = input("Enter: ")
# print(int(val)/len(val))
# print(0/5) output: 0.0

# def func(a, b):
#     return b ** a 

# # print(func(b=2, 2)) Output: error, named arguments must be last

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)

# print(fun(0, 3))
#Output is: 0 because fun calls itself until if condition met

# print = "hello"
# print(print)

# lst = [[x for x in range(3)] for y in range(3)]
#     # [[0, 1, 2][0, 1, 2][0, 1, 2]]
# for r in range(3):
#     for c in range(3):
#         # print(lst[r][c])
#         if lst[r][c] % 2 != 0:
#             print("#")
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return

# print(fun(fun(2)) + 1)

#output is Error, cause + 1 operation is outside arithmetic operations

# value = input("Enter: ")
# print(value/value)

#Output: TypeError: unsupported operand type(s) for /: 'str' and 'str'

# def fun(x=0):
#     return x

# print(fun(5))

# def fun_1(a):
#     return a ** a
    
# def fun_2(a):
#     return fun_1(a) * fun_1(a)

# print(fun_2(2))

# power = 1
# while power < 5:
#     power += 1
#     print ("@", end="")
#     if power == 3:
#         break

# else:
#     print("@")

#Output is @@ because else for while will be executed regardless. 

# torq = 1

# while torq < 2:
#     torq *= 2
#     print("*", end="")
# else: 
#     print("*")
#Output: ** while condition executed once thus printing * and second * printed by else:
 
# train_speed = {"FlyingS": 201, "TGV": 320, "Shinkansen": 320}

# for train in train_speed:
#     print(train, end="")
#output is: FTS, when dictionary get iterate by for loop , it takes keys


# def com(w, h=10, d=0, is_3D=False):
#     return [is_3D, w , h, d]
#     #Output: [False, 2, 1, 0]
# print(com(h=1, w=2)[3])
#index[3] is 0 so output is 0. so function invocation comes with indexing, and print

# def samp(value):
#     return value + value

# x = samp(value =1)
# y = samp(x)
# print(y)
#output is 4: because of each invokation of the function it adds, and samp(x) is samp(value=x) which is 2

# def process(data):
#     data = [1, 2, 3]
#     return data[-2]

# measurements = [0 for i in range(3)] #list comprehension expression in 0 and it ranges 3 times 0
# print(measurements, "before invoke")
# process(measurements)
# print(measurements,"after invoke")

# torq = 0
# while torq != 0:
#     torq //=2
#     print("*", end= "")
# else:
#     print("*")

