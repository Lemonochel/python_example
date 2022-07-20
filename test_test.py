
def examp_type():
    var = input()
    type_var = type(var)
    print(type_var)
    return type_var
    

def answer(inkog_type):
    if inkog_type == ("<class 'str'>"):
        print('this is string')
    elif inkog_type == ("<class 'int'>"):
        print('this is integer')



test = examp_type()
answer(test)
