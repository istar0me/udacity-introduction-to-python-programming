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
  - [L6-13. Handling Errors](#l6-13-handling-errors)
    - [Try Statement](#try-statement)
      - [Without Errors Handling](#without-errors-handling)
      - [With Errors Handling](#with-errors-handling)
      - [Keep running until user input a valid number](#keep-running-until-user-input-a-valid-number)
    - [Finally](#finally)
    - [Specifying Exceptions](#specifying-exceptions)
  - [L6-16. Accessing Error Messages](#l6-16-accessing-error-messages)
  - [L6-17. Reading and Writing Files](#l6-17-reading-and-writing-files)
    - [Reading a File](#reading-a-file)
    - [Writing to a File](#writing-to-a-file)
    - [Too Many Open Files](#too-many-open-files)
    - [With](#with)
  - [L6-18. Quiz: Reading and Writing Files](#l6-18-quiz-reading-and-writing-files)
    - [Calling the `read` Method with an Integer](#calling-the-read-method-with-an-integer)
    - [Reading Line by Line](#reading-line-by-line)
      - [f.readline()](#freadline)
      - [for line in file](#for-line-in-file)
      - [f.readlines()](#freadlines)
    - [Quiz: Flying Circus Cast List](#quiz-flying-circus-cast-list)
    - [doc](#doc)
      - [read([size[, chars[, firstline]]])](#readsize-chars-firstline)
      - [readline([size[, keepends]])](#readlinesize-keepends)
      - [readlines([sizehint[, keepends]])](#readlinessizehint-keepends)
      - [str.strip([chars])](#strstripchars)
  - [L6-20. Quiz: Practice Debugging](#l6-20-quiz-practice-debugging)
  - [L6-22. Importing Local Scripts](#l6-22-importing-local-scripts)
    - [Importing Local Scripts](#importing-local-scripts)
    - [Using a main block](#using-a-main-block)
    - [Example](#example)
  - [L6-23. The Standard Library](#l6-23-the-standard-library)
  - [L6-24. Quiz: The Standard Library](#l6-24-quiz-the-standard-library)
    - [Quiz: Compute an Exponent](#quiz-compute-an-exponent)
    - [Quiz: Password Generator](#quiz-password-generator)
  - [L6-26. Techniques for Importing Modules](#l6-26-techniques-for-importing-modules)
    - [Techniques for Importing Modules](#techniques-for-importing-modules)
    - [Modules, Packages, and Names](#modules-packages-and-names)
  - [L6-27. Quiz: Techniques for Importing Modules](#l6-27-quiz-techniques-for-importing-modules)
    - [Importing and accessing from modules](#importing-and-accessing-from-modules)
  - [L6-28. Third-Party Libraries](#l6-28-third-party-libraries)
    - [Third-Party Libraries](#third-party-libraries)
    - [Using a `requirements.txt` File](#using-a-requirementstxt-file)
    - [Useful Third-Party Packages](#useful-third-party-packages)
  - [L6-29. Experimenting with an Interpreter](#l6-29-experimenting-with-an-interpreter)
    - [Experimenting With An Interpreter](#experimenting-with-an-interpreter)
    - [IPython](#ipython)
  - [L6-30. Online Resources](#l6-30-online-resources)
    - [Getting the information you need to know](#getting-the-information-you-need-to-know)
    - [How to Search](#how-to-search)
    - [Hierarchy of Online Resources](#hierarchy-of-online-resources)
  - [L6-31. Practice Question](#l6-31-practice-question)
    - [Practice Question](#practice-question)
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

## L6-13. Handling Errors

### Try Statement

#### Without Errors Handling

- file: [demo1.py](code/handling_errors/demo1.py)

  ```py
  x = int(input('Enter a number: '))
  ```

- output

  ```
  $ python3 demo1.py
  Enter a number: nope
  Traceback (most recent call last):
    File "demo1.py", line 1, in <module>
      x = int(input('Enter a number: '))
  ValueError: invalid literal for int() with base 10: 'nope'
  ```

#### With Errors Handling

- file: [demo2.py](code/errors_and_exceptions/demo2.py)

  ```py
  try:
      x = int(input('Enter a number: '))
  except:
      print('That\'s not a valid number')

  print('\nAttempted Input\n')
  ```

- output

  ```
  $ python3 demo2.py
  Enter a number: nope
  That's not a valid number

  Attempted Input
  ```

#### Keep running until user input a valid number

- file: [demo3.py](code/errors_and_exceptions/demo3.py)

  ```py
  while True:
      try:
          x = int(input('Enter a number: '))
          break
      except:
          print('That\'s not a valid number!')

      print('\nAttempted Input\n')
  ```

- output

  ```
  $ python3 demo3.py
  Enter a number: ten
  That's not a valid number!

  Attempted Input

  Enter a number: hello
  That's not a valid number!

  Attempted Input

  Enter a number: 10
  ```

### Finally

- `finally`: Before Python leaves this `try` statement, it will run the code in this `finally` block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the `except` or `else` block, this `finally` block will still be executed before stopping the program.
- the `finally` block is useful for cleaning up actions in the code.
  - later in this course, we will use `finally` to close file after attempting to open in a try statement.

- file: [demo4.py](code/errors_and_exceptions/demo4.py)

  ```py
  while True:
      try:
          x = int(input('Enter a number: '))
          break
      except:
          print('That\'s not a valid number!')
      finally:
          print('\nAttempted Input\n')
  ```

- output

  ```
  $ python3 demo4.py
  Enter a number: hello
  That's not a valid number!

  Attempted Input

  Enter a number: hi
  That's not a valid number!

  Attempted Input

  Enter a number: 10

  Attempted Input

  ```

### Specifying Exceptions

- In the [demo4.py](code/errors_and_exceptions/demo4.py), if we exit the program with Ctrl + C, it doesn't stop the program
  - because the expect handle any error, including the KeyboardInterrupt error

  ```
  $ python3 demo4.py
  Enter a number: ^CThat's not a valid number!

  Attempted Input

  Enter a number: 10

  Attempted Input

  ```

- we can specify which error we want to handle

  ```py
  try:
      # some code
  except ValueError:
      # some code
  ```

  - code: [demo5.py](code/handling_errors/demo5.py)

    ```py
    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except ValueError:
            print('That\'s not a valid number!')
        finally:
            print('\nAttempted Input\n')
    ```

  - output

    ```
    $ python3 demo5.py
    Enter a number: hello
    That's not a valid number!

    Attempted Input

    Enter a number: ^C
    Attempted Input

    Traceback (most recent call last):
      File "demo5.py", line 3, in <module>
        x = int(input('Enter a number: '))
    KeyboardInterrupt
    ```

  - `KeyboardInterrupt` Error wasn't handled, so this program crashed.
  - reminder: although the program crashed, this code in the `finally` block was still executed.

- If we want this handler to address more than one type of exception, we can include a **parenthesized tuple** after the `except` with the exceptions.

  ```py
  try:
      # some code
  except (ValueError, KeyboardInterrupt):
      # some code
  ```

  - code: [demo6.py](code/handling_errors/demo6.py)

    ```py
    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except (ValueError, KeyboardInterrupt):
            print('That\'s not a valid number!')
        finally:
            print('\nAttempted Input\n')
    ```

  - output

    ```
    $ python3 demo6.py
    Enter a number: ten
    That's not a valid number!

    Attempted Input

    Enter a number: ^CThat's not a valid number!

    Attempted Input

    Enter a number: 10

    Attempted Input

    ```

- we can also execute different blocks of code depending on the exception, you can have multiple except blocks.

  ```py
  try:
      # some code
  except ValueError:
      # some code
  except KeyboardInterrupt:
      # some code
  ```

  - [demo7.py](code/handling_errors/demo7.py)

      ```py
      while True:
          try:
              x = int(input('Enter a number: '))
              break
          except ValueError:
              print('That\'s not a valid number!')
          except KeyboardInterrupt:
              print('\nNo input taken')
              break # don't forget to add break statement
          finally:
              print('\nAttempted Input\n')
      ```

  - output

    ```
    $ python3 demo7.py
    Enter a number: hello
    That's not a valid number!

    Attempted Input

    Enter a number: ^C
    No input taken

    Attempted Input

    ```

## L6-16. Accessing Error Messages

- When we handle an exception, we can still access its error message ike this:

```py
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
```

- output:

  ```
  ZeroDivisionError occurred: integer division or modulo by zero
  ```

- If we don't have specific error to handle, we can still access error message by using `except Exception:`

  ```py
  try:
      # some code
  except Exception as e:
    # some code
    print("Exception occurred: {}".format(e))
  ```

  - `Exception` is just the base class for all built-in exceptions. Learn more at [Built-in Exceptions — Python 3.8.3 documentation](https://docs.python.org/3/library/exceptions.html#Exception)

## L6-17. Reading and Writing Files

### Reading a File

```py
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
```

1. open the file using built-in method `open()`, it returns a file object.
   - there're optional parameters we can specify in Python. Here we use `r` for read only. This's the default value for the mode argument.
2. use the `read()` method to access the contents from the file object.
3. when finished with the file, don't forget to use `close()` to free up memory.

### Writing to a File

```py
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
```

1. open the file in writing(`w`) mode
   - if the file doesn't exist, python will create it for us
   - if we open an existed file, any contents contained previously will be deleted
   - if we don't want to add files without deleting contents, we should use append(`a`) mode
2. use the `write()` method to write text to a file
3. close the file when finished

### Too Many Open Files

- we shouldn't open too many files without close it.

  ```py
  files = []
  for i in range(10000):
      files.append(open('some_file.txt', 'r'))
      print(i)
  ```

- output

  ```
  ...
  5850
  5851
  5852
  Traceback (most recent call last):
    File "tempCodeRunnerFile.python", line 3, in <module>
  OSError: [Errno 23] Too many open files in system: 'some_file.txt'
  ```

### With

- Python provides a special syntax that auto-closes a file for us once we're finished using it.

  ```py
  with open('my_path/my_file.txt', 'r') as f:
      file_data = f.read()
      # we don't need to close a file manually

  print(f) # (X) we can only access the file object within 'with' scope
  print(file_data) # (O) we can still access variable outside 'with' scope
  ```

## L6-18. Quiz: Reading and Writing Files

### Calling the `read` Method with an Integer

- if we don't pass any argument to `f.read()`, this defaults to reading all the remainder of the file from its current position
- if we pass with integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.

---

- input: camelot.txt

  ```
  We're the knights of the round table
  We dance whenever we're able
  ```

- script

  ```py
  with open("camelot.txt") as song:
      print(song.read(2))
      print(song.read(8))
      print(song.read())
  ```

- output

  ```
  We
  're the 
  knights of the round table
  We dance whenever we're able
  ```

### Reading Line by Line

- `\n`s in blocks of text are newline characters.

#### f.readline()

- we can use `f.readline()` to read a single line from the file

  ```py
  with open("camelot.txt") as f:
      print(f.readline())
      print(f.readline())
  ```

- output
  - there're unnecessary new lines

  ```
  We're the knights of the round table

  We dance whenever we're able

  ```

- we can use `.strip()` to remove the unnecessary new lines

  ```py
  with open("camelot.txt") as f:
      print(f.readline().strip())
      print(f.readline().strip())
  ```

- output

  ```
  We're the knights of the round table
  We dance whenever we're able
  ```

#### for line in file

- Conveniently, Python will loop over the lines of a file using the syntax `for line in file`.

  ```py
  camelot_lines = []
  with open("camelot.txt") as f:
      for line in f:
          camelot_lines.append(line.strip())

  print(camelot_lines)
  ```

- output

  ```
  ["We're the knights of the round table", "We dance whenever we're able"]
  ```

- we use `.strip()` to remove trailing `\n` before, if we don't add `.strip()`:

  ```py
  camelot_lines = []
  with open("camelot.txt") as f:
      for line in f:
          camelot_lines.append(line)

  print(camelot_lines)
  ```

- output
  - every elements except for the last element will have a trailing `\n`

  ```
  ["We're the knights of the round table\n", "We dance whenever we're able"]
  ```

#### f.readlines()

- or we can just use `f.readlines()`

  ```py
  with open("camelot.txt") as f:
      print(f.readlines())
  ```

- output
  - every elements except for last element will have a trailing `\n`

  ```
  ["We're the knights of the round table\n", "We dance whenever we're able"]
  ```

- we can't just add `.strip()` after `readlines()`, because it returns an list

  ```py
  with open("camelot.txt") as f:
      print(f.readlines().strip())
  ```

- output

  ```
  Traceback (most recent call last):
    File "tempCodeRunnerFile.python", line 2, in <module>
      print(f.readlines().strip())
  AttributeError: 'list' object has no attribute 'strip'
  ```

### Quiz: Flying Circus Cast List

- You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.
- Write a function called `create_cast_list` that takes a filename as input and returns a list of actors' names. It will be run on the file `flying_circus_cast.txt` (this information was collected from imdb.com). Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the `.split()` [method](https://docs.python.org/3/library/stdtypes.html#str.split) to process each line.

- file: flying_circus_cast.txt

  <details><summary>click here to see the file</summary>

  <Dropdown Content>

  ```
  Graham Chapman,  Various / ... (46 episodes, 1969-1974)
  Eric Idle,  Various / ... (46 episodes, 1969-1974)
  Terry Jones,  Various / ... (46 episodes, 1969-1974)
  Michael Palin,  It's Man / ... (46 episodes, 1969-1974)
  Terry Gilliam,  Various / ... (46 episodes, 1969-1974)
  John Cleese,  Announcer / ... (40 episodes, 1969-1973)
  Carol Cleveland,  Various / ... (34 episodes, 1969-1974)
  Ian Davidson,  Algy Braithwaite / ... (8 episodes, 1969-1970)
  John Hughman,  Alfred Lord Tennyson / ... (8 episodes, 1970-1974)
  The Fred Tomlinson Singers,  Amantillado Chorus / ... (7 episodes, 1969-1973)
  Connie Booth,  Animated Mother / ... (6 episodes, 1969-1974)
  Bob Raymond,  'Dad' / ... (5 episodes, 1974)
  Lyn Ashley,  Algon Girl / ... (5 episodes, 1970-1972)
  Rita Davies,  Argument Secretary / ... (4 episodes, 1969-1972)
  Stanley Mason,  Clapper Man / ... (4 episodes, 1970-1971)
  David Ballantyne,  Ivan the Terrible / ... (3 episodes, 1970-1971)
  Donna Reading,  Girl in Bikini with Its Man / ... (3 episodes, 1969)
  Peter Brett,  Door-to-Door Martial Arts Salesman (2 episodes, 1974)
  Maureen Flanagan,  Anona Winn / ... (2 episodes, 1969-1970)
  Katya Wyeth,  Elsie / ... (2 episodes, 1969)
  Frank Lester,  The Late Professor Thynne (2 episodes, 1972-1974)
  Neil Innes,  Hesitant guitarist / ... (2 episodes, 1974)
  Dick Vosburgh,  Van der Berg (1 episode, 1969)
  Sandra Richards,  'Semprini' Girl / ... (1 episode, 1970)
  Julia Breck,  Puss In Boots / ... (1 episode, 1972)
  Nicki Howorth,  Miss Bladder (1 episode, 1972)
  Jimmy Hill,  Himself (1 episode, 1974)
  Barry Cryer,  Herman Rodrigues (1 episode, 1969)
  Jeannette Wild,  Second Secretary (1 episode, 1970)
  Marjorie Wilde,  Dear Old Lady (1 episode, 1970)
  Marie Anderson,  Girl interviewing the announcer (1 episode, 1972)
  Caron Gardner,  Mary (1 episode, 1973)
  Nosher Powell,  Jack Bodell (1 episode, 1973)
  Carolae Donoghue,  Vera's Husband's Mistress (1 episode, 1969)
  Vincent Wong,  Mr. Kamikaze (1 episode, 1970)
  Helena Clayton,  Various Roles (1 episode, 1971)
  Nigel Jones,  Various (1 episode, 1972)
  Roy Gunson, (1 episode, 1970)
  Daphne Davey,  Various Roles (1 episode, 1971)
  Stenson Falke, (1 episode, 1974)
  Alexander Curry,  Various (1 episode, 1970)
  Frank Williams,  Clerk of the Court (1 episode, 1972)
  Ralph Wood, (1 episode, 1970)
  Rosalind Bailey,  Elizabethan Girl (1 episode, 1972)
  Marion Mould, (1 episode, 1974)
  Sheila Sands,  Stripper / ... (uncredited) (2 episodes, 1969)
  Richard Baker,  Himself - BBC News Anchor (uncredited) (3 episodes, 1972-1973)
  Douglas Adams,  Dr. Emile Koning - Surgeon / ... (uncredited) (2 episodes, 1974)
  Ewa Aulin,  Harrassed Woman (uncredited) (1 episode, 1969)
  Reginald Bosanquet,  Himself (uncredited) (1 episode, 1970)
  Barbara Lindley,  Bride (uncredited) (1 episode, 1970)
  Roy Brent,  Armoured Knight (uncredited) (1 episode, 1972)
  Jonas Card,  Armoured Knight (uncredited) (1 episode, 1972)
  Tony Christopher,  Armoured Knight (uncredited) (1 episode, 1972)
  Beulah Hughes, (uncredited) (1 episode, 1972)
  Peter Kodak,  Armoured Knight (uncredited) (1 episode, 1972)
  Lulu,  Herself (uncredited) (1 episode, 1972)
  Jay Neill,  Armoured Knight (uncredited) (1 episode, 1972)
  Graham Skidmore,  Armoured Knight (uncredited) (1 episode, 1972)
  Ringo Starr,  Himself (uncredited) (1 episode, 1972)
  Fred Tomlinson,  Superintendent McGough (uncredited) (1 episode, 1972)
  David Hamilton,  Himself - Thames TV Announcer (uncredited) (1 episode, 1973)
  Suzy Mandel,  German Girl (uncredited) (1 episode, 1974)
  Peter Woods,  BBC Presenter (uncredited) (1 episode, 1974)
  ```
  </details>

- my solution:

  ```py
  def create_cast_list(filename):
      cast_list = []
      #use with to open the file filename
      #use the for loop syntax to process each line
      #and add the actor name to cast_list
      with open(filename) as f:
          for line in f:
              cast_list.append(line.split(",")[0])

      return cast_list

  cast_list = create_cast_list('flying_circus_cast.txt')
  for actor in cast_list:
      print(actor)
  ```

- answer:
  - add a new variable `name` to separate into two lines

  ```py
  def create_cast_list(filename):
      cast_list = []
      with open(filename) as f:
          for line in f:
              name = line.split(",")[0]
              cast_list.append(name)

      return cast_list

  cast_list = create_cast_list('flying_circus_cast.txt')
  for actor in cast_list:
      print(actor)
  ```

### doc

#### read([size[, chars[, firstline]]])

- [read([size[, chars[, firstline]]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.read)

#### readline([size[, keepends]])

- [readline([size[, keepends]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.readline)

#### readlines([sizehint[, keepends]])

- [readlines([sizehint[, keepends]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.readlines)

#### str.strip([chars])

- [str.strip([chars])](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)

## L6-20. Quiz: Practice Debugging

- The following are some common exceptions. Again, "exceptions" are errors detected during execution.

  | EXAMPLE EXCEPTION | HOW WOULD YOU TRY TO HANDLE THE EXCEPTION?                                                                                                        |
  | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
  | UnboundLocalError | You are trying to access a local variable before it is defined. Make sure local scope of variable in function is defined or value assigned to it. |

## L6-22. Importing Local Scripts

### Importing Local Scripts

- importing python script from other files is useful when working on a bigger project
- format: `import` followed by the name of the file, without the `.py` extension

  ```py
  import useful_functions
  ```

- Conventionally, we write `import` statement at the top of the file
- Import statement will create a module object
  - Modules are just Python files that contain definitions and statements.
  - To access objects from an imported module, you need to use dot notation

  ```py
  import useful_functions
  useful_functions.add_five([1, 2, 3, 4])
  ```

- we can add an alias by using `as` statment

  ```py
  import useful_functions as uf
  ```

### Using a main block

- Whenever we run a script like this, Python actually sets a special built-in variable called `__name__` for any module
  - When we run a script, Python recognizes this module as the main program, and sets the `__name__` variable for this module to the string `"__main__"`.
  - For any modules that are imported in this script, this built-in `__name__` variable is just set to the name of that module.
- Therefore, the condition if `__name__ == "__main__"` is just checking whether this module is the main program.

### Example

- file: [demo.py](code/import/demo.py)

  ```py
  import useful_functions as uf

  scores = [88, 92, 79, 93, 85]

  mean = uf.mean(scores)
  curved = uf.add_five(scores)

  mean_c = uf.mean(curved)

  print("Scores:", scores)
  print("Original Mean:", mean, " New Mean:", mean_c)

  print(__name__)     # __main__
  print(uf.__name__)  # useful_functions
  ```

- output

  ```
  Scores: [88, 92, 79, 93, 85]
  Original Mean: 87.4  New Mean: 92.4
  __main__
  useful_functions
  ```

- file: [useful_functions.py](code/import/useful_functions.py)

  ```py
  def mean(num_list):
      return sum(num_list) / len(num_list)


  def add_five(num_list):
      return [n + 5 for n in num_list]  # list comprehension


  def main():
      print("Testing mean function")
      n_list = [34, 44, 23, 46, 12, 24]
      correct_mean = 30.5
      assert(mean(n_list) == correct_mean)

      print("Testing add_five function")
      correct_list = [39, 49, 28, 51, 17, 29]
      assert(add_five(n_list) == correct_list)

      print("All tests passed!")


  if __name__ == '__main__':  # only execute when we run 'useful_functions.py'
      main()
  ```

- output

  ```
  Testing mean function
  Testing add_five function
  All tests passed!
  ```

## L6-23. The Standard Library

- [The Python Standard Library](https://docs.python.org/3/library/)
- we can discover new modules at the [Python Module of the Week](https://pymotw.com/3/) blog

## L6-24. Quiz: The Standard Library

### Quiz: Compute an Exponent

- It's your turn to import and use the `math` module. Use the `math` module to calculate `e` to the power of 3. `print` the answer.
- Refer to the [math module's documentation](https://docs.python.org/3.6/library/math.html?highlight=math%20module#module-math) to find the function you need!

  ```py
  import math

  # print e to the power of 3 using the math module
  print(math.exp(3))          # 20.085536923187668 (more precise)
  print(math.pow(math.e, 3))  # 20.085536923187664
  ```

### Quiz: Password Generator

- Write a function called `generate_password` that selects three random words from the list of words `word_list` and concatenates them into a single string.
- Your function should not accept any arguments and should reference the global variable `word_list` to build the password.

- file: words.txt

  <details><summary>click here to see words.txt</summary>

  <Dropdown Content>

  ```
  Alice
  was
  beginning
  to
  get
  very
  tired
  of
  sitting
  by
  her
  sister
  bank
  having
  nothing
  Once
  twice
  she
  had
  peeped
  into
  the
  book
  her
  sister
  was
  reading
  but
  it
  had
  no
  pictures
  or
  conversations
  in
  it
  and
  what
  is
  the
  use
  of
  a
  book
  thought
  Alice
  without
  pictures
  or
  conversations
  ```
  </details>

- my solution: password_generator.py

  ```py
  # Use an import statement at the top
  import random

  word_file = "words.txt"
  word_list = []

  #fill up the word_list
  with open(word_file,'r') as words:
    for line in words:
      # remove white space and make everything lowercase
      word = line.strip().lower()
      # don't include words that are too long or too short
      if 3 < len(word) < 8:
        word_list.append(word)

  # Add your function generate_password here
  # It should return a string consisting of three random words 
  # concatenated together without spaces
  def generate_password():
      password = ""
      for _ in range(0,3):
          password += random.choice(word_list)
      return password


  # test your function
  print(generate_password())
  ```

- key method:

  ```py
  random.choice(word_list)
  ```

- answer 1:

  ```py
  def generate_password():
      return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
  ```

- answer 2:
  - use the [`random.sample`](https://docs.python.org/3.6/library/random.html#random.sample) function and `.join` method for strings

  ```py
  def generate_password():
      return ''.join(random.sample(word_list,3))
  ```

## L6-26. Techniques for Importing Modules

### Techniques for Importing Modules

- There are other variants of import statements that are useful in different situations.

1. To import an individual function or class from a module:

  ```py
  from module_name import object_name
  ```

2. To import multiple individual objects from a module:

  ```py
  from module_name import first_object, second_object
  ```

3. To rename a module:

  ```py
  import module_name as new_name
  ```

4. To import an object from a module and rename it:

  ```py
  from module_name import object_name as new_name
  ```

5. To import every object individually from a module (**DO NOT DO THIS**):

  ```py
  from module_name import *
  ```

6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.

  ```py
  import module_name
  ```

### Modules, Packages, and Names

- In order to manage code better, module is split down into sub-modules
- A **package** is simply a module that contains sub-modules
- We can only import sub-modules, not functions

  ```py
  import package_name.submodule_name
  # import os.path
  ```

- when the name of module and class are identical, the name will represent the class

  ```py
  >>> from datetime import datetime
  >>> print(datetime)
  <class 'datetime.datetime'>
  ```

## L6-27. Quiz: Techniques for Importing Modules

### Importing and accessing from modules

- In this quiz, you'll be using different methods to import and use the `random.randint()` function from the `random` module. Your task is to match the `import` statement with the way you would then call the function itself.

- Match the import statement with the way that `random.randint()` is called

  | IMPORT STATEMENT                     | CALLING THE FUNCTION             |
  | ------------------------------------ | -------------------------------- |
  | `import random`                      | `random.randint(0, 10)`          |
  | `from random import randint`         | `randint(0, 10)`                 |
  | `import random as rd`                | `rd.randint(0, 10)`              |
  | `from random import randint as rint` | `rint(0, 10)`                    |
  | `from random import *`               | **Don't use this import statement!** |

## L6-28. Third-Party Libraries

### Third-Party Libraries

- **pip**: package manager that is included in Python 3
- One popular alternative is **Anaconda** which is designed specifically for data science.
- pip install sytax: 

  ```py
  pip install package_name
  ```

### Using a `requirements.txt` File

- we used to list all the dependencies in a file called `requirements.txt`, make it easier to share
- this's an example of `requirements.txt`:
  - there're 2 equal sign(`=`), not 1
  - version number is optional, but it usually should be included

  ```
  beautifulsoup4==4.5.1
  bs4==0.0.1
  pytz==2016.7
  requests==2.11.1
  ```

- we can use pip to install all dependencies from `requirements.txt` at once:
  - `r` for requirement

  ```
  pip install -r requirements.txt
  ```

### Useful Third-Party Packages

- [IPython](https://ipython.org/) - A better interactive Python interpreter
- [requests](http://docs.python-requests.org/) - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- [Flask](http://flask.pocoo.org/) - a lightweight framework for making web applications and APIs.
- [Django](https://www.djangoproject.com/) - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Used to parse HTML and extract information from it. Great for web scraping.
- [pytest](http://doc.pytest.org/) - extends Python's builtin assertions and unittest module.
- [PyYAML](http://pyyaml.org/wiki/PyYAML) - For reading and writing [YAML](https://en.wikipedia.org/wiki/YAML) files.
- [NumPy](http://www.numpy.org/) - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
- [pandas](http://pandas.pydata.org/) - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
- [matplotlib](http://matplotlib.org/) - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
- [ggplot](http://ggplot.yhathq.com/) - Another 2D plotting library, based on R's ggplot2 library.
- [Pillow](https://python-pillow.org/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [pyglet](http://www.pyglet.org/) - A cross-platform application framework intended for game development.
- [Pygame](http://www.pygame.org/) - A set of Python modules designed for writing games.
- [pytz](http://pytz.sourceforge.net/) - World Timezone Definitions for Python

## L6-29. Experimenting with an Interpreter

### Experimenting With An Interpreter

- type `python` or `python3` in terminal will start a python interactive interpreter
  - `python` for v2.x, `python3` for v3.x
  - it's an awesome place to experiment and try bits of python code
- the value of the last line in a prompt will be outputted automatically
  - if having multiple lines, we still have to use `print()`

  ```py
  >>> type(5.23)
  <class 'float'>
  ```

- if we define a function, we will see a change at the left side(`...`), meaning continuation lines
  - we have to include our own indentation

  ```py
  >>> def cylinder_volume(height, radius):
  ...         pi = 3.14159
  ...         return height * pi * radius ** 2
  ```

- A drawback of using interpreter is hard to edit code, we have to move cursor only by using keyboard, not mouse
- to quit the Python interpreter
  - type `exit()` or hit `Ctrl + D` on macOS or Linux
  - type `exit()` or hit `Ctrl + Z` then `Enter` on Windows

### IPython

- It's an awesome alternative for default Python interpreter
- It comes with many handy features:
  - tab completion
  - `?` for details about an object
  - `!` to execute system shell commands
  - syntax highlighting
  - and [more](https://ipython.org/ipython-doc/3/interactive/tutorial.html)

## L6-30. Online Resources

### Getting the information you need to know

- (X) carry an encyclopedia's worth of knowledge in their heads
- (O) finding information quickly

### How to Search

1. using `python` or the name of the library
2. writing good search query can take multiple attempts, try again
3. try using keywords found on the page we found
4. copy and paste error messages, remove the unnecessary parts (e.g. line numbers that has error)
5. ask it ourself! Community like [stackoverflow](https://stackoverflow.com/) is a great place, but there's a etiquitte rules we have to follow

### Hierarchy of Online Resources

- While there are many online resources about programming, not all of the them are created equal. This list of resources is in approximate order of reliability.

  1. [The Python Tutorial](https://docs.python.org/3/tutorial/) - This section of the official documentation surveys Python's syntax and standard library. It uses examples, and is written using less technical language than the main documentation. Make sure you're reading the Python 3 version of the docs!
  2. [The Python Language and Library References](https://docs.python.org/3/index.html) - The Language Reference and Library Reference are more technical than the tutorial, but they are the definitive sources of truth. As you become increasingly acquainted with Python you should use these resources more and more.
  3. Third-Party Library Documentation - Third-party libraries publish their documentation on their own websites, and often times at <https://readthedocs.org/>. You can judge the quality of a third-party library by the quality of its documentation. If the developers haven't found time to write good docs, they probably haven't found the time to polish their library either.
  4. The websites and blogs of prominent experts - The previous resources are primary sources, meaning that they are documentation from the same people who wrote the code being documented. Primary sources are the most reliable. Secondary sources are also extremely valuable. The difficulty with secondary sources is determining the credibility of the source. The websites of authors like [Doug Hellmann](https://doughellmann.com/blog/) and developers like [Eli Bendersky](http://eli.thegreenplace.net/) are excellent. The blog of an unknown author might be excellent, or it might be rubbish.
  5. [StackOverflow](http://stackoverflow.com/) - This question and answer site has a good amount of traffic, so it's likely that someone has asked (and someone has answered) a related question before! However, answers are provided by volunteers and vary in quality. **Always understand solutions before putting them into your program. One line answers without any explanation are dubious.** This is a good place to find out more about your question or discover alternative search terms.
  6. Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that no one has addressed it on StackOverflow. You might find a reference to your error in a bug report on GitHub for instance. These bug reports can be helpful, but you'll probably have to do some original engineering work to solve the problem.
  7. Random Web Forums - Sometimes your search yields references to forums that haven't been active since 2004, or some similarly ancient time. If these are the only resources that address your problem, you should rethink how you're approaching your solution.

## L6-31. Practice Question

### Practice Question

- For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

- Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

- Sample Output:

  ```
  >>> Enter your First [space] Last name only: Bill Newman
  >>> Unique flower name with the first letter: Bellflower
  ```

- file: flowers.txt

  <details><summary>click here to see flowers.txt</summary>

  <Dropdown Content>

  ```
  A: African Daisy
  B: Bellflower
  C: Coral Bells
  D: Desert Rose
  E: English Bluebell
  F: Forget Me Not
  G: Goldenrod
  H: Heliotrope
  I: Impatiens
  J: Jamesia americana
  K: Kangaroo Paw
  L: Lily of the Valley
  M: Monks Hood
  N: Nemophila
  O: Ox Eye Daisy
  P: Peace Lily
  Q: Quaker Ladies
  R: Rain Lily
  S: Snapdragon
  T: Trumpet Vine
  U: Urn Plant
  V: Viola wittrockiana
  W: Whirling Butterflies
  X: Xanthoceras sorbifolium
  Y: Yellow Archangel
  Z: Zinnia elegans
  ```
  </details>

- my solution: python match_flower_name.py
  - lower the key of flowers.txt by using `str.lower()` method
  - remove the `\n` at the end by using `.strip()` method

  ```py
  # Write your code here

  # HINT: create a dictionary from flowers.txt
  flowers = dict()
  with open('flowers.txt') as f:
      for line in f:
          (key, value) = line.strip().split(': ')
          flowers[key.lower()] = value

  # HINT: create a function to ask for user's first and last name
  name = input('Enter your First [space] Last name only: ')
  firstLetter = name[0].lower()

  # print the desired output
  print('Unique flower name with the first letter: {}'.format(flowers[firstLetter]))
  ```

- output

  ```
  Enter your First [space] Last name only: Bill Newman
  Unique flower name with the first letter: Bellflower
  ```

- answer:
  - declare a function called `create_flowerdict()`
  - take filename as an parameter of `create_flowerdict()`

  ```py
  # function that creates a flower_dictionary from filename
  def create_flowerdict(filename):
      flower_dict = {}
      with open(filename) as f:
          for line in f:
              letter = line.split(": ")[0].lower()
              flower = line.split(": ")[1].strip()
              flower_dict[letter] = flower
      return flower_dict

  # Main function that prompts for user input, parses out the first letter
  # includes function call for create_flowerdict to create dictionary
  def main(): 
      flower_d = create_flowerdict('flowers.txt')
      full_name = input("Enter your First [space] Last name only: ")
      first_name = full_name[0].lower()
      first_letter = first_name[0]
  # print command that prints final input with value from corresponding key in dictionary
      print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

  main()
  ```

## Vocabulary

1. tautology (n.) 贅述
2. burgeoning (adj.) 迅速發展的
3. myriad (adj.) 無數的
4. keep abreast with (phr.) 跟上；不落後於
5. definitive (adj.) 最權威的
6. dubious (adj.) 可疑的

<!-- ## Reference

1. [title](url) -->

## Further Reading

1. [Shell Workshop | Udacity](https://www.udacity.com/course/shell-workshop--ud206)
2. [Writing READMEs | Udacity](https://www.udacity.com/course/writing-readmes--ud777)
3. [Version Control with Git | Udacity](https://www.udacity.com/course/version-control-with-git--ud123)
4. [Why do we need the finally clause in Python?](https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python#)
5. [Python | assert keyword - GeeksforGeeks](https://www.geeksforgeeks.org/python-assert-keyword/)
