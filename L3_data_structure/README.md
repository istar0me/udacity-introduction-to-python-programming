# Data Structure

- [Data Structure](#data-structure)
  - [L3.1 Introduction](#l31-introduction)
    - [Primitive Data Types](#primitive-data-types)
    - [Data Structure](#data-structure-1)
    - [(last two types of) operators](#last-two-types-of-operators)
  - [L3.2 Lists and Membership Operators](#l32-lists-and-membership-operators)
    - [List](#list)
      - [zero-based indexing](#zero-based-indexing)
      - [Slice and Dice with Lists](#slice-and-dice-with-lists)
    - [Membership Operators](#membership-operators)
    - [Mutability and Order](#mutability-and-order)
      - [Strings vs. Lists](#strings-vs-lists)
      - [Mutability](#mutability)
      - [Order](#order)
      - [Conclusion](#conclusion)
  - [L3.3 Quiz: Lists and Membership Operators](#l33-quiz-lists-and-membership-operators)
    - [Quiz: Slicing Lists](#quiz-slicing-lists)
  - [L3.6 List Methods](#l36-list-methods)
    - [String: Call by Value](#string-call-by-value)
    - [List: Call by Reference](#list-call-by-reference)
    - [List Methods](#list-methods)
  - [L3.8 Check for Understanding: Lists](#l38-check-for-understanding-lists)
  - [L3.9 Tuples](#l39-tuples)
    - [Tuple Unpacking](#tuple-unpacking)
  - [L3.10 Quiz: Tuples](#l310-quiz-tuples)
  - [L3.11 Sets](#l311-sets)
  - [L3.13 Dictionaries and Identity Operators](#l313-dictionaries-and-identity-operators)
    - [Dictionary](#dictionary)
    - [Identity Operators](#identity-operators)
  - [L3.14 Quiz: Dictionaries and Identity Operators](#l314-quiz-dictionaries-and-identity-operators)
    - [`get` with a Default Value](#get-with-a-default-value)
    - [Checking for Equality vs. Identity: `==` vs. `is`](#checking-for-equality-vs-identity--vs-is)
  - [Vocabulary](#vocabulary)

---

## L3.1 Introduction

### Primitive Data Types

1. int
2. float
3. boolean
4. string

### Data Structure

- group and order these data types

1. list
2. tuple
3. set
4. dictionary
5. compound data structure

### (last two types of) operators

1. membership
2. identity

## L3.2 Lists and Membership Operators

- Data Structure: containers that organize and group data types, which contain other data types and even other containers

### List

- a data type for **mutable ordered** sequences of elements

#### zero-based indexing

- index start from 0
- how far the element is from the beginning of the list
- the last element index is -1

```py
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(months[0]) # January
print(months[1]) # February
print(months[7]) # August

print(months[-1]) # December
print(months[-0]) # January

print(months[25]) # IndexError: list index out of range
```

- lists can contain any mix and match of the data types

```py
list_of_random_things = [1, 3,4, 'a string', True]
```

#### Slice and Dice with Lists

- slicing: using indices to slice off parts of an object
  - lower bound is inclusive; upper bound is **exclusive**

```py
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

q3 = month[6:9] # ['July', 'August', 'September']

first_half = month[:6] # ['January', 'February', 'March', 'April', 'May', 'June']
second_half = month[6:] # ['July', 'August', 'September', 'October', 'November', 'December']
```

- lists are most similar to strings
  - both types support `len` function, indexing, and slicing
- `len(str)` contains empty spaces

```py
greeting = "Hello there"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(len(greeting), len(months)) # 11 12
print(greeting[6:9], months[6:9]) # 'the' ['July', 'August', 'September']
```

### Membership Operators

![membership operators](img/L2&#32;16b&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;V3&#32;1-48&#32;screenshot.png)

- `in`: evaluates if object on left side is included in object on right side
- `not in`: evaluates if object on left side is not included in object on right side
- support both string and list type

```py
greeting = "Hello there"
print('her' in greeting, 'her' not in greeting)
# True False

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print('Sunday' in months, 'Sunday' not in months)
# False True
```

### Mutability and Order

#### Strings vs. Lists

| Features         | Strings              | Lists               |
| ---------------- | -------------------- | ------------------- |
| Support indexing | O                    | O                   |
| Support slicing  | O                    | O                   |
| Support `len()`  | O                    | O                   |
| Elements         | sequences of letters | any type of objects |
| Mutability       | X                    | O                   |
| Order            | O                    | O                   |

#### Mutability

![mutability_comparison](img/L2&#32;16c&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;II&#32;V4&#32;0-50&#32;screenshot.png)

- whether an object can be modified after it has been created
- lists are mutable, strings are immutable
  - ![lists_mutability](img/L2&#32;16c&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;II&#32;V4&#32;0-28&#32;screenshot.png)
  - ![string_mutability](img/L2&#32;16c&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;II&#32;V4&#32;0-33&#32;screenshot.png)

#### Order

![order](img/L2&#32;16c&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;II&#32;V4&#32;1-3&#32;screenshot.png)

- whether the order of elements in an object matters
- and whether this can be used to access elements
- both lists and strings are ordered

#### Conclusion

![mutability_order](img/L2&#32;16c&#32;Lists&#32;And&#32;Membership&#32;Operators&#32;II&#32;V4&#32;1-16&#32;screenshot.png)

- Data type selection is largely dependent on properties, and what you can easily do with it!

## L3.3 Quiz: Lists and Membership Operators

### Quiz: Slicing Lists

- Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

```py
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[:-3]) # X
print(eclipse_dates[-3:]) # O, start from index of -3
```

## L3.6 List Methods

### String: Call by Value

- due to string is immutable, so it's call by value

```py
name = "Jim"
student = name
name = "Tim"

print(name)     # Tim
print(student)  # Jim
```

### List: Call by Reference

- due to list is mutable, so it's call by reference
- ![list_call_by_reference](img/L2&#32;18a&#32;Lists&#32;Methods&#32;V2&#32;0-45&#32;screenshot.png)

### List Methods

- `len()`: how many elements in the list
- `max()`: greatest elements in the list
  - the maximum elements in the list of number is the largest number
  - the maximum elements in the list of strings is the last element when we sort alphabetically
  
  ```py
  python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']

  print(max(python_varieties)) # Reticulated Python
  ```

  - undefined for lists that contain elements form different incomparable types

  ```py
  max([42, 'African Swallow']) # TypeError: '>' not supported between instances of 'str' and 'int'
  ```

- `min()`: return the smallest elements in a list
- `sorted()`: return a copy of a list in order from smallest to largest leaving the original list unchanged

  ```py
  sizes = [15, 6, 89, 34, 65, 35]
  print(sorted(sizes)) # [6, 15, 34, 35, 65, 89]

  print(sorted(sizes, reverse=True)) # [89, 65, 35, 34, 15, 6]
  ```

- `join()`: takes a list as an argument and returns a string consisting of the list elements joined by separator string

  ```py
  nauticla_directions = "\n".join(["fore", "aft", "starboard", "port"])
  print(nauticla_directions)

  '''
  fore
  aft
  starboard
  port
  '''
  ```

- we can change the separator to `-`(hyphen)

  ```py
  names = ["Garcia", "O'Kelly", "Davis"]
  print("-",join(names)) # Garcia-O'Kelly-Davis
  ```

- Although forgetting to add comma will not trigger an error, but will give an unexpected results
  - this happens bacause of Python's default string literal appending

  ```py
  names = ["Garcia", "O'Kelly", "Davis"]
  print("-" join(names)) # GarciaO'KellyDavis
  ```

- `join()` will trigger an error, when we join anything other than string

   ```py
   stuff = ["thing", 42, "nope"]
   print(" and " .join(stuff)) # TypeError: sequence item 1: expected str instance, int found
   ```

- `append()`: add the element to the end of the lists

  ```py
  python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']

  python_varieties.append('Blood Python')

  print(python_varieties) # ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python', 'Blood Python']
  ```

## L3.8 Check for Understanding: Lists

- Q1: Which of the following statements about data types and data structures are true? Select all that apply

    | answer | option                                                                    | reason                                                                                                                                                                                               |
    | ------ | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | (O)    | Data structures are containers that can **include different data types.** | Data structures are containers that organize and group data types together in different ways. For example, some of the elements that a list can contain are integers, strings, and even other lists! |
    |        | Data structures can only hold data of the same data type.                 |                                                                                                                                                                                                      |
    | (O)    | A list is an example of a data structure.                                 |                                                                                                                                                                                                      |
    |        | All data types are data structures.                                       |                                                                                                                                                                                                      |
    | (O)    | All data structures are data types.                                       | A data type is just a type that classifies data. This can include primitive (basic) data types like integers, booleans, and strings, as well as data structures, such as lists.                      |

## L3.9 Tuples

- Tuple: data structure in Python that is an immutable ordered sequence of elements, often used to store related pieces of information

    ```py
    AngkorWat = (13.4125, 103.866667)

    print(type(AngkorWat)) # <class 'tuple'>

    print("Angkor Wat is at latitude: {}".format(AngkorWat[0])) # Angkor Wat is at latitude: 13.4125
    print("Angkor Wat is at longitude: {}".format(AngkorWat[1])) # Angkor Wat is at longitude: 103.866667
    ```

![tuple](img/L2&#32;20&#32;Tuples&#32;V4&#32;0-42&#32;screenshot.png)

- tuple is immutable, we cannot add or remove items from tuple for sort them in place
- Why do we have tuples if they're lists with fewer features?
  - Tuples are useful when we have two or more values that are so closely related

### Tuple Unpacking

```py
dimensions = 52, 40, 100
length, width, height = dimensions # tuple unpacking
print("The dimensions are {}x{}x{}".format(length, width, height)) # The dimensions are 52x40x100
```

- tuple can also be used to assign multiple variables in a compact way
- the parenthese`()` are optional when making tuple, and programmer frequently omit it if parentheses don't clarify the code.
- tuple unpacking: assign the information from a tuple into mutiple variables

---

- if we don't need to use `dimensions` directly, we can shorten the code

    ```py
    length, width, height = 52, 40, 100
    print("The dimensions are {}x{}x{}".format(length, width, height)) # The dimensions are 52x40x100
    ```

## L3.10 Quiz: Tuples

Q2.

```py
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b) # True
```

## L3.11 Sets

- Set: a data type for **mutable unordered** collections of **unique** elements
- it's useful to remove the duplicates elements

    ```py
    countries = ['angola', 'Maldives', 'India', 'United Stated', 'India', 'Denmark', 'Sweden', 'Ghana', ] # 777 more countries not displayed

    print(len(countries)) # 785
    print(countries[:5]) # ['angola', 'Maldives', 'India', 'United Stated', 'India']
    ```

- we can create set like this, `set(listName)`:

    ```py
    countries = ['angola', 'Maldives', 'India', 'United Stated', 'India', 'Denmark', 'Sweden', 'Ghana', ] # 777 more countries not displayed

    country_set = set(countries)
    print(len(country_set)) # 196
    ```

- set also support the `in`-operator the same way lists do

    ```py
    countries = ['angola', 'Maldives', 'India', 'United Stated', 'India', 'Denmark', 'Sweden', 'Ghana', ] # 777 more countries not displayed

    country_set = set(countries)

    print('India' in countries)     # True
    print('India' in country_set)   # True
    ```

- we can add elements to sets where we don't use the `append` method, we use `add` alternatively

    ```py
    countries = ['angola', 'Maldives', 'India', 'United Stated', 'India', 'Denmark', 'Sweden', 'Ghana', ] # 777 more countries not displayed

    country_set = set(countries)

    country_set.add("Italy") # Italy is added
    ```

- Set also have a `pop()` method just like lists, it will remove a random element
  - ![set_pop()](img/L2&#32;22&#32;Sets&#32;V3&#32;1-15&#32;screenshot.png)
- set is unordered, so there's no "last element"
- It also support union, intersection and difference mathematical set methods
  - it's much faster than such operators with other containers

## L3.13 Dictionaries and Identity Operators

- set is a simple data structure, they have one main use: collecting unique elements
  - dictionary is more flexible

### Dictionary

- Dictionary: a data type for **mutable** objects that store mappings of unique keys to values
  - dictionary stores pairs of elements, keys and values

  ```py
  elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
  print(elements['carbon']) # 6
  ```

- we're adding lithium and giving it a value of three

  ```py
  elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
  elements['lithium'] = 3
  print(elements) # {'hydrogen': 1, 'helium': 2, 'carbon': 6, 'lithium': 3}
  ```

- dictionary keys are similar to list indices, but dictionary can have keys of any immutable type, not just integets
  - it's **not necessary** for every key to have **the same type**
- dictionary also support `in` operator

  ```py
  elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
  print('mithril' in elements) # False
  ```

- `get()`: look up a value in a dictionary
  - it's **recommended** to use `get()` rather than `dictionary[key]`, because the later will product an error, that can crash program

  ```py
  elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
  print(elements.get('hydrogen')) # 1

  print(elements.get('delithium')) # None
  print(elements['delithium']) # KeyError: 'delithium'
  ```

### Identity Operators

![identity_operators](img/L2&#32;24&#32;Dictionaries&#32;And&#32;Identiy&#32;Operators&#32;V4&#32;2-18&#32;screenshot.png)

- we can check if a key return none with `is` operator, or the opposite `it not` operator

  ```py
  elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
  
  x = elements.get('delithium') # None
  is_null = x is None
  not_null = x is not None
  print(is_null) # True
  print(not_null) # False
  ```

## L3.14 Quiz: Dictionaries and Identity Operators

- Q2: Which of these could be used as the key for a dictionary? (Choose all that apply.) Hint: Dictionary keys must be immutable, that is, they must be of a type that is not modifiable.

    | answer | option | reason                                                                  |
    | ------ | ------ | ----------------------------------------------------------------------- |
    | (O)    | str    |                                                                         |
    |        | list   | lists can be changed by adding and removing elements, they are mutable. |
    | (O)    | int    |                                                                         |
    | (O)    | float  |                                                                         |

### `get` with a Default Value

- `get()` returns `None` (or a default value) if the key isn't found
  - In the last example, we specify the string "There's no such lement" instead of the default `None`

  ```py
  elements.get('dilithium') # None
  elements['dilithium'] # KeyError: 'dilithium'
  elements.get('kryptonite', 'There\'s no such   lement!') # "There's no such element!"
  ```

### Checking for Equality vs. Identity: `==` vs. `is`

- equality: `==`
- identity: `is`

```py
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True
print(a == c) # True
print(a is c) # False
```

expression | output | reason
- | - | -
a == b | True | List a and list b are equal(`==`) and identical(`is`)
a is b | True | as above
a == c | True | List c is equal(`==`) to a (and b) since they have same concpet
a is c | False | List b and list c are point to two different objects (i.e., they're not identical object)

## Vocabulary

1. ticker (n.) 自動收報器
2. reticulate (adj.) 網狀的
3. aft (n.) 船尾

<!-- ## Reference -->

<!-- 1. -->

<!-- ## Further Reading -->

<!-- 1. -->
