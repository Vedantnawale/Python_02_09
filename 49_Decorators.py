def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank for using this function")
    return mfx


@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)  # for printing this we need to use *args --> All arguments are included as a tuple, **kwargs --> All arguments are included as a Dictionary


#  greet(hello)() line 18 replaced by line no. 9
hello()
# greet(add)(1,2) line 20 replaced by line no. 13
add(1,2)
