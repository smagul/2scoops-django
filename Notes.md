<!-- TOC -->

- [1 Coding Style](#1-coding-style)
    - [1.1 The Importance of Making Your Code Readable](#11-the-importance-of-making-your-code-readable)
    - [1.2 PEP 8](#12-pep-8)
        - [1.2.1 The 79-Character Limit](#121-the-79-character-limit)
    - [1.3 The Word on Imports](#13-the-word-on-imports)
    - [1.4 Use Explicit Relative Imports](#14-use-explicit-relative-imports)

<!-- /TOC -->

# 1 Coding Style

## 1.1 The Importance of Making Your Code Readable

What this means is that you should go the extra mile to make your code as readable as possible:

- Avoid abbreviating variable names.  
- Write out your function argument names.  
- Document your classes and methods.  
- Comment your code.  
- Refactor repeated lines of code into reusable functions or methods.
- Keep functions and methods short. A good rule of thumb is that scrolling should not be necessary to read an entire function or method.  

## 1.2 PEP 8

**PEP 8** is the official style guide for Python.  
`WARNING`: Don’t Change an Existing Project’s Conventions  
`PACKAGE TIP`: Use Flake8 for Checking Code Quality  

### 1.2.1 The 79-Character Limit

According to PEP 8, the limit of text per line is *79 characters*. This exists because it’s a safe value that most text-wrapping editors and developer teams can accommodate without hurting the understandability of code.  
`TIP`: Django core developer Aymeric Augustin on Line Length Issues:  
Fitting the code in 79 columns is never a good reason to pick worse names for variables, functions, and classes. It’s much more important to have readable variable names than to fit in an arbitrary limit of hardware from three decades ago.  

## 1.3 The Word on Imports

The import order in a Django project is:  

1. Standard library imports.
2. Imports from core Django.
3. Imports from third-party apps including those unrelated to Django.
4. Imports from the apps that you created as part of your Django project.

## 1.4 Use Explicit Relative Imports

When writing code, it’s important to do so in such a way that it’s easier to move, rename, and version your work. In Python, explicit relative imports remove the need for hardcoding a module’s package via implicit relative imports, separating individual modules from being tightly coupled to the architecture around them.  

[Example 1.2: Bad Python Imports](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.2.py)  

Sure, your cones app works fine within your ice cream tracker project, but it has those nasty implicit relative imports that make it less portable and reusable:  

- What if you wanted to reuse your cones app in another project that tracks your general dessert consumption, but you had to change the name due to a naming conflict (e.g. a conflict with a Django app for snow cones)?  
- What if you simply wanted to change the name of the app at some point?  
  
[Example 1.3: Relative Python Imports](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.3.py)  

Table 1.1: Imports: Absolute vs. Explicit Relative vs. Implicit Relative  

| Code                             | Import Type       | Usage                                                                                 |
| -------------------------------- | ----------------- | ------------------------------------------------------------------------------------- |
| from core.views import FoodMixin | absolute import   | Use when importing from outside the current app                                       |
| from .models import WaffleCone   | explicit relative | Use when importing from another module in the current app                             |
| from models import WaffleCone    | implicit relative | Often used when importing from another module in the current app, but not a good idea |

`TIP`: [Doesn’t PEP 328 Clash With PEP 8?](https://mail.python.org/pipermail/python-dev/2010-October/104476.html)  
Additional reading: <https://www.python.org/dev/peps/pep-0008/>