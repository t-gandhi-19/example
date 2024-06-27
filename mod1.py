from mod2 import function_b
def function_a():
    function_b()
    x = ClassX()
    x.method_y()

class ClassX:
    def method_y(self):
        pass
