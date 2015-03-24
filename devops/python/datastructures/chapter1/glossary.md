### GLOSSARY

#### 1.1 Python Overview

Interpreted language - commands executed through Python Interpreter rather than being compiled at a low level. 

#### 1.2 Objects in Python 

Assignment statement - statement that copies value into a variable, e.g. genre = "rock." 

Identifier - initital value getting assigned an object, in this case "genre."

Object - location in memory having a value. Can be a variable, data structure, or function.

Reserved words - True, False, or, etc. Most logic statements and statements related to control structure. 

Instantiation -  The process of creating a new instance of a class. cur = conn.cursor() 

Methods - Also known as member functions defined by "." of an instantiated class. conn = mysql.connector.connect(...) 

Built-in classes - bool (immutable), int(immutable), float(immutable), list(mutable), tuple(mutabke), str(immutable), set(mutable), frozenset(immutable), dict(mutable).

#### 1.3  Expressions, Operators, and Precedense

Expressions - Piece of syntax which can be evaluated to some value like names, operators, or function calls. In bar = "foo", "foo" is an expression while "bar = "foo"" is a statement.  

Operators - truth statements (true or false)  and arithmatic comparisons (+,-, % = modulo). 

Compound Expressions - two or more operations (a + b + c).

#### 1.4 Control Flow

Conditionals - if statements. 

Break statement - terminates while or for loop when executed within body.

Continue statement - causes current run of a loop to stop, but continues processing ongoing passes. 

#### 1.5 Functions

Function vs method - function is a normal, stateless, call without a class. Method is object-oriented function. 

Signature - definition of the function. For example, in def fun(aweyeah), awyeah is part of the signature and identifier. 

Function body - everything located within a function. 

Activation Record - stores information relevant to current system call each time function is called. Includes namespace to manage identifiers by managed by local scope.

Return - Used to indicate the end of a function. None returned if not used. 

#### 1.5.1 Information Passing

Formal parameters - Identifiers used to describe expected parameters. For example, def music(genre, artist).

Actual parameters - Objects sent by caller when invoking function. For example, genre="rock" artist="Cloud Cult".

Polymorphic - defining one or more default values for parameters. austin(pop=8885400, growth, jobs), "pop" has default value unless otherwise set.

Positional arguments - parameters sent to caller based on position. Such as music(verse, chorus, tag), music(3, 2, 1), 3 is verse, 2 chorus, 1 tag.  

Keyword argument - allows to set function values explicitely. Like music(chorus=2) will assign chorus with a value of 2 regardless of position. 

#### 1.5.2 Built in functions

I/O: print, input, open.

Character Encoding: ord and chr.

Mathematics: abs, divmod, pow, round, and sum.

Ordering: max and min. 

Collections/Iterations: range, len, reversed, all, any, and map. 
