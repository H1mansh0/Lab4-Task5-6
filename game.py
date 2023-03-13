"""
Game code
"""

class Room:
    """
    Class of rooms
    """

    def __init__(self, name):
        """
        init function
        """
        self.name = name

    def set_description(self, description):
        """
        Create description for istance
        """
        self.description = description

    def get_details(self):
        """
        Return details of isintance
        """
        print(self.description)
    
    def set_item(self, item):
        """
        Create new attribute: item
        """
        self.item = item

    def set_character(self, character):
        """
        Create new attribute: character
        """
        self.character = character

    def get_character(self):
        """
        Returns character
        """
        try: return self.character
        except AttributeError: return None
    
    def get_item(self):
        """
        Returns item
        """
        try: return self.item
        except AttributeError: return None
    
    def link_room(self, nextroom, destination):
        """
        Sets the next possible room
        and sets the destination to it
        """
        self.nextroom = nextroom
        self.destination = destination
        
    def move(self, destination_user):
        """
        If the destination to next room correct
        returns next room
        """
        if destination_user == self.destination: return self.nextroom
            
    

class Character:
    """
    Class of all characters
    """

    _wins = 0

    def __init__(self, name , description):
        """
        init function
        """
        self.name = name
        self.description = description
        

    def set_conversation(self, conv):
        """
        Create new attribute: character's phrase
        """
        self.conv = conv

    def describe(self):
        """
        Returns description of character
        """
        print(self.description)
    
    def talk(self):
        """
        Returns phrase of character
        """
        print(self.conv)
    
    def get_defeated(self):
        """
        Returns amount of wins
        """
        return self._wins
    


class Enemy(Character):
    """
    Class of enemies
    """

    def __init__(self, name, description):
        """
        init function
        """
        super(Enemy, self).__init__(name, description)

    def set_weakness(self, weakness):
        """
        Create new attribute: weakness
        """
        self.weakness = weakness

    def fight(self, item):
        """
        Check if the main hero can kill character
        """
        if item == self.weakness:
            Character._wins += 1
            return True
        else: return False

    

class Friend(Character):
    """
    Class of allies
    """
    def __init__(self, name, description):
        """
        init function
        """
        super(Friend, self).__init__(name, description) 


class Item():
    """
    Class of items
    """
    def __init__(self, name):
        """
        init function
        """
        self.name = name

    def set_description(self, description):
        """
        Create description for istance
        """
        self.description = description

    def get_name(self):
        """
        Returns name of item
        """
        return self.name
    
    def describe(self):
        """
        Returns description of item
        """
        print(self.description)
