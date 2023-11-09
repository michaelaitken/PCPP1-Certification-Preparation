'''
Objective:
- Improving my skills in operating with special methods

Scenario
 - Create a class representing a time interval;
 - the class should implement its own method for addition, subtraction on time interval class objects;
 - the class should implement its own method for multiplication of time interval class objects by an integer-type value;
 - the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
 - the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
 - check the argument type, and in case of a mismatch, raise a TypeError exception.
'''

class Time:
    def __init__(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def check_seconds(self) -> None:
        while self.second >= 60 or self.second < 0:
            if self.second >= 60:
                self.minute += 1
                self.second -= 60
            if self.second < 0:
                self.minute -= 1
                self.second += 60
    
    def check_minutes(self) -> None:
        while self.minute >= 60 or self.minute < 0:
            if self.minute >= 60:
                self.hour += 1
                self.minute -= 60
            if self.minute < 0:
                self.hour -= 1
                self.minute += 60
    
    def check_hours(self) -> None:
        if self.hour < 0:
            raise ArithmeticError       # Throws an Arithmetic Error if the Time value is < 0
    
    def check_values(self) -> None:
        self.check_seconds()
        self.check_minutes()
        self.check_hours()
    
    def __add__(self, time: object) -> None:
        if not isinstance(time, Time):
            raise TypeError
        
        self.second += time.second
        self.minute += time.minute
        self.hour += time.hour
        self.check_values()
    
    def __sub__(self, time: object) -> None:
        if not isinstance(time, Time):
            raise TypeError
        
        self.second -= time.second
        self.minute -= time.minute
        self.hour -= time.hour
        self.check_values()
        
    def __mul__(self, value: int) -> None:
        self.second *= value
        self.minute *= value
        self.hour *= value
        self.check_values()
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    

# Testing the Time Class
print("=== TESTING ===")
time1 = Time(3, 15, 55)
time2 = Time(4, 55, 15)
time3 = Time(3, 12, 21)
print(time1)
print(time2)
print(time3)

print("=== Add ===")
time1 + time2
print(time1)

print("=== Subtract ===")
time1 - time3
print(time1)

print("=== Multiply ===")
time1 * 2
print(time1)