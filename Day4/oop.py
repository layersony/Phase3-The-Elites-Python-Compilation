# class ClassName:
#   def __init__(self): # constructor method
#      pass


class Dog:

    # class attribute
    species = 'Canine'
    
    def __init__(self, name, age, color): # constructor method
        # instance attributes
        self.d_name = name
        self.d_age = age
        self.d_color = color

    # instance method
    def barks(self):
        print(f'{self.d_name} has just barked')


    def yob(self):
        year_of_birth = 2024 - int(self.d_age)
        return year_of_birth
    

    # class Instance methods
    @classmethod
    def create_puppy(cls, name, color):
        puppy_age = 1
        return cls(name, puppy_age, color)


    def __str__(self):
        return f'This is {self.d_name} - Age {self.d_age}'



dog1 = Dog('Buddy', '7', 'brown') # instance
dog2 = Dog('Rita', '5', 'white') # instance

#---------------------------------- Get Instance Attributes
# print( dog1.d_name )
# print( dog1.d_age )

print( dog1 )

# dog1.barks()
# dog2.barks()

# print( dog1.yob() )
# print( dog2.yob() )


#--------------------------------- Get Class attributes
# print( Dog.species )

# print( Dog.barks())

puppy1 = Dog.create_puppy('Faith', 'red')

# print( puppy1.d_name )
# print( puppy1.d_age )