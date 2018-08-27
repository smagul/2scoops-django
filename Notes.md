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
- [2 The Optimal Django Environment Setup](#2-the-optimal-django-environment-setup)
    - [2.1 Use the Same Database Engine Everywhere](#21-use-the-same-database-engine-everywhere)
        - [2.1.1 You Can’t Examine an Exact Copy of Production Data Locally](#211-you-cant-examine-an-exact-copy-of-production-data-locally)
        - [2.1.2 Different Databases Have Different Field Types/Constraints](#212-different-databases-have-different-field-typesconstraints)
        - [2.1.3 Fixtures Are Not a Magic Solution](#213-fixtures-are-not-a-magic-solution)
    - [2.2 Use Pip and Virtualenv](#22-use-pip-and-virtualenv)
        - [2.2.1 virtualenvwrapper](#221-virtualenvwrapper)
    - [2.3 Install Django and Other Dependencies via Pip](#23-install-django-and-other-dependencies-via-pip)
    - [2.4 Use a Version Control System](#24-use-a-version-control-system)
    - [2.5 Optional: Identical Environments](#25-optional-identical-environments)
        - [2.5.1 Docker](#251-docker)
    - [2.6 Summary](#26-summary)
- [3 How to Lay Out Django Projects](#3-how-to-lay-out-django-projects)
    - [3.2 Our Preferred Project Layout](#32-our-preferred-project-layout)
        - [3.2.1 Top Level: Repository Root](#321-top-level-repository-root)
        - [3.2.2 Second Level: Django Project Root](#322-second-level-django-project-root)
        - [3.2.3 Second Level: Configuration Root](#323-second-level-configuration-root)
    - [3.3 Sample Project Layout](#33-sample-project-layout)
    - [3.4 What About the Virtualenv](#34-what-about-the-virtualenv)
        - [3.4.1 Listing Current Dependencies](#341-listing-current-dependencies)
        - [3.5.1 Generating Project Boilerplate With Cookiecutter](#351-generating-project-boilerplate-with-cookiecutter)
        - [3.5.2 Generating a Starting Project With Cookiecutter Django](#352-generating-a-starting-project-with-cookiecutter-django)
    - [3.6 Summary](#36-summary)

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

# 2 The Optimal Django Environment Setup

## 2.1 Use the Same Database Engine Everywhere

A common developer pitfall is using SQLite3 for local development and PostgreSQL (or MySQL) in production. This section applies not only to the SQLite3/PostgreSQL scenario, but to any scenario where you’re using two different databases and expecting them to behave identically.  

### 2.1.1 You Can’t Examine an Exact Copy of Production Data Locally  

When your production database is different from your local development database, you can’t grab an exact copy of your production database to examine data locally.  
Sure, you can generate a SQL dump from production and import it into your local database, but that doesn’t mean that you have an exact copy after the export and import.  

### 2.1.2 Different Databases Have Different Field Types/Constraints  

Keep in mind that different databases handle typing of field data differently. Django’s ORM attempts to accommodate those differences, but there’s only so much that it can do.  

`TIP`: Django+PostgreSQL Rocks  

### 2.1.3 Fixtures Are Not a Magic Solution  

Fixtures are not a reliable tool for migrating large data sets from one database to another in a databaseagnostic way. They are simply not meant to be used that way. Don’t mistake the ability of fixtures to create basic data `(dumpdata/loaddata)` with the capability to migrate production data between database tools.  

`WARNING`: Don’t Use SQLite3 with Django in Production  

## 2.2 Use Pip and Virtualenv

**Pip** is a tool that fetches Python packages from the **Python Package Index** and its mirrors. It is used to manage and install Python packages. It’s like easy_install but has more features, the key feature being support for virtualenv.  
**Virtualenv** is a tool for creating isolated Python environments for maintaining package dependencies. It’s great for situations where you’re working on more than one project at a time, and where there are clashes between the version numbers of different libraries that your projects use.  

For example, imagine that you’re working on one project that requires Django 1.10 and another that
requires Django 1.11.  

- Without virtualenv (or an alternative tool to manage dependencies), you have to reinstall Django every time you switch projects.  
- If that sounds tedious, keep in mind that most real Django projects have at least a dozen dependencies to maintain.  

### 2.2.1 virtualenvwrapper

Virtualenvwrapper is a popular companion tool to pip and virtualenv and makes our lives easier, but it’s not an absolute necessity.

- pip install virtualenvwrapper-win
- mkvirtualenv twoscoops
- setprojectdir .
- deactivate
- workon twoscoops

## 2.3 Install Django and Other Dependencies via Pip

`TIP`: Setting PYTHONPATH  

If you have a firm grasp of the command line and environment variables, you can set your virtualenv `PYTHONPATH` so that the `django-admin.py` command can be used to serve your site and perform other tasks.
You can also set your virtualenv’s `PYTHONPATH` to include the current directory with the latest version of pip. Running `"pip install -e ."` from your project’s root directory will do the trick, installing the current directory as a package that can be edited in place.  
Additional reading:  

- <http://hope.simons-rock.edu/~pshields/cs/python/pythonpath.html>  
- <https://docs.djangoproject.com/en/1.11/ref/django-admin/>  

## 2.4 Use a Version Control System

Version control systems are also known as revision control or source control. Whenever you work on any Django project, you should use a version control system to keep track of your code changes.  
Wikipedia has a detailed comparison of different version control systems: <https://en.wikipedia.org/wiki/Comparison_of_version_control_software>  

## 2.5 Optional: Identical Environments

### 2.5.1 Docker

We can:  

- Set up identical local development environments for everyone on our project’s dev team.
- Configure these local development environments in a way similar to our staging, test, and production servers. 

The potential downsides are:

- Extra complexity that is not needed in many situations. For simpler projects where we’re not too worried about OS-level differences, it’s easier to skip this.
- On older development machines, running even lightweight containers can slow performance to a crawl. Even on newer machines, small but noticeable overhead is added. 

References for developing with Docker:

- <https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html>
- <https://realpython.com/django-development-with-docker-compose-and-machine/>
- <https://www.dockerbook.com/>

## 2.6 Summary

This chapter covered using the same database in development as in production, pip, virtualenv, and version control systems. These are good to have in your tool chest, since they are commonly used not just in Django, but in the majority of Python software development.

# 3 How to Lay Out Django Projects

`PACKAGE TIP`: Django Project Templates

- <https://github.com/pydanny/cookiecutter-django>
- <https://djangopackages.org/>

## 3.2 Our Preferred Project Layout

We rely on a modified two-tier approach that builds on what is generated by the `django-admin.py startproject` management command. Our layouts at the highest level are:  

```python
<repository_root>/
├── <configuration_root>/
├── <django_project_root>/
```

### 3.2.1 Top Level: Repository Root

The *<repository_root>* directory is the absolute root directory of the project. In addition to the *<django_project_root>* and *<configuration_root>*, we also include other critical components like the *README.md*, *docs/* directory, *manage.py*, *.gitignore*, *requirements.txt* files, and other high-level files that are required for deployment and running the project.

`TIP`: Common Practice Varies Here. Some developers like to combine the *<django_project_root>* into the *<repository_root>* of the project.

### 3.2.2 Second Level: Django Project Root

The *<django_project_root>/* directory is the root of the actual Django project. Non-configuration Python code files are inside this directory, its subdirectories, or below.  
If using `django-admin.py startproject`, you would run the command from within the repository root. The Django project that it generates would then be the project root.  

### 3.2.3 Second Level: Configuration Root

The *<configuration_root>* directory is where the settings module and base URLConf (*urls.py*) are placed. This must be a valid Python package (containing an *__init__.py* module).  
If using `django-admin.py startproject`, the configuration root is initially inside of the Django project root. It should be moved to the repository root.

## 3.3 Sample Project Layout

As you can see, in the icecreamratings_project/ directory, which is the *<repository_root>*, we have the following files and directories. We describe them in the table below:

| File or Directory | Purpose |
| ----------------- | ------- |
| *.gitignore* |Lists the files and directories that Git should ignore. (This file is different for other version control systems. For example, if you are using Mercurial instead, you’d have an .hgignore file.) |
| *config/* | The *<configuration_root>* of the project, where project-wide *settings*, *urls.py*, and *wsgi.py* modules are placed |
| *Makefile* | Contains simple deployment tasks and macros. For more complex deployments you may want to rely on tools like [Invoke](https://pypi.org/project/invoke/), [Paver](https://pypi.org/project/Paver/), or [Fabric](https://www.fabfile.org/). |
| *manage.py* | If you leave this in, don’t modify its contents. |
| *README.md and docs/* | Developer-facing project documentation. |
| *requirements.txt* | A list of Python packages required by your project, including the Django 1.11 package. |
| *icecreamratings/* | The <django_project_root> of the project. |  

Inside the icecreamratings_project/icecreamratings directory, at the *<django_project_root>*, we place the following files/directories:  

| File or Directory | Purpose |
| ----------------- | ------- |
| *media/* | For use in development only: user-generated static media assets such as photos uploaded by users. For larger projects, this will be hosted on separate static media server(s). |
| *products/* | App for managing and displaying ice cream brands. |
| *profiles/* | App for managing and displaying user profiles. |
| *ratings/* | App for managing user ratings. |
| *static/* | Non-user-generated static media assets including CSS, JavaScript, and images. For larger projects, this will be hosted on separate static media server(s). |
| *templates/* | Where you put your site-wide Django templates. |  

`TIP`: **Conventions for Static Media Directory Names.**  
In the example above, we follow the official Django documentation’s convention of using *static/* for the (non-user-generated) static media directory. If you find this confusing, there’s no harm in calling it *assets/* or *site_assets/* instead. Just remember to update your `STATICFILES_DIRS` setting appropriately.

## 3.4 What About the Virtualenv

A good place to create the virtualenv for this project would be a separate directory where you keep all of your virtualenvs for all of your Python projects. We like to put all our environments in one directory and all our projects in another.  

### 3.4.1 Listing Current Dependencies

```pip
pip freeze                      # Listing Current Dependencies
pip freeze > requirements.txt   # Saving Current Dependencies to a File
```

### 3.5.1 Generating Project Boilerplate With Cookiecutter

Here’s how Cookiecutter works:

1. First, it asks you to enter a series of values (e.g. the value for `project_name`).
2. Then it generates all your boilerplate project files based on the values you entered.

### 3.5.2 Generating a Starting Project With Cookiecutter Django

```bash
cookiecutter https://github.com/pydanny/cookiecutter-django
```

`TIP:` **What Are All the Other Files?**  
Keep in mind that Cookiecutter Django goes much further than the basic project layout components that we outlined earlier in this chapter. It’s our ultimate Django project template that we use for our projects, so it has a lot of other bells and whistles.  
It’s a lot fancier than the default `startproject` template provided by Django. We’d rather have you see our actual, real-life template that we use for our projects than a stripped-down, beginner-oriented template that we don’t use.

## 3.6 Summary

Project layout is one of those areas of Django where practices differ widely from developer to developer and group to group. What works for a small team may not work for a large team with distributed resources. Whatever layout is chosen should be documented clearly.