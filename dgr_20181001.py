Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __bui

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __bui
NameError: name '__bui' is not defined
>>> __builtins__
<module '__builtin__' (built-in)>
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.doc__)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(__builtins__.doc__)
AttributeError: 'module' object has no attribute 'doc__'
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a=20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> b=1,56
>>> vars()
{'a': 20, 'b': (1, 56), '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> b=1.56
>>> c='Q'
>>> vars()
{'a': 20, 'c': 'Q', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(a)
<type 'int'>
>>> type(c)
<type 'str'>
>>> 
