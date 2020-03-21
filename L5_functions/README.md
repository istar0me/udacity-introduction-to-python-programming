# Functions

<details><summary>Outline</summary>
<Dropdown Content>

- [Functions](#functions)
  - [L5-1. Introduction](#l5-1-introduction)
  - [L5-2. Defining Functions](#l5-2-defining-functions)
    - [Defining Functions](#defining-functions)
      - [Function Header](#function-header)
        - [parameter vs. arguments](#parameter-vs-arguments)
      - [Function Body](#function-body)
    - [Default Arguments](#default-arguments)
  - [L5-6. Variable Scope](#l5-6-variable-scope)
    - [Local Variable](#local-variable)
    - [Global Variable](#global-variable)
    - [More on Variable Scope](#more-on-variable-scope)
  - [L5-7. Quiz: Variable Scope](#l5-7-quiz-variable-scope)
  - [L5-8. Solution: Variable Scope](#l5-8-solution-variable-scope)
  - [L5-9. Check For Understanding: Variable Scope](#l5-9-check-for-understanding-variable-scope)
    - [Check for Understanding](#check-for-understanding)
    - [Q1](#q1)
    - [Q3](#q3)
    - [Q4](#q4)
  - [L5-10. Documentation](#l5-10-documentation)
  - [L5-11. Quiz: Documentation](#l5-11-quiz-documentation)
    - [Quiz: Write a Docstring](#quiz-write-a-docstring)
  - [L5-13. Lambda Expressions](#l5-13-lambda-expressions)
    - [standard function vs. lambda expression](#standard-function-vs-lambda-expression)
  - [L5-14. Quiz: Lambda Expressions](#l5-14-quiz-lambda-expressions)
    - [Quiz: Lambda with Map](#quiz-lambda-with-map)
    - [Quiz: Lambda with Filter](#quiz-lambda-with-filter)
    - [doc](#doc)
      - [map(function, iterable, ...)](#mapfunction-iterable)
      - [filter(function, iterable)](#filterfunction-iterable)
  - [L5-16. Conclusion](#l5-16-conclusion)
    - [What's Next?](#whats-next)
  - [Vocabulary](#vocabulary)
  - [Reference](#reference)
  - [Further Reading](#further-reading)

</details>

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

##### parameter vs. arguments

- warning: the class doesn't clarify the differences between **(formal) parameters** and **(actual) arguments**, click [here](https://developer.mozilla.org/zh-TW/docs/Glossary/Parameter) for more details
  - A parameter is a named variable passed into a function.
  - Parameter variables are used to import arguments into functions.

```py
def cal_bmi(weight, height): # parameter = weight, height
    return weight / ((height/100)**2)

print(cal_bmi(50, 165)) # argument = 50, 165

'''
output:
18.36547291092746
'''
```

---

#### Function Body

- the body of function is indented after the header and is where the function does its work
  - **local variable**: can only be used within the body of its function
  - [**variable scope**](#l5-6-variable-scope): determines which variables you have access to
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

## L5-6. Variable Scope

- **variable scope**: the parts of program that a variable can be referenced, or used from

### Local Variable

- if a variable is created inside function, it can only be used within that function

    ```py
    def show_number():
        number = 10
        print(number) # 10

    show_number()
    print(number) # NameError: name 'number' is not defined
    ```

### Global Variable

- alternatively, we might have a variable defined outside of functions

    ```py
    number = 10

    def show_number():
        print(number) # 10

    show_number()
    print(number) # 10
    ```

- the value of a global variable can **NOT be moditfied** inside the function, see [L5-7. Quiz: Variable Scope](#l5-7-quiz-variable-scope) for the details

### More on Variable Scope

- reusing names for objects is OK as long as you keep them in separate scope
- **good practice**: define variables in the smallest scope they will be needed in

## L5-7. Quiz: Variable Scope

Read through this code snippet:

```py
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
```

What is the result of running this code? If you aren't sure, try running it on your own computer!

| answer | option                  |
| ------ | ----------------------- |
|        | `egg_count` equals zero |
|        | `egg_count` equals 12   |
| (O)    | An error occurs         |

- output:

    ```py
    UnboundLocalError: local variable 'egg_count' referenced before assignment
    ```

- reason:
  - Python doesn't allow functions to modify variables that are outside the function's scope
  - A better way would be to pass the variable as an argument and reassign it outside the function

## L5-8. Solution: Variable Scope

- If we try to **change** or **reassign** global variable inside function, we get an error
- Python doesn't allow functions to modify variables that aren't in the function's scope
- A better way to write this would be:
  - pass the variable as an argument and reassign it outside the function

    ```py
    egg_count = 0

    def buy_eggs(count):
        return count + 12 # don't modify global variable

    egg_count = buy_eggs(egg_count)
    ```

## L5-9. Check For Understanding: Variable Scope

### Check for Understanding

It is important to understand variable scope, as this often can lead to confusion when writing code that solves complex problems.

### Q1

Use the code below to determine what will print to the console.

```py
str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
```

What will happen when we run this code?

| answer | option                                                        | reason                                                |
| ------ | ------------------------------------------------------------- | ----------------------------------------------------- |
| (O)    | It will print 'Variable scope is an important concept.'       | we use the local variable rather than global variable |
|        | It will print 'Functions are important programming concepts.' |                                                       |
| (X)    | It will give a ValueError.                                    |                                                       |

### Q3

We made another tweak to the code.

```py
def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn(str1)
```

What do you think will happen when we run this code?

| answer | option                                                                            | reason |
| ------ | --------------------------------------------------------------------------------- | ------ |
| (O)    | It will give a TypeError: print_fn() takes 0 positional arguments but 1 was given |        |
| (X)    | It will print 'Variable scope is an important concept.'                           |        |
|        | It will print nothing.                                                            |        |

### Q4

We made a final tweak to the code.

```py
str1 = 'Functions are important programming concepts.'

def print_fn():
    print(str1)

print_fn(str1)
```

Now what do you think will happen?

| answer | option                                                                              | reason |
| ------ | ----------------------------------------------------------------------------------- | ------ |
| (O)    | It still gives a TypeError: print_fn() takes 0 positional arguments but 1 was given |        |
| (X)    | It will print 'Functions are important programming concepts'                        |        |
|        | It will not print anything.                                                         |        |

- conclusion: As long as the function definition did not include any parameters, call function with arguments will give an error

## L5-10. Documentation

- Documentation is used to make code easier to understand and use
- **docstrings**, or documentation strings: a type of comment used to explain the purpose of a function, and how it should be used
  - docstring is optional, however, it's a good coding practice
- single line docstrings are perfectly acceptable
  - docstrings are surrounded by triple quotes(`"""`)
  - the first line of the docstrings is a brief explanation of the function's **purpose**

  ```py
  def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
  ```

- If longer description would be appropriate for the function, we can add more information like the type and purpose of function's arguments, input and output

  ```py
  def population_density(population, land_area):
    """Calculate the population density of an area.
    INPUT:
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    OUTPUT:
    population_density: population/land_area. The population density of a particular area."
    """
    return population / land_area
  ```

- we can click [here](https://www.python.org/dev/peps/pep-0257/) to read more details about docstrings

## L5-11. Quiz: Documentation

### Quiz: Write a Docstring

Write a docstring for the `readable_timedelta` function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions [here](https://www.python.org/dev/peps/pep-0257/) and check out this [Stack Overflow page](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format) for some inspiration!

- my solution:

  ```py
  def readable_timedelta(days):
      # insert your docstring here
      """convert days into weeks and days"""

      weeks = days // 7
      remainder = days % 7
      return "{} week(s) and {} day(s)".format(weeks, remainder)
  ```

- 3 types of answer:

  ```py
  """Return a string of the number of weeks and days included in days."""
  ```

  ```py
  """Return a string of the number of weeks and days included in days.

      Args:
          days (int): number of days to convert
      """
  ```

  ```py
  """
      Return a string of the number of weeks and days included in days.

      Parameters:
      days -- number of days to convert (int)

      Returns:
      string of the number of weeks and days included in days
      """
  ```

## L5-13. Lambda Expressions

- We can use lambda expressions to create anonymous functions.
  - That is, functions that don’t have a name.
  - helpful for creating quick functions that aren’t needed later in your code.
- **higher-order functions**: functions taht take in other functions as arguments, where lambda expressions become especially useful

### standard function vs. lambda expression

```py
# standard function
def double(x):
  return x * 2

# lambda expression
double = lambda x: x * 2
```

- structure
  - `lambda` keyword: used to indicate that this is a lambda expression
  - `x`: (one or more) arguments
  - `:`
  - `x * 2`: expression that is evaluated and returned in this function
- lambda functions aren't ideal for complex function, but it's useful for short symbol functions
- add commas(`,`) to use more than 1 argument

  ```py
  lambda x, y: x * y
  ```

## L5-14. Quiz: Lambda Expressions

### Quiz: Lambda with Map

`map()` is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses `map()` to find the mean of each list in `numbers` to create the list `averages`. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the `mean` function with a lambda expression defined within the call to `map()`.

- my solution:

  ```py
  numbers = [
                [34, 63, 88, 71, 29],
                [90, 78, 51, 27, 45],
                [63, 37, 85, 46, 22],
                [51, 22, 34, 11, 18]
            ]

  # def mean(num_list):
  #     return sum(num_list) / len(num_list)
  mean = lambda num_list: sum(num_list) / len(num_list)

  averages = list(map(mean, numbers))
  print(averages)
  ```

- answer:
  - we don't need a separate `mean` variable
  - using the short variable name like `x`

  ```py
  averages = list(map(lambda x: sum(x) / len(x), numbers))
  ```

### Quiz: Lambda with Filter

`filter()` is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses `filter()` to get the names in `cities` that are fewer than 10 characters long to create the list `short_cities`. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the `is_short` function with a lambda expression defined within the call to `filter()`.

- my solution:

  ```py
  cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

  # def is_short(name):
  #     return len(name) < 10
  is_short = lambda name: len(name) < 10

  short_cities = list(filter(is_short, cities))
  print(short_cities)
  ```

- answer:
  - just like the example above, we don't need `is_short` variable
  - using the short variable name like `x`

  ```py
  short_cities = list(filter(lambda x: len(x) < 10, cities))
  ```

### doc

#### map(function, iterable, ...)

- [map(function, iterable, ...)](https://docs.python.org/3/library/functions.html#map)

#### filter(function, iterable)

- [filter(function, iterable)](https://docs.python.org/3/library/functions.html#filter)

## L5-16. Conclusion

### What's Next?

- write scripts in local environments with many functions pieced together

## Vocabulary

1. cylinder (n.) 圓柱體
2. nuance (n.) 細微差別
3. unit-agnostic (adj.) 與單位無關的
4. rationale (n.) 基本原理、邏輯根據

## Reference

1. [Parameter - MDN Web Docs Glossary: Definitions of Web-related terms | MDN](https://developer.mozilla.org/zh-TW/docs/Glossary/Parameter)

## Further Reading

1. [B. Reserved Words](https://pentangle.net/python/handbook/node52.html)
2. [Python Scope](https://www.w3schools.com/python/python_scope.asp)
3. [PEP 257 -- Docstring Conventions | Python.org](https://www.python.org/dev/peps/pep-0257/)
4. [4. Map, Filter and Reduce — Python Tips 0.1 documentation](https://book.pythontips.com/en/latest/map_filter.html)
