
# NOTE: A docstring should prescribe the code segment's effect, not describe it.
# In other words, it should take the form of an imperative
# (e.g. "Do this", "Return that", "Compute this", "Convert that", etc.),
# not a description (e.g. "Does this", "Returns that", "Forms this", "Extends that", etc.).

# CORRECT / RECOMMENDED EXAMPLES:

def greeting(name):
    """Take a name and return its replicated form."""
    return name * 2

def my_function(x, y):
    """Compute the angles and return a list of coordinates."""

def king_creator(name="Greg", ordinal="I", country="Neverland"):
    """Create a king following the article title naming convention.
    
    Keyword arguments:
    :arg name: the king's name (default: Greg)
    :type name: str
    :arg ordinal: Roman ordinal number (default: I)
    :type ordinal: str
    :arg country: the country ruled (default: Neverland)
    :type country: str
    """
    if name == "Voldemort":
        return "Voldemort is a reserved name."


class Vehicle:
    """A class to represent a Vehicle.
    
    Attributes:
    -----------
    vehicle_type: str
        The type of the vehicle, e.g. a car.
    id_number: int
        The vehicle identification number.
    is_autonomous: bool
        self-driving -> True, not self-driving -> False

    
    Methods:
    --------
    report_location(lon=45.00, lat=90.00)
        Print the vehicle id number and its current location.
        (default longitude=45.00, default latitude=90.00)
    """
    
    def __init__(self, vehicle_type, id_number, is_autonomous=True):
        """
        Parameters:
        -----------
        vehicle_type: str
            The type of the vehicle, e.g. a car.
        id_number: int
            The vehicle identification number.
        is_autonomous: bool, optional
            self-driving -> True (default), not self-driving -> False
        """
        
        self.vehicle_type = vehicle_type
        self.id_number = id_number
        self.is_autonomous = is_autonomous
    
    def report_location(self, id_number, lon=45.00, lat=90.00):
        """
        Print the vehicle id number and its current location.
        
        Parameters:
        -----------
        id_number: int
            The vehicle identification number.
        lon: float, optional
            The vehicle's current longitude (default is 45.00)
        lat: float, optional
            The vehicle's current latitude (default is 90.00)
        """
