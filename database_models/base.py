"""
All Classes found within the database_models directory must inherit the SQLAlchemy Declarative Base class.
Each class is SQLAlchemy ORM Class that is a representation of a database table. This declarative_base class
allows SQLAlchemy to perform actions such as relationship joining, inspection, and reflection.

The intended directory structure of the database_models directory is as follows:
 - database_models
    - base.py
    - __init__.py
    - database directory
        - __init__.py
        - python file containing one or more ORM Classes
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
