# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
                
        if type(self.name) != str:
            raise TypeError
        elif self.name == "":
            raise ValueError
        

    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        Splits the name via whitespaces available and then uppercase the first letter of each seperated word.
        """
        spaces= self.name.split()
        combined = ""
        for x in spaces:
            initials = x[0].upper()
            combined += initials
        return combined

    def is_birthday(self):
        """
        Takes todays day, formats it so only days and months are available, does the same for the given input, if they match returns true if not returns false.
        """
        
        today = date.today()
        md = today.strftime("%m-%d")
        md1 = self.birth[5:]
        if str(md) == md1:
            return True 
        else:
            return False
            

    

    # (see README.md for further details)
