# 0x05. Python - Exceptions

Exceptions in Python are events that occur when an error happens during the execution of a program. When an exception is raised, it propagates up the call stack until it's caught by an exception handler. If it's not caught, the program will terminate.
Python has many built-in exceptions, such as TypeError, ValueError, IndexError, and so on. You can also define your own exceptions by creating a new class that inherits from the Exception class.
You can handle exceptions using a try/except block. Here's a simple example:

try:
    # code that might raise an exception
except ExceptionType:
    # code to handle the exception

In this example, if an exception of type ExceptionType is raised in the try block, the code in the except block will be executed. If the exception is of a different type, it won't be caught by this except block.

## Tasks List

0. Safe list printing
1. Safe printing of an integers list
2. Print and count integers
3. Integers division with debug
4. Divide a list
5. Raise exception
6. Raise a message
