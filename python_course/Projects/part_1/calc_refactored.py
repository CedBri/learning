from tkinter import Tk, StringVar, Entry, Button
from functools import partial

def button_pressed(value):
    # update the value
    expression_field_value.set(expression_field_value.get() + str(value))

def equal_pressed():
    try:
        result = eval(expression_field_value.get())
        expression_field_value.set(result)
    except ZeroDivisionError:
        expression_field_value.set("Divison by zero error")

def clear_pressed():
    expression_field_value.set("")

if __name__ == "__main__":
    window = Tk()
    window.title("My Calculator")

    # Make the entry region
    expression_field_value = StringVar()
    expression_field = Entry(window, width=30, textvariable=expression_field_value)
    # specify the location
    expression_field.grid(row=0, column=0, columnspan=4, sticky="ew")

    # to pass argument we use partial
    when_pressed = partial(button_pressed, "1")
    # mapping the buttons
    button_rows = [
        ["1","2","3","*"],
        ["4","5","6","-"],
        ["7","8","9","+"],
        ["0","/"]
    ]

    #Creating the buttons
    for row, buttons in enumerate(button_rows): # buttons = ["1","2","3","*"]
        for col, button_value in enumerate(buttons): # button_value = "1"
            when_pressed = partial(button_pressed, button_value)
            button2 = Button(window, text=button_value, height=3, width=3, borderwidth=1, command=when_pressed)
            button2.grid(row=row+1, column=col if button_value != "/" else 3, sticky="ew")

   
   
    equal = Button(window, text="=", height=3, width=3, borderwidth=1, command=equal_pressed)
    equal.grid(row=4, column=1, sticky="ew")

    clear = Button(window, text="C", height=3, width=3, borderwidth=1, command=clear_pressed)
    clear.grid(row=4, column=2, sticky="ew")


    window.mainloop()
