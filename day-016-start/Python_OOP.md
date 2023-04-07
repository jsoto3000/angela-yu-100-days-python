# Angela Yu - Python Day 16
## Object Oriented Programming

- Procedural Programming
  - A programming paradigm, derived from imperative programming.
  - Based on the concept of the procedure call. 
  - Procedures (a type of routine or subroutine) simply contain a series of computational steps to be carried out. 
  - Any given procedure might be called at any point during a program's execution, including by other procedures or itself.  
  - Computer works from top to bottom, jumping out to a function as needed.


- Object Oriented Programming (OOP)
  - A programming paradigm based on the concept of "objects", which can contain data and code. 
  - The data is in the form of fields (often known as attributes or properties)
  - The code is in the form of procedures (often known as methods).  
  - A common feature of objects is that procedures (or methods) are attached to them and can access and modify the object's data fields. 
    - In this brand of OOP, there is usually a special name such as this or self used to refer to the current object. 
  - Computer programs are designed by making them out of objects that interact with one another.
  - OOP languages are diverse, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types.  
  - Essentially get object and call it's associated methods, don't have to worry about implementation of the functions.
  - Can work with multiple objects trusting them to manage data and perform their associated functionality.


- OOP in Dynamic Languages 
  - In recent years, object-oriented programming has become especially popular in dynamic programming languages.  
  - Some dynamic languages built on OOP principles:
    - Python
    - PowerShell
    - Ruby
    - Groovy  
  - Also,Perl and PHP have been adding object-oriented features since Perl 5 and PHP 4, and ColdFusion since version 6. 
  - The Document Object Model of HTML, XHTML, and XML documents on the Internet has bindings to the popular JavaScript/ECMAScript language.  
  - JavaScript is perhaps the best known prototype-based programming language, which employs cloning from prototypes rather than inheriting from a class (contrast to class-based programming).  
    - Another scripting language that takes this approach is Lua.  


- - OOP: Classes and Objects
- - OOP models a real world, real life, object such as a Virtual Restaurant with a VRrtual Manager, Chef, Waiter, & Cleaner.  
  - These objects contain/have things and do things.
    - Attributes
      - Things an object has
    - Methods
      - Things an object do
    - Virtual Restaurant
      - Waiter (Object)
        - Atttribute (variable associated with--attached to--object):
          - is_holding_plate = True
          - tables_responsible = [4, 5, 6]
        - Methods (function that modeled object performs):
          - <b>def</b> take_order(table, order)
            - takes order to chef
          - <b>def</b> take_payment (amount)
            - add money to restaurant
      - Can generate many 'Waiters' from the same 'blueprint' (called "class" in OOP)  


- Link to python Turtle documentation:
  - https://docs.python.org/3/library/turtle.html

- Constructing Objects and Accessing their Attributes and Methods  
  - Class
    - Blueprint
      - Car
        - attributes
          - color
          - wheels
          - mileage
          - speed
          - fuel
        - methods
          - ability to drive
          - ability to stop
          - ability to break
  - From Class generate as many Objects (i.e., cars) that we want
    - Object is the actual thing we will use in our code
      - car is the object created from car blueprint
      - use pascal case to name classes
        - car = CarBlueprint()
      - car.speed (use '.' to separate object from attribute)
        - dot notation
        - from car object get speed attribute  
      - car.stop() (use same dot notation to separate object from method)
        - calling stop function (method) associated with the car object.  