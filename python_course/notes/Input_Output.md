# Print
An empty `print()` will simply output an empty line.\
We can also print empty lines using `print("\n")`.
To convert `int` to `str` so that we can concatenate strings, we use `str()` to do the conversion.

We can also provide multiple args. Ex.: `print("my", "name", "is", "ced")` will print `my name is ced`

We can also pick the seperator using `print("my","name","is","ced", sep="_")` will print `my_name_is_ced`

We can prevent `print()` from finishing with newline by specifying `end=""`. Ex.:
```python
    print("my name is ", end="")
    # some code...
    print("ced")
    # Will print "my name is ced" instead of "my name is \n ced"
```
## Special chars
`\n` is a newline\
`\t` is a tab



# Input
## Usage
Ex.:
```python
    age = input("Please enter your age: ")
    print(f"You are {age} years old")
```
The `input()` func will pause the program until data is entered. By default the type of the input will be `str`.

# Reading from files 
## open()

With `open()` we can initialize a variable that will hold the the file object. Ex.:
```python
    my_file = open("file.txt")
    contents =  my_file.read() # to store the content of my_file
    my_file.close()
```
In this case, it is important to use `.close()` at the end otherwise the file will be kept open at runtime for the whole duration of the program.

### The prefered approach is to use `with open("file.txt") as my_file: ...`
Now python manages the file  automatically, we don't need to close it.
```python
    with open("my_file.txt") as my_file:
        content = my_file.read() # stores the content in "content"
```

# Writing to files
To write to a file, we first must specify the permissions
## Permissions
Permissions are passed as `with open("new_file.txt", "r") as new_file : ...`

Permissions:
- `r` will only let you read the file.
- `w` will overwrite the existing file ( or create a new one if it doesn't exist) and let you write to it.
- `a` to append data to an existing file.
- `x` will try to create new file, if file exists it will fail.
- `t` opens file in text mode (default)
- `b` opens file in binary mode
- `+` opens a file for updating (read and write)

We can write to the file using `.write()`

# Working dirs and paths
Python uses relative paths. The place where you run the scripts will be where it will try to file the file you're trying to open.
Just use the full path...
