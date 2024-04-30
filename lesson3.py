"инкаспуляция - это защита данных"

# class Laptops:
#     def __init__(self , model , os , memory):
#         self.model = model
#         self._os = os
#         self.__memory = memory

# huawei = Laptops("Huawei" , "Windows 11" , 512)

# print(huawei.model)
# print(huawei._os)
# print(huawei.__memory)

def users(func):
    
    def start():
        print("Hello World!")
        print("1")
        print("2")
        print("3")
        print("start func")
        func()
        print("Bye!")
    return start

@users
def say():
    print("Hi!")
say()    