######### FUNCTION RETURNING FUNCTION #########

def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func()

var = outer_func()      #o/p:inside inner func
    



##another

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var= outer_func2("hi! there")
var()       #o/p:message is hi! there
