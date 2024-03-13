# sequence - list, array, tuple

# my_numbers = [12,8,7,6,5,4,3,2,1,9,8,7,11,10,9,0]

# my_numbers.sort(reverse=False)

# print( my_numbers ) # intergers
# print( sorted(months) ) # strings


# months.append('Nov')

# months.insert(2, 'Dec')


### Remove 
# .pop()
# .remove()
# .clear()
# del()


# del(months[4])

# array[starting : ending : interval]

# non-destructive methods
# slicing 
# list(<orignal list>)
# package copy
# sorted()

# destructive methods
# append
# extend
# # .pop()
# # .remove()
# # .clear()
# # del()
# .sort()

# myName = 'String'

# for letter in myName:
#     print(letter)



# list comprehension (one liner)
# my_list = []

# for i in range(10):
#     my_list.append(i)

# print(my_list)

# my_list = [ i for i in range(10) ]

# print(my_list)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

# my_list = []

# for i in months:
#     if i.startswith('A'):
#         my_list.append(i)

# my_list = [ i for i in months if i.startswith('M') ]     

# print(my_list)


# sets (unique, unordered, mutable)


# my_set = set([1,4,6,9,2,6,2,1,4,5,5,5,3,3])

# print(my_set)


# dicts
# my_dict = {
#     key: value,
#     key: value
# }



# print( my_car['engine'] )

# print( my_car.get('engine') )


# my_car['engine'] = '4000cc'

# my_car.update({'engine':'4000cc'})



my_car = {
    'brand': 'Toyota',
    'price': 569909,
    'color': 'white',
}

# for data in my_car:
#     print(data)

for data in my_car.values():
    print(data)

# for key, value in my_car.items():
#     print(f'{key}  --------- {value}')



