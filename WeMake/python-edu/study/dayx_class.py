class MyClass:
    object_count = 0
    common_obj_data   # error
    # common_obj_data = None
    def say(self, _message):
        print (_message)


obj = MyClass()
obj.say("hello")

obj2 = MyClass()
obj2.say("hello? 2nd")

MyClass.common_obj_data = "abc"
print(MyClass.object_count, MyClass.common_obj_data)
