# Control Flow

<details><summary>Outline</summary>

<Dropdown Content>

- [Control Flow](#control-flow)
  - [L4-1. Introduction](#l4-1-introduction)
  - [L4-2. Conditional Statements](#l4-2-conditional-statements)
    - [if](#if)
    - [if...else...](#ifelse)
    - [elif](#elif)
    - [`=` vs. `==`](#vs)
    - [Indentation](#indentation)
      - [Spaces or Tabs?](#spaces-or-tabs)
  - [L4-7. Boolean Expressions for Conditions](#l4-7-boolean-expressions-for-conditions)
    - [Complex Boolean Expressions](#complex-boolean-expressions)
    - [Good and Bad Examples](#good-and-bad-examples)
      - [1. Don't use True or False as conditions](#1-dont-use-true-or-false-as-conditions)
      - [2. Be careful writing expressions that use logical operators](#2-be-careful-writing-expressions-that-use-logical-operators)
      - [3. Don't compare a boolean variable with == True or == False](#3-dont-compare-a-boolean-variable-with--true-or--false)
    - [Truth Value Testing](#truth-value-testing)
  - [L4-10. For Loops](#l4-10-for-loops)
    - [For Loops](#for-loops)
    - [Using the `range()` Function with `for` Loops](#using-the-range-function-with-for-loops)
    - [Creating and Modifying Lists](#creating-and-modifying-lists)
  - [L4-13. Quiz: For Loops](#l4-13-quiz-for-loops)
    - [doc](#doc)
      - [str.replace(old, new[, count])](#strreplaceold-new-count)
    - [Quiz: Tag Counter](#quiz-tag-counter)
    - [doc](#doc-1)
      - [str.startswith(prefix[, start[, end]])](#strstartswithprefix-start-end)
      - [str.endswith(suffix[, start[, end]])](#strendswithsuffix-start-end)
  - [L4-15. Quiz: Match Inputs To Outputs](#l4-15-quiz-match-inputs-to-outputs)
  - [L4-16. Building Dictionaries](#l4-16-building-dictionaries)
    - [Method 1: Using a `for` loop to create a set of counters](#method-1-using-a-for-loop-to-create-a-set-of-counters)
  - [L4-17. Iterating Through Dictionaries with For Loops](#l4-17-iterating-through-dictionaries-with-for-loops)
    - [Iterating Through Dictionaries with `For` Loops](#iterating-through-dictionaries-with-for-loops)
  - [L4-20. While Loops](#l4-20-while-loops)
    - [`While` Loops](#while-loops)
    - [doc](#doc-2)
      - [sum(iterable, /, start=0)](#sumiterable--start0)
  - [L4-21. Practice: While Loops](#l4-21-practice-while-loops)
    - [Practice: Factorials with While Loops](#practice-factorials-with-while-loops)
    - [Practice: Factorials with For Loops](#practice-factorials-with-for-loops)
  - [Vocabulary](#vocabulary)

</details>

---

## L4-1. Introduction

![introduction](img/2020-03-14-01-17-32.png)

- Control flow: the sequence in which your code is run.
- we'll learn about several tools in Python:
  - Conditional Statements
  - Boolean Expressions
  - For and While Loops
  - Break and Continue
  - Zip and Enumerate
  - List Comprehensions

## L4-2. Conditional Statements

### if

![if-1](img/2020-03-14-01-23-15.png)
![if-2](img/2020-03-14-01-23-25.png)

### if...else...

![else](img/2020-03-14-01-25-24.png)

### elif

![elif](img/2020-03-14-01-29-15.png)

- if we have more than two possible cases, we can use eilf
- `elif` short for `else if`

### `=` vs. `==`

![`=` vs. `==`](img/2020-03-14-01-29-53.png)

- `=`: assign operator
- `==`: comparison operator

### Indentation

- Unlike other programming language using braces to enclose block of code
- In python, we use indentation to enclose block of code.
- This indentation conventionally comes in multiples of four spaces.
- It's important to be strict about following this convention.

#### Spaces or Tabs?

- The [Python Style Guide](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces) recommends using 4 spaces to indent, rather than using a tab.
- Whichever you use, be aware that "**Python 3 disallows mixing the use of tabs and spaces for indentation.**"

## L4-7. Boolean Expressions for Conditions

### Complex Boolean Expressions

```py
if 18.5 <= weight / height**2 < 25: # height ** 2 compute first
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
```

- For really complicated conditions you might need to combine some `and`s, `or`s and `not`s together.
- Use parentheses if you need to make the combinations clear.

### Good and Bad Examples

![good_and_bad_examples](img/2020-03-14-02-06-05.png)

#### 1. Don't use True or False as conditions

- it's useless to use any condition that you know will always evaluate to True or False

    ```py
    # Bad example
    if True:
        print("This indented code will always get run.")

    # Another bad example
    if is_cold or not is_cold:
        print("This indented code will always get run.")
    ```

#### 2. Be careful writing expressions that use logical operators

- Logical operators `and`, `or` and `not` have specific meanings that aren't quite the same as their meanings in plain English.

    ```py
    # Bad example
    if weather == "snow" or "rain":
        print("Wear boots!")

    # Good example
    if weather == "snow" or weather == "rain":
        print("Wear boots!")
    ```

![be_careful_writing_expressions_that_use_logical_operators](img/2020-03-14-02-11-57.png)

- [Later](#truth-value-testing) we'll discuss what happens when we use non-boolean-type objects in place of booleans.

    ```py
    if "rain": # evaluate result is True
        print("Wear boots!") # Wear boots!
    ```

#### 3. Don't compare a boolean variable with == True or == False

- This comparison isn’t necessary, since the boolean variable itself is a boolean expression.

    ```py
    # Bad example
    if is_cold == True:
        print("The weather is cold!")

    # Good example, discard unnecessary words
    if is_cold:
        print("The weather is cold!")
    ```

- If you want to check whether a boolean is **False**, you can use the `not` operator.

    ```py
    # Bad example
    if is_hot == False:
        print("The weather is cold!")

    # Good example, use "not" operator
    if not is_hot:
        print("The weather is cold!")
    ```

### Truth Value Testing

- By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

![truth_value_testing](img/2020-03-14-02-52-27.png)

- Here are most of the built-in objects that are considered False in Python:
  - constants defined to be false: `None` and `False`
  - zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
  - empty sequences and collections: `'""`, `()`, `[]`, `{}`, `set()`, `range(0)`

- example:

    ```py
    errors = 3
    if errors:
        print("You have {} errors to fix!".format(errors))
    else:
        print("No errors to fix!")

    # Output: You have 3 errors to fix!
    ```

## L4-10. For Loops

### For Loops

- A `for` loop is used to "iterate", or do something repeatedly, over an iterable.
- An iterable is an object that can return one of its elements at a time.
  - This can include sequence types, such as **strings**, **lists**, and **tuples**, as well as non-sequence types, such as **dictionaries** and **files**.
- common pattern: the name of list cities is the plural form of city

```py
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())
print("Done!")

'''
output:
New York City
Mountain View
Chicago
Los Angeles
Done!
'''
```

### Using the `range()` Function with `for` Loops

- `range()` is a built-in function used to create an iterable sequence of numbers.
- `range(start=0, stop, step=1)`

```py
print(range(4))                 # range(0, 4)
print(list(range(4)))           # [0, 1, 2, 3]
print(list(range(2, 6)))        # [2, 3, 4, 5]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]
```

- we adopt range in a list before printing it, because printing just the output of range only shows you a range object

### Creating and Modifying Lists

- we can create a list by appending to a new list at each iteration

    ```py
    # Creating a new list
    cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
    capitalized_cities = []

    for city in cities:
        capitalized_cities.append(city.title())
    ```

- Modifying a list is a bit more involved, and requires the use of the `range()` function.
  - **don't forget to add `range()`**

    ```py
    cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

    for index in range(len(cities)):
        cities[index] = cities[index].title()
    ```

## L4-13. Quiz: For Loops

```py
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    newName = name.replace(" ", "_").lower()
    usernames.append(newName)

print(usernames)

'''
output:
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
'''
```

### doc

#### str.replace(old, new[, count])

- [str.replace(old, new[, count])](https://docs.python.org/3/library/stdtypes.html#str.replace)

---

- Q2: Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?

```py
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)
```

| answer | option                                                                                  | reason                                                                                                                                                |
| ------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|        | Modifies the `names` list so that each name is lowercase and separated by underscores   |                                                                                                                                                       |
| (X)    | Causes a runtime error                                                                  |                                                                                                                                                       |
| (O)    | The printed output for the `names` list will look exactly like it did in the first line | It doesn't modify the contents of the `names` list at all. To modify the list you must operate on the list itself, using `range`, as you saw earlier. |
|        | Deletes the list                                                                        |                                                                                                                                                       |

### Quiz: Tag Counter

Write a `for` loop that iterates over a list of strings, `tokens`, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an [XML tag](https://en.wikipedia.org/wiki/XML) if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable `count`.

You can assume that the list of strings will not contain empty strings.

```py
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if (token.startswith('<') and token.endswith('>')):
        count += 1

print(count) # 2
```

- if we don't want to use `str.startswith()` and `str.endswith` method, we can use the method 2.

    ```py
    method 1:
    if (token.startswith('<') and token.endswith('>')):

    method 2:
    if token[0] == '<' and token[-1] == '>':
    ```

### doc

#### str.startswith(prefix[, start[, end]])

- [str.startswith(prefix[, start[, end]])](https://docs.python.org/3/library/stdtypes.html#str.startswith)

#### str.endswith(suffix[, start[, end]])

- [str.endswith(suffix[, start[, end]])](https://docs.python.org/3/library/stdtypes.html#str.endswith)

## L4-15. Quiz: Match Inputs To Outputs

- `range()` from zero to negative number contains nothing

```py
print(list(range(0, -5)))       # []
print(list(range(0, -5, -1)))   # [0, -1, -2, -3, -4]
```

## L4-16. Building Dictionaries

- we have the same `book_title` and `word_counter` in two methods

```py
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
```

### Method 1: Using a `for` loop to create a set of counters

```py
for word in book_title:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)

'''
output:
{'great': 2, 'holmes': 1, 'hamlet': 1, 'huckleberry': 1, 'sherlock': 1, 'adventures': 2, 'gasby': 1, 'expectations': 1, 'fin': 1, 'the': 2, 'of': 2}
'''
```

- Method 2: Using the `get` method
  - `word_counter.get(word, 0)`: when there's no word in `word_counter`, the default value is 0

```py
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)

'''
output:
{'great': 2, 'holmes': 1, 'hamlet': 1, 'huckleberry': 1, 'sherlock': 1, 'adventures': 2, 'gasby': 1, 'expectations': 1, 'fin': 1, 'the': 2, 'of': 2}
'''
```

## L4-17. Iterating Through Dictionaries with For Loops

### Iterating Through Dictionaries with `For` Loops

- the dictionary `cast` contains these keys and values

```py
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
```

- Iterating through it in the usual way with a `for` loop would give you just the keys

```py
for key in cast:
    print(key)

'''
output:
Jerry Seinfeld
Julia Louis-Dreyfus
Jason Alexander
Michael Richards
'''
```

- If we wish to iterate through both keys and values, we can use the built-in method `items` like this:

```py
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

'''
output:
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
'''
```

- `items` is an awesome method that returns tuples of key, value pairs

```py
print(cast.items())

'''
output:
dict_items([('Jerry Seinfeld', 'Jerry Seinfeld'), ('Julia Louis-Dreyfus', 'Elaine Benes'), ('Jason Alexander', 'George Costanza'), ('Michael Richards', 'Cosmo Kramer')])
'''
```

## L4-20. While Loops

### `While` Loops

- `For` loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times.
- "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a `while` loop.

```py
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
    print(sum(hand))

print(hand)

'''
output:
10
18
[10, 8]
'''
```

- The indented body of the loop should modify at least one variable in the test condition.
  - If the value of the test condition never changes, the result is an infinite loop!

### doc

#### sum(iterable, /, start=0)

- [sum(iterable, /, start=0)](https://docs.python.org/3/library/functions.html#sum)

## L4-21. Practice: While Loops

### Practice: Factorials with While Loops

```py
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while (current <= number):
    # multiply the product so far by the current number
    product *= current

    # increment current with each iteration until it reaches number
    current += 1



# print the factorial of number
print(product) # 720
```

### Practice: Factorials with For Loops

```py
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
# for i in range(1, number): # (X) exit at number 6-1
# for i in range(1, number+1): # (△) exit at number 6
for i in range(2, number+1): # (O) there's no need to mutiple by 1
    product *= i


# print the factorial of number
print(product) # 720
```

## Vocabulary

1. pay-as-you-go(PAYG) (n.) 現收現付
2. concession ticket (n.) 優惠票
3. succinct (adj.) 簡潔的
4. blackjack dealer (n.) 賭場發牌手

<!-- ## Reference

1. [title](url) -->
