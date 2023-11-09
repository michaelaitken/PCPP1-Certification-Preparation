'''
Objectives

    Improving the student's skills in creating decorators and operating with them.

Scenario

    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

'''

import datetime

def timestamp(flag):
    def wrapper(function):
        def internal_wrapper(*args, **kwargs):
            print(f"[{flag}] START: {datetime.datetime.now()}")
            function(*args, **kwargs)
            print(f"[{flag}] END: {datetime.datetime.now()}")
        return internal_wrapper
    return wrapper

@timestamp("Multiply")
def simple_multiply(a, b):
    print(a * b)
    
@timestamp("Add")
def simple_add(a, b):
    print(a + b)

# === Testing ===
simple_multiply(4, 6)
simple_add(10, 45)