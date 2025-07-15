def deco(ff):
    def fs():
        print("starting funtion...")
        ff()
        print("Function finished")
    return fs
@deco
def say_hello():
    print("hello, bhuvan!")
say_hello()