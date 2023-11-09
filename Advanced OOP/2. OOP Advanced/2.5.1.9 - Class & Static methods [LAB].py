'''
Objectives

    improving the student's skills in operating with static and class methods

Scenario

    Create a class representing a luxury watch;
    The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
    the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
    the regular __init__ method should only increase the value of the appropriate class variable;

The text intended to be engraved should follow some restrictions:

    it should not be longer than 40 characters;
    it should consist of alphanumerical characters, so no space characters are allowed;
    if the text does not comply with restrictions, an exception should be raised;

before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

    Create a watch with no engraving
    Create a watch with correct text for engraving
    Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
    After each watch is created, call class method to see if the counter variable was increased

'''


class Watch:
    watches_created = 0
    
    @classmethod
    def get_number_of_watches_created(cls) -> int:
        return cls.watches_created
    
    def __init__(self) -> None:
        self.engraving = ''
        Watch.watches_created += 1
    
    @classmethod
    def create_with_engraving(cls, engraving):
        if cls.validate_engraving(engraving):
            _watch = cls()
            _watch.engraving = engraving
            return _watch
        
    @staticmethod
    def validate_engraving(engraving: str):
        if len(engraving) > 40:
            raise Exception("Engraving cannot be longer than 40 chracters!")
        elif engraving.count(' ') != 0:
            raise Exception("Engraving cannot contain any spaces!")
        else:
            return True



# === Testing ===

watch1 = Watch()
print(Watch.get_number_of_watches_created())

watch2 = Watch.create_with_engraving("JohnSmith")
print(Watch.get_number_of_watches_created())

try:
    watch3 = Watch.create_with_engraving("Happy Birthday")
except Exception:
    print("Invalid Engraving!")
print(Watch.get_number_of_watches_created())