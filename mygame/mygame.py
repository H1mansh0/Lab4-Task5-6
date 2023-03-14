"""
Game code
"""

class Street:
    """
    Class of rooms
    """

    def __init__(self, name):
        """
        init function
        """
        self.name = name
        self.rooms = []

    def set_description(self, description):
        """
        Create description for istance
        """
        self.description = description

    
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
    
    def link_street(self, nextroom, destination):
        """
        Sets the next possible room
        and sets the destination to it
        """
        self.nextroom = nextroom
        self.destination = destination
        self.rooms += [(self.nextroom, self.destination)]
        
    def move(self, destination_user):
        """
        If the destination to next room correct
        returns next room
        """
        for ele in self.rooms:
            if destination_user in ele:
                return ele[0]
            
    def get_details(self):
        """
        Return details of isintance
        """
        print(
            f'{self.name}\n'
            '---------------------\n'
            f'{self.description}\n'
        )
        for ele in self.rooms:
            print(f'{ele[0].name} {ele[1]} [{ele[1]}]')

class Final_street(Street):

    rooms = []

    def __init__(self, name):
        """
        init function
        """
        self.name = name
        
    def move(self, destination_user):
        """
        If the destination to next room correct
        returns next room
        """
        print('Це фінальна битва. Звідси не можна втекти! [битись]')

class Character:
    """
    Class of all characters
    """

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
        print(
            f'{self.name} тут\n'
            f'{self.description} [битись, говорити]'
            )
    
    def talk(self):
        """
        Returns phrase of character
        """
        print(self.conv)


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
            return True
        else: return False

class Big_enemy(Enemy):
    def __init__(self, name, description):
        """
        init function
        """
        super(Enemy, self).__init__(name, description)

    def final_heet(self):
        """
        Returns a question
        """
        print('Під яким кущем під час дощу ховається заєць?')

class Friend(Character):
    """
    Class of allies
    """
    def __init__(self, name, description):
        """
        init function
        """
        super(Friend, self).__init__(name, description) 

    def set_treatment(self, treatment):
        """
        Sets new attribute: treatment
        """
        self.treatment = treatment

    def set_item(self, item):
        """
        Sets new attribute: item
        """
        self.item = item


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
        print(f'Ви знайшли {self.name} - {self.description} [взяти]')

class Hint(Item):
    """
    Class of hints
    """
    def __init__(self, name):
        """
        init function
        """
        super(Hint, self).__init__(name)

    def use_hint(self):
        """
        Prints hint
        """
        print('Ви розгорнули підказку. Вона пуста, але мокра')
