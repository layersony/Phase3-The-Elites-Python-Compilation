def my_decorator(func):
    print('Exectution before call of main function')
    func()
    print('Exectution after call of main function')

###########################################################################

@my_decorator
def greeting():
    print('Hello from greetings function')


def goodbye():
    print('Hello from goodbye function')

