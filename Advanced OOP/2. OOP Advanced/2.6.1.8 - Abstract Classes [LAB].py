'''
Objectives

    Creation of abstract classes and abstract methods;
    multiple inheritance of abstract classes;
    overriding abstract methods;
    delivering multiple child classes.

Scenario

    You are about to create a multifunction device (MFD) that can scan and print documents;
    the system consists of a scanner and a printer;
    your task is to create blueprints for it and deliver the implementations;
    create an abstract class representing a scanner that enforces the following methods:
        scan_document - returns a string indicating that the document has been scanned;
        get_scanner_status - returns information about the scanner (max. resolution, serial number)
    Create an abstract class representing a printer that enforces the following methods:
        print_document - returns a string indicating that the document has been printed;
        get_printer_status - returns information about the printer (max. resolution, serial number)
    Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
        MFD1 - should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
        MFD2 - should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
        MFD3 - should be a premium device allowing additional operations like printing operation history and fax machine.
    Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
'''

import abc

# == ABSTRACT CLASSES / INTERFACES == 

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self) -> str:
        pass
    
    @abc.abstractmethod
    def get_scanner_status(self) -> tuple:
        pass
    
class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self) -> str:
        pass
    
    @abc.abstractmethod
    def get_printer_status(self) -> tuple:
        pass
    
# == IMPLEMENTED CLASSES ==
# Cheap Multi Function Device (MFD1)
class MDF1(Scanner, Printer):
    __serial_number = 0
    
    def __init__(self) -> None:
        MDF1.__serial_number += 1
        self.serial_number = MDF1.__serial_number
        self.max_resolution = "480p"
    
    def scan_document(self) -> str:
        return "Document has been scanned"
    
    def get_scanner_status(self) -> tuple:
        return (self.max_resolution, f"MDF{self.serial_number}")
    
    def print_document(self) -> str:
        return "Document has been printed"

    def get_printer_status(self) -> tuple:
        return self.get_scanner_status()
    

# Medium-priced Multi Function Device (MDF2)
class MDF2(MDF1):
    def __init__(self) -> None:
        super().__init__()
        self.max_resolution = "720p"
        self.number_of_documents_printed = 0
    
    def print_operation_history(self) -> str:
        return f"Number of documents printed: {self.number_of_documents_printed}"
    

# Premium Multi Function Device (MDF3)
class MDF3(MDF2):

    def __init__(self) -> None:
        super().__init__()
        self.max_resolution = "1080p"
 
    def send_document(self) -> str:
        return f"{self.scan_document()} & sent"
    
# === TESTING ===

for device in MDF1(), MDF2(), MDF3():
    print(device.scan_document())
    print(device.get_scanner_status())
    print(device.print_document())
    print(device.get_printer_status())
    
    if isinstance(device, MDF2):
        print(device.print_operation_history())
    
    if isinstance(device, MDF3):
        print(device.send_document())