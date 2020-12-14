# Functions
## Declaring functions
To declare a function we use `def` followed by the name and `:`. Ex.:
```python
    def my_func(:
        print("something")
```
The content of a function is noted by the indentation.

To execute a function you must call it in the script. 
```python
    my_func()
```
Unless called, the python interpreter will not read the function unless it's called.

## Arguments and parameters
A parameter is a named entity within the scope of the function, which will act as a variable, to which an argument will be passed when calling the said function.

An argument is the value passed when calling the function. Ex.:
```python
    def my_func(parameter):
        print(parameter)
    
    my_func(argument)
```
## Keyword arguments
Passing args as keyword args prevents errors from not passing the args in the right order (positional arguments errors)
Ex.:
```python
    def greet(name, age, gender):
        print(f"Hi {name}, you are {age} and you are a {gender}.")
    greet(age=24, gender="male", name="ced")
```

## *args
`*` is called the unpacking operator.
`*args` will let us provide any numbers of arguments.
Using `*`, python will save all of the given arguments in a tuple. Ex.:
```python
    def my_func(*args):
        print(args)
    my_func() # will work
    my_func(1,2,3,4,5,6) # will work
```

## **kwargs
`**kwargs` or `Keyword Arguments`, will let us pass any number of arguments with a given keyword.

It will also unpack all of the arguments in a dictionary (how fucking neat!)\
Ex.:
```python
    def my_func(**kwargs):
        print(kwargs["-l"]) # will print the value of key -l
        print(kwargs["-a"]) # will print the value of key -a
```

## Default argument values
We can set default values by passing values in the parameters section of the function. Ex.:
```python
    def my_func(arg1="1", arg2="2"):
        print(arg1, arg2)
    my_func()
```

# Return
We can return multiple values using:

`return val1, val2, val3`

It will then return a tuple.