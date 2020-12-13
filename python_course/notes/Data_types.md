# **Data Types**

## Integer
* Refered to as `int`
* By integers we essentially imply and "round" number
* We can do mathematical calculation directly on ints

## Float
* Refered to as `float`
* any number that has a decimal point (1.2, 5.4, etc...)
* We can do math calc directly on floats

## String
* A string is a series of characters
* Python3 even supports emojis...
* By following the string by a `.` we can see the methods that we can apply to it
* We can do boolean operations on strings
    - The methods can be seen [here](https://www.python-ds.com/python-3-string-methods)
* We have to be careful of alternating quotes in the syntax
    - Ex.: 
        ```python
                my_string = "abc"
                print(my_string + "I don't like quotes") # Works
                print(my_string + 'I don't like quotes') # Doesn't work
        ```
### More string operators
#### **Concatenation**
* `'x' * 5 = 'xxxxx'`
* Membership operator:
    - `in` can be used to check if a string is in another string
    - ex.: `if "a" in "my phrase" return True`
    - We can also use `not in` 
#### String indexing
* Indexing is accessing a value at a given position

In python, indexing is "0"-based.

| H | e | l | l | o |
|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 |

We can then access the value of the given position using `x[0]` for example.\
We can also access the values in reverse using negative numbers

| H | e | l | l | o |
|---|---|---|---|---|
| -5 | -4 | -3 | -2 | -1 |

#### String slicing
`substring = x[start:end]`
* We can also leave `start` or `end` empty if we want "everything" before or after that point
    - Ex.: `"Hello World"[:4]` will print "Hello"\
    `"Hello World"[6:]` will print "World"

`my_str[::-1]` will print the string in reverse

#### String formatting
* String concatenation
    - `print("Hello, my name is " + my_name + " and i\'m " + str(age) + " years old.")`

* Using % formatting
    - `print("Hello, my name is %s and i\'m %d years old." % (my_name, age))`
    - In this case, we simply use %s to say we're going to give it a string, then %d to say we're going to use a digit and we specify them at the end of the string using `% (my_values)`

* Using .format method
    - `print("Hello, my name is {} and i\'m {} years old.".format{my_name, age})`
    - We simply use the wildcard {} and then substitute them in .format in the right order as arguments in `.format(my_values)`

* Using f-strings
    - `my_string = f"Hello, my name is {my_name} and i\'m {age} years old."`
    - We put `f` before the string, and pass the arguments between `{}`
#### Userful string methods and other stuff
* `len()` return the length of the string (starting at 1, 0 if empty)
* `\n` can be used to make a newline
* `.isnumeric()` checks if the string is only numbers
* `.islower()` & `.isupper()` check if the string is all lowercase or upper
* `.lower()` & `.upper()` makes the string lowercase or upper
* `.lstrip()` returns string with leading white spaces removed
*  Etc ...

We can also search for the methods by searching `"python3 string methods documentation"`

## Boleans
The values always start with a capital letter

## The type function
Returns the data type\
Ex.: `print(type(my_str))` will return `<class 'str'>`
