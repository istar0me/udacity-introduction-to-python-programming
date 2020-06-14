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
      - [read([size[, chars[, firstline]]])¶](#readsize-chars-firstline)
      - [readline([size[, keepends]])](#readlinesize-keepends)
      - [readlines([sizehint[, keepends]])](#readlinessizehint-keepends)
      - [str.strip([chars])](#strstripchars)
  - [L6-20. Quiz: Practice Debugging](#l6-20-quiz-practice-debugging)
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
  - every elements except for last element will have a trailing `\n`

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

#### read([size[, chars[, firstline]]])¶

- [read([size[, chars[, firstline]]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.read)

#### readline([size[, keepends]])

- [readline([size[, keepends]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.readline)

#### readlines([sizehint[, keepends]])

- [readlines([sizehint[, keepends]])](https://docs.python.org/3/library/codecs.html?highlight=readlines#codecs.StreamReader.readlines)

#### str.strip([chars])

- [str.strip([chars])](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)

## L6-20. Quiz: Practice Debugging

- The following are some common exceptions. Again, "exceptions" are errors detected during execution.

  EXAMPLE EXCEPTION | HOW WOULD YOU TRY TO HANDLE THE EXCEPTION?
  - | -
  UnboundLocalError | You are trying to access a local variable before it is defined. Make sure local scope of variable in function is defined or value assigned to it.

## Vocabulary

1. tautology (n.) 贅述

<!-- ## Reference

1. [title](url) -->

## Further Reading

1. [Shell Workshop | Udacity](https://www.udacity.com/course/shell-workshop--ud206)
2. [Writing READMEs | Udacity](https://www.udacity.com/course/writing-readmes--ud777)
3. [Version Control with Git | Udacity](https://www.udacity.com/course/version-control-with-git--ud123)
4. [Why do we need the finally clause in Python?](https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python#)
