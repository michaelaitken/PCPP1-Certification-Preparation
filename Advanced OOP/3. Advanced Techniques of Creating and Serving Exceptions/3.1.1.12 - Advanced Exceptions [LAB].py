'''
Objectives

    improving the student's skills in operating with different kinds of exceptions.

Scenario

    Try to extend the check list script to handle more different checks, all reported as RocketNotReady exceptions.
    Add your own checks for: batteries and circuits.
'''

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    # add your own implementation
    try:
        print("Battery charge level is {}%".format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with battery read-out') from e

def circuits_check():
    # add your own implementation
    try:
        print(f"\t {systems[0]} system is online.")
        print(f"\t {systems[1]} system is online.")
        print(f"\t {systems[2]} system is online.")
        print(f"\t {systems[3]} system is online.")
    except IndexError as e:
        raise RocketNotReadyError("Not all systems online!") from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
systems = ['Radar', 'Communications', 'Life Support']
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
