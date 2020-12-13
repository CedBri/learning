# Project 1: Making a calculator

## Creating the window
* Create an instance of Tk() with `window = Tk()`
    - this creates an empty window
* To start and show the window we use `window.mainloop()`
* We can change the title with `window.title()`
---
## Creating the UI
### Generating a textbox with `Entry()`
 * Specify which window owns it by passing the window instance as an argment. Ex.: `Entry(window)`.
 * We can change the size with `Entry(window, width=30)`.
 * We specify the location with with `.grid(row=0, column=0, columnspan=4)` for example.

 ### Making the buttons
 * Generate instance of Button() with `button1 = Button(window, text="1", height=3, width=3, borderwidth=1)`
 * We can once again set the locatio with `.grid()`
 * We can make the button stick to the left with `.grid(sticky="ew")`. Here "ew" means "east, west"
 
 ### Making the buttons interact
 * Accept the input of expression_field with `expression_field_value = StringVar()`
    - The value is passed from `Entry()` by adding `textvariable=expression_field_value` to the instance creation arguments
 * We get the latest value on `button_pressed` by calling 
 ```python
 expression_field_value.set(expression_field_value.get() + str(value))
 ```
* We attach the action by using `command=button_pressed()` in the instance creation of `buttonX`
* We need to import functools to return a partial function
* We then pass the argument of the number that is pressed using `when_pressed = partial(button_pressed, "X")` and change the command argument to `command=when_pressed`
* We then create the `equal_press` function. 
    - The result is stored in `result` using `eval()`
    - `eval()` will essentially read the string and evaluate it (return the answer)
    - We then update the field value using `expression_field_value.set(result)`
* Finally, we implement the clear function
    - `expression_field_value.set("")`
## Catching errors
* Try/Except
    - In our case, we will use 
    ```python
        try:
            result = eval(expression_field_value.get())
            expression_field_value.set(result)
        except ZeroDivisionError:
            expression_field_value.set()
    ```
    
# Project 1.2: Refactoring (making it clean)

## Clearing up the buttons
* We first map the buttons in a list using: 
    - We can note here that the clear and equal button won't be listed because they don't use the "when pressed" function
```python
    button_rows = [
        ["1","2","3","*"],
        ["4","5","6","-"],
        ["7","8","9","+"],
        ["0","/"]
    ]
```
* We then generate the buttons with 
```python
    for row, buttons in enumerate(button_rows): # buttons = ["1","2","3","*"]
        for col, button_value in enumerate(buttons): # button_value = "1"
            when_pressed = partial(button_pressed, button_value)
            button2 = Button(window, text=button_value, height=3, width=3, borderwidth=1, command=when_pressed)
            button2.grid(row=row+1, column=col, sticky="ew") # row+1 since row starts at 1 because of the text input
```
1. Here, we first enumerate every element of `button_rows` which will return us values like: `["1","2","3","*"]` and we assign the position of the element to `row` and the value it holds to `buttons`
2. We then enumerate the values of `buttons` and assign the position of the element to `col` and the value of it to `button_value` ("1")
3. We then change the row number so that it's not static anymore, do the same with the column and the text value
4. to fix the position of `/` we use the dynamic call `column=col if button_value != "/" else 3`

## End of project 1
