class User:
    def __init__(self, name, email):
        self.user_name = name
        self.user_email = email

    def display_info(self):
        return f"UserName: {self.user_name}, Email: {self.user_email}"
    
# class Child(parent):
class Admin(User):
    def __init__(self, name='ibu', email='ebu@gmail.com', user_level='admin'):
        super().__init__(name, email)
        self.user_level = user_level

    def display_info(self):
        updated_info = super().display_info() + f", User-Level: {self.user_level}"
        return updated_info

class RegularUser(User):
    def __init__(self, name='ibu', email='ebu@gmail.com', user_level='regular'):
        super().__init__(name, email)
        self.user_level = user_level

    def display_info(self):
        update_info = super().display_info() + f", User Level: {self.user_level}"
        return update_info


########################################

# regularUser1 = RegularUser('Felix', 'felix@gmail.com', 'regularUser')
# print(regularUser1.display_info())




admin1 = Admin('Nancy', 'admin')      

print( admin1.display_info() )



# user1 = User('Maingi', 'maingi@gmail.com')
# user2 = User('Jane', 'jane@gmail.com')

# print(user1.display_info())
# print(user2.display_info())