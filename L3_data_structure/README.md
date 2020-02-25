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

<!-- ## Vocabulary -->

<!-- 1. vocabuary (n.) 單字 -->

<!-- ## Reference -->

<!-- 1. -->

<!-- ## Further Reading -->

<!-- 1. -->
