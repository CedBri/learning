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