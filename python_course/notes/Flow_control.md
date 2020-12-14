# Flow Control
## If statement
The `if` statement allows for conditional code block "run".\
The `if` will only run if the condition is `True`.

## If-else
If the `if` statement condition is not met, we can run another code block by using `else`.

## If-elif-else
If we want multiple conditions to be check we use:
```python
    if condition == True:
        print("Do this")
    elif condition == False:
        print("Don't do this")
    else:
        print("???")
```

## Nested code
Nested code is simply code within code. Ex.:
```python
    if condition1:
        if condition2:
            return "both criteria met"
```
