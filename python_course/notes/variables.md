# Python variables
## id()
We can use id() to check if two vars point to the same location (the same value essentially)
## is (ex.: a is b)
`is` is used to check if two vars are pointing to the same object in memory
```python
    a = 1000
    b = 1000 
    a is b -> False 
    a == b -> True
                
                
```
In this case, they both hold the same value but don't have the same location in memory so "is" returns false.
### Special cases:
- in the case where the value is between -5 and 256, `is` will return `True`. For optimisation purposes, python precompiles an array of the "most used" numbers. Every var that has a value between -5 and 256 will, instead of having it's own memory space, be pointed to the value in the pre-generated array.
```python
    a = -5
    b = -5
    a is b -> True
```
```python
    a = 256 
    b = 256
    a is b -> True
```
# Variable name conventions
- Variables cannot start with a number
```python
    var1 = 1 -> Ok
    1var = 1 -> Not ok (will throw error)
```
- Spaces will not work in var names
- Cannot be reserved Python keywords

| and      | except  | lambda   | with  |
|----------|---------|----------|-------|
| as       | finally | nonlocal | while |
| assert   | false   | None     | yield |
| break    | for     | not      |       |
| class    | from    | or       |       |
| continue | global  | pass     |       |
| def      | if      | raise    |       |
| del      | import  | return   |       |
| elif     | in      | True     |       |
| else     | is      | try      |       |

- Python **IS** case sensitive

# Global variables
## Scopes
### Local scope
The local scope is when a variable si only accessible within a function\
Local variable example:
```python
    def my_function():
        # A local scope
        a = 1
        print(f"Print a from within my_function: {a}")
```
In this case, the variable is only accessible within `my_function`
### Global scope
Global variable example:
```python
    def my_function():
        # A local scope
        global a
        a = 1
    # outside of func
    print(f"Print a from outside my_function: {a}")

```
In this case, we can print `a` without being in the function\
We can also define the variable outside of the function so that it is, by default, global.
```python
    a = 1
    def my_function():
        print(f"Print a from outside of my_function: {a})")
```
### Changing the variable
A globally defined variable can be changed localy. The change will only occur localy, when another function calls the var it will go back to it's global assignment.\
Ex:
```python
    GLOBAL_VAR = 12345

    def func_1():
        GLOBAL_VAR = 67890
        print(GLOBAL_VAR) # Will print 67890
    
    def func_2():
        print(GLOBAL_VAR) # Will print 12345
```
To change the value of a global var globally we call `global` again.\
Ex.:
```python
    GLOBAL_VAR = 12345

    def func_1():
    global GLOBAL_VAR
        GLOBAL_VAR = 67890
        print(GLOBAL_VAR) # Will print 67890
    
    def func_2():
        print(GLOBAL_VAR) # Will print 67890
```
Overall, global variables should not be used often.