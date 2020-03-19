# Functions

- [Functions](#functions)
  - [L5-1. Introduction](#l5-1-introduction)
  - [L5-2. Defining Functions](#l5-2-defining-functions)
    - [Defining Functions](#defining-functions)
      - [Function Header](#function-header)
      - [Function Body](#function-body)
    - [Default Arguments](#default-arguments)
  - [Vocabulary](#vocabulary)
  - [Further Reading](#further-reading)

---

## L5-1. Introduction

- Previously, we used several of Python's built-in functions
- Here, we were write functions of our own.
- Functions are useful chunks of code that allow us to encapsulate a task
  - **Encapsulation**: a way to carry out a whole series of steps with one simple command
  - ![encapsulation](img/2020-03-19-23-29-17.png)
- Functions are also used to help organize and optimize code

## L5-2. Defining Functions

### Defining Functions

```py
def cylinder_volumes(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volumes(10, 3) # function call statement
print(cylinder_volumes(10, 3))

'''
output:
282.7431
'''
```

#### Function Header

- defining functions always starts with the `def` keyword and ends with colon(`:`)
- following `def` is the name of the function `cylinder_volumes`
  - this needs one word with no gaps
  - the rules for function names are the same as those for variable names ([snake case](../L2_data_types_and_operators/README.md#snake-case))
- after the function name are parentheses that includes the arguments `height` and `radius`, separated by commas
  - **argument**: values passed in as input to a function

---

#### Function Body

- the body of function is indented after the header and is where the function does its work
  - **local variable**: can only be used within the body of its function
  - **variable scope**: determines which variables you have access to
- the body of function will often include `return` keyword, it's used to give back an output value when the function is called
- Rather than returning the value as it is calculated, an alternative technique would be to calculate the value earlier and then store it in a variable
  - before

    ```py
    return height * pi * radius ** 2
    ```

  - after

    ```py
    volume = height * pi * radius ** 2
    return volume
    ```

![function_metaphor](img/2020-03-19-23-50-40.png)

- functions like machines that take input (or arguments) and process them into ouput (or return values)

```py
return_value = print("I wish to register a complaint.")

print("Output: ", return_value)

'''
output:
I wish to register a complaint.
Output:  None
'''
```

- This is a good image but it's incomplete
  - cuz some functions like `print()` don't return anything at all
  - `print()` displays text on the output window but don't return anything
  - `None` is when a function will return by default if it doesn't explicitly return anything else
- diff between `print()` and `return`
  - `print()` provides output to the console while `return` provides the value

- It's not necessary that every function has a return statement

    ```py
    def print_greeting():
        print('Hello World!')
    ```

### Default Arguments

```py
def cylinder_volumes(height, radius = 5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volumes(10, 5))  # 785.3975
print(cylinder_volumes(10))     # 785.3975
```

- default arguments allow functions to use default values when those arguments are omitted
- it's helpful because it can make code more concise in scenarios where there's common value we can use for a variable

```py
print(cylinder_volumes(10, 7)) # 1539.3791
```

- arguments are still customizable, we are **overriding** the default value in the example below:
  - notice: we're passing values to our arguments by **position**
- there're two way to pass values
  1. by position

        ```py
        print(cylinder_volumes(10, 7)) # by position
        ```

  2. by name

        ```py
        print(cylinder_volumes(height = 10, radius = 7)) # by name

        print(cylinder_volumes(radius = 7, height = 10)) # it's also acceptable
        ```

## Vocabulary

1. cylinder (n.) 圓柱體
2. nuance (n.) 細微差別

<!-- ## Reference

1. [title](url) -->

## Further Reading

1. [B. Reserved Words](https://pentangle.net/python/handbook/node52.html)
2. [Python Scope](https://www.w3schools.com/python/python_scope.asp)
