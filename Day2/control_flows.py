## if conditions

sunny = True # go out with light cloths
raining = False # go out with umbrella
chilly = True # go out with heavy cloths

# syntax
# if condition:
#    do something
# elif condition:
#   do something
# else:
#   do something

# if sunny == True:
#     print("go out with light cloths")
# elif raining == True:
#     print("go out with umbrella")
# else:
#     print("go out with heavy cloths")

# if... elif .... else

# if (sunny == True) and (raining == True):
#     print('go out with light cloths and carry umbrella')
# elif sunny == True and chilly == True:
#     print('Jipange vizuri')
# else:
#     print('Stay indoors')

# JS     PYTHON
# &&     and
# ||      or
    

# ----------------------------------------------------------------
    
####### loops
# for loop
    # for ... in
    # for ... for
# while loop
    # do.. while loop

# break
# continue


# syntax
# for variable in array:
    # do something

# fruits = ['apple', 'orange', 'pineapple', 'watermelon', 'mango']

# # for fruit in fruits:
# #     if fruit == 'pineapple':
# #         print('pineapple found')
# #         continue

# #     print(fruit)
# print(range(10))

# for number in range(10):
#     print(number)

####################### While Loop
    
# syntax

# variable
# while condition:
    # do something

    # increment

# curr_no = 10

# while 0 < curr_no:
#     curr_no -= 1 # increment

#     if curr_no == 5:
#         print('Niko Hapa number 5')
#         continue

#     print(curr_no)
    
#################################################### decorators


# syntax
# def fnName:
#     pass

def my_decorator(mainfunc):
    print('before excution of main function')
    mainfunc()
    print('after excution of main function')

def greeting_hello():
    print('Morning From Greeting hello function')

def goodbye():
    print('goodbye from goodbye function')


gree
