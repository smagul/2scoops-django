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