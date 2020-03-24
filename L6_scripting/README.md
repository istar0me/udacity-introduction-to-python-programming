# Scripting

<details><summary>Outline</summary>
<Dropdown Content>

- [Scripting](#scripting)
  - [L6-1. Introduction](#l6-1-introduction)
  - [L6-2. Python Installation](#l6-2-python-installation)
    - [Before We Install Python:](#before-we-install-python)
      - [1. Prepare to Use Command Line](#1-prepare-to-use-command-line)
      - [2. Is Python Already Installed On Your Computer?](#2-is-python-already-installed-on-your-computer)
  - [L6-8. Scripting with Raw Input](#l6-8-scripting-with-raw-input)
    - [`input()`: input a str](#input-input-a-str)
    - [`input()`: input a int, float](#input-input-a-int-float)
    - [`eval()`](#eval)
  - [L6-9. Quiz: Scripting with Raw Input](#l6-9-quiz-scripting-with-raw-input)
    - [Quiz: Generate Messages](#quiz-generate-messages)
  - [L6-11. Errors and Exceptions](#l6-11-errors-and-exceptions)
    - [Errors](#errors)
    - [Exceptions](#exceptions)
  - [L6-12. Quiz: Errors and Exceptions](#l6-12-quiz-errors-and-exceptions)
  - [Vocabulary](#vocabulary)
  - [Further Reading](#further-reading)

</details>

---

## L6-1. Introduction

- goal: write and run our scripts locally on our computers
- we'll learn about:
  - Python Installation and Environment Setup
  - Running and Editing Python Scripts
  - Interacting with User Input
  - Handling Exceptions
  - Reading and Writing Files
  - Importing Local, Standard, and Third-Party Modules
  - Experimenting with an Interpreter

## L6-2. Python Installation

### Before We Install Python:

#### 1. Prepare to Use Command Line

- recommend to reinforce Unix Shell commands: [Shell Workshop | Udacity](https://www.udacity.com/course/shell-workshop--ud206)

#### 2. Is Python Already Installed On Your Computer?

- In this course, we're using the most recent major version of Python - Python 3
- Mac OS X and Linux usually come with Python 2 already installed. We **DO NOT** recommend that you make any changes to this Python, since parts of the operating system are using Python
- we can type commands in terminal to check whether python is installed

  ```shell
  python --version
  ```

## L6-8. Scripting with Raw Input

### `input()`: input a str

- this is a demo with `input()`

  ```py
  name = input('Enter a name: ')
  print('Hello', name.title())
  ```

- now we input a name `alan`, it'll output the string `Hello Alan`

  ```
  $ python3 input_demo.py
  Enter a name: alan
  Hello Alan
  ```

### `input()`: input a int, float

- if we want to input a integer...

  ```py
  num = input('Enter a number: ')
  num += 20
  print(num)
  ```

- it'll show `TypeError`

  ```
  $ python3 input_demo.py
  Enter a number: 5
  Traceback (most recent call last):
    File "tempCodeRunnerFile.python", line 2, in <module>
      num += 20
  TypeError: can only concatenate str (not "int") to str
  ```

- because we need to convert type into `int` by using method `int()`

  ```py
  num = int(input('Enter a number: '))
  num += 20
  print(num)
  ```

- as long as we input a integer, the output will as our expected

  ```
  $ python3 input_demo.py
  Enter a number: 5
  25
  ```

- but if the input isn't integer, there's a `ValueError`

  ```
  $ python3 input_demo.py
  Enter a number: 4.5
  Traceback (most recent call last):
  File "tempCodeRunnerFile.python", line 1, in <module>
    num = int(input('Enter a number: '))
  ValueError: invalid literal for int() with base 10: '4.5'
  ```

- we need to convert type to `float()` just like this:

  ```py
  num = float(input('Enter a number: '))
  num += 20
  print(num)
  ```

- output:

  ```
  $ python3 input_demo.py
  Enter a number: 4.5
  24.5
  ```

---

- but what if we need an integer, like multiplying a string by it to repeat it a certain number of times?

  ```py
  num = float(input('Enter a number: '))
  print('hello' * num)
  ```

- this wouldn't work even if we input an integer nubmer

  ```
  $ python3 input_demo.py
  Enter a number: 3
  Traceback (most recent call last):
    File "tempCodeRunnerFile.python", line 2, in <module>
      print('hello' * num)
  TypeError: can't multiply sequence by non-int of type 'float'
  ```

- we can wrap `float()` within `int()` to convert to int

  ```py
  num = int(float(input('Enter a number: ')))
  print('hello' * num)
  ```

- that works

  ```
  $ python3 input_demo.py
  Enter a number: 3
  hellohellohello
  ```

- imagine and handle every possible case is important!
- we'll learn a better way to handle these scenarios in the next section

### `eval()`

- here's another way we can interpret user input
- `eval()`: a built-in function that evaluate a string as line in Python

  ```py
  x = eval(input('Enter an expression: '))
  print(x)
  ```

- output:

  ```
  $ python3 input_demo.py
  Enter an expression: 25 + 32
  57
  ```

- we can even include a variable like this:

  ```py
  num = 30
  x = eval('num + 42')
  print(x)
  ```

- output:

  ```
  $ python3 input_demo.py
  72
  ```

## L6-9. Quiz: Scripting with Raw Input

### Quiz: Generate Messages

Imagine you're a teacher who needs to send a message to each of your students reminding them of their missing assignments and grade in the class. You have each of their names, number of missing assignments, and grades on a spreadsheet and just have to insert them into placeholders in this message you came up with:

```
Hi [insert student name],

This is a reminder that you have [insert number of missing assignments] assignments left to submit before you can graduate. Your current grade is [insert current grade] and can increase to [insert potential grade] if you submit all assignments before the due date.
```

You can just copy and paste this message to each student and manually insert the appropriate values each time, but instead you're going to write a program that does this for you.

Write a script that does the following:

1. Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for `names`, `assignments`, and `grades`.
2. Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.

---

- my solution:
- file: [message.py](code/message/message.py)

  ```py
  names = input('Enter names separated by commas: ').title().split(',') # get and process input for a list of names
  assignments = input('Enter assignments count separated by commas: ').split(',') # get and process input for a list of the number of assignments
  grades = input('Enter grade separated by commas: ').split(',') # get and process input for a list of grades

  # message string to be used for each student
  # HINT: use .format() with this string in your for loop
  message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
  submit before you can graduate. You're current grade is {} and can increase \
  to {} if you submit all assignments before the due date.\n\n"

  # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
  for name, assignment, grade in zip(names, assignments, grades):
      print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
  ```

- note
  - we have to do `.title()` before `.split(',')`
    - the type of `names` is `str` before `.split(',')`, otherwise is `list`
  - `.split(',')`: separated by commas
  - `zip(names, assignments, grades)`: it's useful to use `zip()` here
  - `int(grade) + int(assignment)*2`: we should convert `assignment` to `int` at first, otherwise it will repeats the string of `assignment` two times

- input: [message.input](code/message/message.input)

  ```
  chandler bing,phoebe buffay,monica geller,ross geller
  3,6,0,2
  81,77,92,88
  ```

- output:

  ```
  $ python3 message.py < message.input
  Enter names separated by commas: Enter assignments count separated by commas: Enter grade separated by commas: Hi Chandler Bing,

  This is a reminder that you have 3 assignments left to submit before you can graduate. You're current grade is 81 and can increase to 8
  7 if you submit all assignments before the due date.


  Hi Phoebe Buffay,

  This is a reminder that you have 6 assignments left to submit before you can graduate. You're current grade is 77 and can increase to 8
  9 if you submit all assignments before the due date.


  Hi Monica Geller,

  This is a reminder that you have 0 assignments left to submit before you can graduate. You're current grade is 92 and can increase to 9
  2 if you submit all assignments before the due date.


  Hi Ross Geller,

  This is a reminder that you have 2 assignments left to submit before you can graduate. You're current grade is 88 and can increase to 92 if you submit all assignments before the due date.
  ```

- note
  - we can input from file by using `< filename`

## L6-11. Errors and Exceptions

### Errors

- **Syntax errors** occur when Python **can’t interpret** our code, since we didn’t follow the correct syntax for Python.
- These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

- file: [errors_demo.py](code/errors_and_exceptions/errors_demo.py)

  ```py
  msg = 'Welcome to this program!
  print(msg)
  ```

- output:

  ```
  $ python3 errors_demo.py
    File "tempCodeRunnerFile.python", line 1
      msg = 'Welcome to this program!
                                    ^
  SyntaxError: EOL while scanning string literal
  ```

### Exceptions

- **Exceptions** occur when unexpected things happen **during execution** of a program, even if the code is syntactically correct
- There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

- file: [exceptions_demo1.py](code/errors_and_exceptions/exceptions_demo1.py)

  ```py
  x = int(input('Enter a number: '))
  x += 20
  print(x)
  ```

- output:

  ```
  $ python3 exceptions_demo1.py
  Enter a number: ten
  Traceback (most recent call last):
    File "exceptions_demo1.py", line 1, in <module>
      x = int(input('Enter a number: '))
  ValueError: invalid literal for int() with base 10: 'ten'
  ```

  - `ValueError` occurs when a built-in operation or function is given an argument with the correct type but an inappropriate value

- file: [exceptions_demo2.py](code/errors_and_exceptions/exceptions_demo2.py)

  ```py
  print(nonexistent_variable)
  ```

- output:

  ```
    File "exceptions_demo2.py", line 1, in <module>
      print(nonexistent_variable)
  NameError: name 'nonexistent_variable' is not defined
  ```

## L6-12. Quiz: Errors and Exceptions

- Q2: Here are some of the common exceptions programmers run into in Python. Do some research online to match the appropriate description for each.

    | BUILT-IN EXCEPTION | DESCRIPTION                                                                                                   |
    | ------------------ | ------------------------------------------------------------------------------------------------------------- |
    | ValueError         | An object of the correct type but inappropriate value is passed as input to a built-in operation or function. |
    | AssertionError     | An assert statement fails.                                                                                    |
    | IndexError         | A sequence subscript is out of range.                                                                         |
    | KeyError           | A key can't be found in a dictionary.                                                                         |
    | TypeError          | An object of an unsupported type is passed as input to an operation or function.                              |

## Vocabulary

1. tautology (n.) 贅述

<!-- ## Reference

1. [title](url) -->

## Further Reading

1. [Shell Workshop | Udacity](https://www.udacity.com/course/shell-workshop--ud206)
2. [Writing READMEs | Udacity](https://www.udacity.com/
3. [Version Control with Git | Udacity](https://www.udacity.com/course/version-control-with-git--ud123)course/writing-readmes--ud777)
