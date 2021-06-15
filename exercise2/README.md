# Exercise 2

Note: Complete code is in the file [exercise2.py](exercise2.py).

## Answer:

Some points in the Python code are wrong or should be noted as listed below:

1. The code has a syntax error in the reserved word **class**. This word must be written with lowercase characters.

1. The class MyClass implements a method called **init** instead of Python's initialization method **\_\_init\_\_**.
Leaving the code as it is, without changing **init** for **\_\_init\_\_** will result in errors when calling any of the other methods because the attribute _my_dict will possibly not exist.

1. We must be aware that **_my_dict** can be accessed from outside our class and if incorrectly changed, having its type modified, for example, MyClass methods will fail. Using a double underscore prefix (name mangling) won't completely prevent this kind of error but will make it harder to happen.

1. If **get_c()** is called before setting the key c, it will raise an exception because the key does not exist.
Here, the method **get** for dicts could be used:

    ```python
    def get_c(self):
        return self._my_dict.get("c")
    ```

1. The method **get_dict_with_twice_a** has some points that should be noted:

    1. The line `buffer = self._my_dict` stores the reference to **_my_dict** into the variable **buffer**. This will cause the line `buffer[“a”] *= 2` to change _my_dict. A possible fix is:

        ```python
        def get_dict_with_twice_a(self):
            buffer = self._my_dict.copy()
            ...
        ```
        But note that if the key **a** had its type changed for dict, for example, we would need a deep copy:

        ```python
        import copy
        ...
        def get_dict_with_twice_a(self):
            buffer = copy.deepcopy(self._my_dict)
            ...
        ```

    2. The line `buffer[“a”] *= 2` has the following problems:

        1. If the key **a** is removed, the line will raise an exception because buffer[“a”] does not exist

        2. If the key **a** has its value changed for a type that doesn't support the **\*** operand, the line will also raise an exception.

        We could catch these exceptions or try to avoid the errors listed above:

        ```python
        def get_dict_with_twice_a(self): 
            buffer = dict(self._my_dict.copy())

            buffer_a = buffer.get("a")
            if hasattr(buffer_a, "__mul__"):
                buffer = buffer_a * 2

            return buffer
        ```