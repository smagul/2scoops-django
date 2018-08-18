<!-- TOC -->

- [1 Coding Style](#1-coding-style)
    - [1.1 The Importance of Making Your Code Readable](#11-the-importance-of-making-your-code-readable)
    - [1.2 PEP 8](#12-pep-8)
        - [1.2.1 The 79-Character Limit](#121-the-79-character-limit)
    - [1.3 The Word on Imports](#13-the-word-on-imports)
    - [1.4 Use Explicit Relative Imports](#14-use-explicit-relative-imports)
    - [1.5 Avoid Using Import *](#15-avoid-using-import)
        - [1.5.1 Other Python Naming Collisions](#151-other-python-naming-collisions)
    - [1.6 Django Coding Style](#16-django-coding-style)
        - [1.6.1 Consider the Django Coding Style Guidelines](#161-consider-the-django-coding-style-guidelines)
        - [1.6.2 Use Underscores in URL Pattern Names Rather Than Dashes](#162-use-underscores-in-url-pattern-names-rather-than-dashes)
    - [1.7 Choose JS, HTML, and CSS Style Guides](#17-choose-js-html-and-css-style-guides)
        - [1.7.1 JavaScript Style Guides](#171-javascript-style-guides)
        - [1.7.2 HTML and CSS Style Guides](#172-html-and-css-style-guides)
    - [1.8 Never Code to the IDE (Or Text Editor)](#18-never-code-to-the-ide-or-text-editor)

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

## 1.5 Avoid Using Import *

The reason for this is to avoid implicitly loading all of another Python module’s locals into and over our current module’s namespace, this can produce unpredictable and sometimes catastrophic results.  

### 1.5.1 Other Python Naming Collisions

You’ll run into similar problems if you try to import two things with the same name:  
[Example 1.6: Python Module Collisions](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.6.py)  
If you need to avoid a naming collision of this nature, you can always use aliases to overcome them:  
[Example 1.7: Using Aliases to Avoid Python Module Collisions](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.7.py)  

## 1.6 Django Coding Style

### 1.6.1 Consider the Django Coding Style Guidelines

[Django Coding Style](https://docs.djangoproject.com/en/1.11/internals/contributing/writing-code/coding-style/)  
`TIP`: Review the Documentation on [Django Internals](https://docs.djangoproject.com/en/1.11/internals/)  

### 1.6.2 Use Underscores in URL Pattern Names Rather Than Dashes

The wrong way, with dashes in url names:  
[Example 1.8: Bad URL Pattern Names](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.8.py)  
The right way, with underscores in url names:  
[Example 1.9: Good URL Pattern Names](https://github.com/smagul/2scoops-django/blob/master/2scoops-django/1-coding-style/ex1.9.py)  
Dashes in actual URLs are fine (e.g. `regex='^add-topping/$'`).  
Use underscores in template block names rather than dashes.

## 1.7 Choose JS, HTML, and CSS Style Guides

### 1.7.1 JavaScript Style Guides

- Standard combined JavaScript and Node.js Style Guide: <https://github.com/standard/standard>
- Principles of Writing Consistent, Idiomatic JavaScript <https://github.com/rwaldron/idiomatic.js/>
- Airbnb JavaScript Style Guide <https://github.com/airbnb/javascript>

`PACKAGE TIP`: [ESLint](https://eslint.org/): A Pluggable Linting Utility for JavaScript and JSX.  

### 1.7.2 HTML and CSS Style Guides

- Code Guide by [@mdo](https://twitter.com/mdo) for HTML and CSS: [codeguide.co](http://codeguide.co/)  
- Principles of Writing Consistent, Idiomatic CSS: <https://github.com/necolas/idiomatic-css>  
  
`PACKAGE TIP`: [stylelint](https://stylelint.io/)

## 1.8 Never Code to the IDE (Or Text Editor)

For example, introspecting template tags or discovering their source can be difficult and time consuming for developers not using a very, very limited pool of IDEs. Therefore, we follow the commonly-used naming pattern of `<app_name>_tags.py`.