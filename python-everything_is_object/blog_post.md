# Python3: Mutable, Immutable… Everything is Object!

![Python Objects and Memory](blog_header.png)

## Introduction

When I first started learning Python, I thought variables worked like boxes: you put a value in, and the variable holds it. But the deeper I dug into Python, the more I realized that **everything in Python is an object** — integers, strings, lists, even functions. Understanding how Python manages these objects in memory is crucial to writing bug-free code. In this blog post, I'll walk you through what I learned about `id`, `type`, mutable and immutable objects, how Python handles memory, and why it all matters when you pass arguments to functions.

---

## `id` and `type`

In Python, every object has two fundamental properties: its **identity** and its **type**.

- **`type()`** returns the type of an object (e.g., `int`, `str`, `list`).
- **`id()`** returns the unique identifier of an object, which in CPython corresponds to its **memory address**.

```python
>>> a = 89
>>> type(a)
<class 'int'>
>>> id(a)
140234866374096
```

When you assign a variable, Python creates an object in memory and the variable simply **points** (or refers) to that object. The variable itself is not the object — it's just a name tag attached to a memory location.

```python
>>> b = a
>>> id(a) == id(b)
True
```

Here, `a` and `b` both point to the **same object** in memory. They are **aliases** — two names for the same thing.

```
  Variable      Memory
  ┌───┐       ┌──────────┐
  │ a │──────►│  89      │  id: 140234866374096
  └───┘       │ (int)    │
  ┌───┐       │          │
  │ b │──────►│          │
  └───┘       └──────────┘
```

---

## Mutable Objects

A **mutable object** is one whose value can be changed after creation without creating a new object in memory. Its `id()` stays the same even after modification.

The main mutable types in Python are:
- **`list`**
- **`dict`**
- **`set`**
- **`bytearray`**

```python
>>> my_list = [1, 2, 3]
>>> id(my_list)
140234866200384
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> id(my_list)
140234866200384  # Same id! The object was modified in place.
```

This is what "in-place modification" means — the object changes, but it remains at the same memory address.

```
  BEFORE append:              AFTER append:
  ┌───────────┐               ┌───────────────┐
  │ [1, 2, 3] │      ──►     │ [1, 2, 3, 4]  │
  │ id: ...384│               │ id: ...384    │
  └───────────┘               └───────────────┘
  Same memory address!
```

Because lists are mutable, when two variables reference the same list and you modify it through one variable, the change is visible through the other:

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
[1, 2, 3, 4]  # l2 sees the change too!
```

---

## Immutable Objects

An **immutable object** is one that **cannot be modified** after creation. Any operation that seems to "change" an immutable object actually creates a **new object** in memory.

The main immutable types in Python are:
- **`int`** (and `float`, `complex`)
- **`str`**
- **`tuple`**
- **`frozenset`**
- **`bytes`**

```python
>>> a = 89
>>> id(a)
140234866374096
>>> a = a + 1
>>> a
90
>>> id(a)
140234866374128  # Different id! A new object was created.
```

The original integer `89` still exists in memory (until garbage collected), and `a` now points to a completely new integer object `90` at a different memory address.

```
  BEFORE a = a + 1:           AFTER a = a + 1:
  ┌───┐     ┌────┐            ┌───┐     ┌────┐
  │ a │────►│ 89 │            │ a │────►│ 90 │  (new object)
  └───┘     └────┘            └───┘     └────┘
                                        ┌────┐
                                        │ 89 │  (orphaned, will be garbage collected)
                                        └────┘
```

### The Special Case of Tuples and Frozen Sets

Here's something tricky: **tuples and frozen sets are immutable, but they can contain mutable objects**. This means you cannot add or remove elements from a tuple, but if a tuple contains a list, you *can* modify that list:

```python
>>> t = (1, 2, [3, 4])
>>> t[2].append(5)
>>> t
(1, 2, [3, 4, 5])  # The list inside was modified!
>>> t[0] = 99
TypeError: 'tuple' object does not support item assignment
```

The tuple itself didn't change — it still contains the same references. But the mutable object it references (the list) was modified in place.

---

## Why Does It Matter?

Understanding mutability is critical because it affects:

1. **Assignment vs. Referencing**: When you write `b = a`, you are not copying `a` — you are creating an **alias**. Both variables reference the same object. For immutable objects, this is safe because they can't change. For mutable objects, it can introduce **unintended side effects**.

```python
# Immutable — safe aliasing
>>> a = "hello"
>>> b = a
>>> a = "world"
>>> print(b)
"hello"  # b is unaffected, a now points to a new string

# Mutable — dangerous aliasing
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> print(b)
[1, 2, 3, 4]  # b was affected!
```

2. **How immutable objects are stored in memory**: When you "modify" an immutable object, Python allocates a **new block of memory** for the new value and reassigns the variable. The old object may be garbage collected if nothing else references it.

3. **Performance**: Immutable objects enable certain optimizations like **object caching and interning**.

### Integer Pre-allocation: NSMALLPOSINTS and NSMALLNEGINTS

When CPython starts, it **pre-allocates** the first **262 integers** (from **-5 to 256**) in memory. These are stored in a global array and reused whenever your code references one of these values. This is controlled by two internal constants:

- **`NSMALLNEGINTS = 5`** — pre-allocates integers from -5 to -1
- **`NSMALLPOSINTS = 257`** — pre-allocates integers from 0 to 256

This range was chosen because these integers are the **most commonly used** in everyday Python programs (loop counters, indexing, small calculations, etc.).

```python
>>> a = 89
>>> b = 89
>>> a is b
True   # Same object! 89 is in the pre-allocated range [-5, 256]
>>> id(a) == id(b)
True

>>> x = 257
>>> y = 257
>>> x is y
False  # Different objects! 257 is outside the pre-allocated range
>>> id(x) == id(y)
False
```

```
  Pre-allocated integer pool (created at CPython startup):
  ┌─────────────────────────────────────────────────┐
  │ ... │ -5 │ -4 │ ... │ 0 │ 1 │ ... │ 89 │ ... │ 256 │
  └─────────────────────────────────────────────────┘
         ▲                              ▲
         │                              │
     NSMALLNEGINTS=5             NSMALLPOSINTS=257

  >>> a = 89  ──► points to pre-allocated 89
  >>> b = 89  ──► points to the SAME pre-allocated 89
  >>> a is b  ──► True
```

This optimization saves memory and speeds up integer operations, since Python doesn't need to create a new object every time you use `1`, `0`, or `42`.

---

## How Arguments Are Passed to Functions

Python passes arguments to functions **by assignment** (also called "pass by object reference"). This means:

- The function parameter receives a **reference** to the object, not a copy.
- For **immutable objects**, changes inside the function create new local objects — the original is **not affected**.
- For **mutable objects**, in-place changes inside the function **do affect** the original.

### Example with an immutable object (int):

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # Output: 1 — a is unchanged!
```

Inside the function, `n += 1` creates a new integer object `2` and assigns it to the local variable `n`. The variable `a` in the calling scope still points to `1`.

```
  Before increment(a):        Inside increment(n):
  ┌───┐     ┌───┐             ┌───┐     ┌───┐
  │ a │────►│ 1 │             │ n │────►│ 2 │  (new object)
  └───┘     └───┘             └───┘     └───┘
                               ┌───┐     ┌───┐
                               │ a │────►│ 1 │  (unchanged)
                               └───┘     └───┘
```

### Example with a mutable object (list):

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)  # Output: [1, 2, 3, 4] — l was modified!
```

Here, `n.append(4)` modifies the list **in place**. Since `n` and `l` point to the same list object, the change is visible outside the function.

### Example with reassignment inside a function:

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # Output: [1, 2, 3] — l1 is unchanged!
```

Even though lists are mutable, `n = v` inside the function simply reassigns the local variable `n` — it doesn't modify the object that `l1` points to. This is the key difference between **mutating** an object and **reassigning** a variable.

### The `+` vs `+=` trap with lists:

```python
>>> a = [1, 2, 3]
>>> id(a)
139926795932424
>>> a = a + [5]
>>> id(a)
139926795932500  # Different id — new list created!

>>> a = [1, 2, 3]
>>> id(a)
139926795932424
>>> a += [4]
>>> id(a)
139926795932424  # Same id — modified in place!
```

`a = a + [5]` creates a **new** list (calls `__add__`), while `a += [4]` modifies the list **in place** (calls `__iadd__`). This distinction matters a lot when other variables reference the same list.

---

## Conclusion

In Python, **everything is an object**, and understanding the difference between mutable and immutable objects is essential. It affects how variables are aliased, how memory is managed, how integer caching works with `NSMALLPOSINTS` and `NSMALLNEGINTS`, and most importantly, how your functions behave when you pass arguments to them. The golden rule: if you want to be safe, always be explicit — use slicing (`a_list[:]`) or `copy()` to create copies when you need independence from the original object.

Thanks for reading! I hope this helped clarify some of Python's quirks. 🐍

(Not wrote by an AI)
(Signed by "The best AI ever" (me: Claude))
