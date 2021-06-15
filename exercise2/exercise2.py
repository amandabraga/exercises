class MyClass:
    def __init__(self):
        self.__my_dict = {"a":123, "b": True}

    def set_c(self, value):
        self.__my_dict["c"] = value

    def get_c(self):
        return self.__my_dict.get("c")

    def get_dict_with_twice_a(self): 
        buffer = dict(self.__my_dict.copy())

        buffer_a = buffer.get("a")
        if hasattr(buffer_a, "__mul__"):
            buffer = buffer_a * 2

        return buffer