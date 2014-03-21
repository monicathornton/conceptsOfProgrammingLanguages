######################################### 	
#  CSCI 305 - Programming Lab #2		
#										
#  Monica Thornton			
#  monicasuethornton@gmail.com			
#
# A program to play the game Rock, Paper, Scissors, Lizard, Spock.
# A variation on Rock, Paper, Scissors with more elements to lessen
# the chance of a tie.
#########################################

#String variable indicating my name.
#I did not work with a partner on this lab
myName = "Monica Thornton"
print ("CSCI 305 Lab 2 submitted by " + myName + ".")

"""A superclass that the five subclasses Rock, Paper, Scissors, Lizard and Spock all inherit from"""
class Element (object):
    #an instance variable to store the name of each Element
    _name = ""

    """A constructor for the Element class, which not only builds an Element, but will be used to specify a name
     in the subclasses(i.e. Rock, Paper, Scissors, et al). Because we are not instantiating any Element objects directly,
     name is an empty string in this class, and is overridden in the subclasses"""
    def __init__(self, _name):
         self._name = _name

    #getter method to return the instance variable _name for the particular Element (inherited in subclasses)
    def name(self):
         return self._name

    """An abstract method to compare Elements, to determine the win status/method of winning when pitted against eachother.
    Each subclass will override this method in different ways, and we will not be comparing Element objects to eachother directly,
    so we throw an exception if someone tries to compare two Element objects directly. """
    def compareTo(self, element):
         raise NotImplementedError("Not yet implemented")

"""A subclass to represent the Rock element, which triumphs when pitted against Lizard or Rock,
but perishes against Paper or Spock. If Rock is played against itself in a match, it results in a tied game."""
class Rock (Element):
    #The name instance variable from Element is overriden, and its value set to Rock
    _name = "Rock"

    #Constructor to build Rocks
    def __init__(self,name):
        super(Rock,self).__init__("Rock")

    #Overrides the compareTo method inherited from element, with all the particular win/loss info for this Element     
    def compareTo(self, Element):
        #A winning case, represents the case when Rock (the self parameter) is played against Lizard(the Element parameter)
        if (Element.name() == "Lizard"):
            return (self.name() + " crushes " + Element.name(), "Win")

        #A winning case, represents the case when Rock (the self parameter) is played against Scissors(the Element parameter)
        if (Element.name() == "Scissors"):
            return (self.name() + " crushes " + Element.name(), "Win")

        #Tie case, where both players throw Rock
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name(), "Tie")  

        #A losing case, represents the case when Rock (the self parameter) is played against Paper (the Element parameter)
        if (Element.name() == "Paper"):
            return (Element.name() + " covers " + self.name(), "Lose")        

        #A losing case, represents the case when Rock (the self parameter) is played against Spock (the Element parameter)
        if (Element.name() == "Spock"):
            return (Element.name() + " vaporizes " + self.name(), "Lose")         

"""A subclass to represent the Paper element, which triumphs when pitted against Rock or Spock,
but perishes against Scissors or Lizard. If Paper is played against itself in a match, it results in a tied game."""
class Paper (Element):
    #the name instance variable from Element is overriden, and its value set to Paper
    _name = "Paper"

    #Constructor to build Papers
    def __init__(self,name):
        super(Paper,self).__init__("Paper")

    #Overrides the compareTo method inherited from element, with all the particular win/loss info for this element              
    def compareTo(self, Element):
        #A winning case, represents the case when Paper (the self parameter) is played against Rock (the Element parameter)
        if (Element.name() == "Rock"):
            return (self.name() + " covers " + Element.name(), "Win")

        #A winning case, represents the case when Paper (the self parameter) is played against Spock (the Element parameter)
        if (Element.name() == "Spock"):
            return (self.name() + " disproves " + Element.name(), "Win")

        #Tie case, where both players throw Paper
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name(), "Tie")  

        #A losing case, represents the case when Paper (the self parameter) is played against Scissors (the Element parameter)
        if (Element.name() == "Scissors"):
            return (Element.name() + " cut " + self.name(), "Lose")        

        #A losing case, represents the case when Paper (the self parameter) is played against Lizard (the Element parameter)
        if (Element.name() == "Lizard"):
            return (Element.name() + " eats " + self.name(), "Lose")      

"""A subclass to represent the Scissors element, which triumphs when pitted against Paper or Lizard,
but perishes against Spock or Rock. If Scissors is played against itself in a match, it results in a tied game."""
class Scissors (Element):
    #the name instance variable from Element is overriden, and its value set to Scissors
    _name = "Scissors"

    #Constructor to build Scissors
    def __init__(self,name):
        super(Scissors,self).__init__("Scissors")

    #Overrides the compareTo method inherited from element, with all the particular win/loss info for this element            
    def compareTo(self, Element):
        #A winning case, represents the case when Scissors (the self parameter) is played against Paper (the Element parameter)
        if (Element.name() == "Paper"):
            return (self.name() + " cut " + Element.name(), "Win")

        #A winning case, Scissors decapitate Lizard
        if (Element.name() == "Lizard"):
            return (self.name() + " decapitate " + Element.name(), "Win")

        #Tie case, where both players throw Scissors (Scissors equals Scissors)
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name(), "Tie")  

        #A losing case, Spock smashes Scissors
        if (Element.name() == "Spock"):
            return (Element.name() + " smashes " + self.name(), "Lose")        

        #A losing case, Rock crushes Scissors
        if (Element.name() == "Rock"):
            return (Element.name() + " crushes " + self.name(), "Lose")    

"""A subclass to represent the Lizard element, which triumphs when pitted against Spock or Paper,
but perishes against Rock or Scissors. If Lizard is played against itself in a match, it results in a tied game."""
class Lizard (Element):
    #the name instance variable from Element is overriden, and its value set to Lizard
    _name = "Lizard"

    #Constructor to build Lizard
    def __init__(self,name):
        super(Lizard,self).__init__("Lizard")

    #Overrides the compareTo method inherited from element, with all the particular win/loss info for this element           
    def compareTo(self, Element):
        #A winning case, represents the case when Lizard (the self parameter) is played against Spock (the Element parameter)
        if (Element.name() == "Spock"):
            return (self.name() + " poisons " + Element.name(), "Win")

        #A winning case, represents the case when Lizard (the self parameter) is played against Paper (the Element parameter)
        if (Element.name() == "Paper"):
            return (self.name() + " eats " + Element.name(), "Win")

        #Tie case, where both players throw Lizard
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name(), "Tie")  

        #A losing case, represents the case when Lizard (the self parameter) is played against Rock (the Element parameter) 
        if (Element.name() == "Rock"):
            return (Element.name() + " crushes " + self.name(), "Lose")        

        #A losing case, represents the case when Lizard (the self parameter) is played against Lizard (the Element parameter) 
        if (Element.name() == "Scissors"):
            return (Element.name() + " decapitate " + self.name(), "Lose")    

"""A subclass to represent the Spock element, which triumphs when pitted against Scissors or Rock,
but perishes against Paper or Lizard. If Spock is played against itself in a match, it results in a tied game."""
class Spock (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Spock"

    #Constructor to build Spocks
    def __init__(self,name):
        super(Spock,self).__init__("Spock")
        
    #Overrides the compareTo method inherited from element, with all the particular win/loss info for this element            
    def compareTo(self, Element):
        #A winning case, represents the case when Spock (the self parameter) is played against Scissors (the Element parameter)
        if (Element.name() == "Scissors"):
            return (self.name() + " smashes " + Element.name(), "Win")

        #A winning case, represents the case when Spock (the self parameter) is played against Rock (the Element parameter)
        if (Element.name() == "Rock"):
            return (self.name() + " vaporizes " + Element.name(), "Win")

        #Tie case, where both players throw Spock 
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name() + " - MIND MELD!!!", "Tie")  

        #A losing case, represents the case when Spock (the self parameter) is played against Paper (the Element parameter) 
        if (Element.name() == "Paper"):
            return (Element.name() + " disproves " + self.name(), "Lose")        

        #A losing case, represents the case when Spock (the self parameter) is played against Lizard (the Element parameter)  
        if (Element.name() == "Lizard"):
            return (Element.name() + " poisons " + self.name(), "Lose")    

"""A method to create a concrete instance of each of the five Element subclasses, and to store each of these
in a global list named moves"""
def moves_list():
    #Creates a concrete instance of Rock, Paper, Scissors, Lizard, Spock, saves them with appropriate variable names
    rock = Rock("Rock")
    paper = Paper("Paper")
    scissors = Scissors("Scissors")
    lizard = Lizard("Lizard")
    spock = Spock("Spock")

    #Creates a global variable named moves
    global moves

    #Constructs a list of all possible moves a player could throw, saves it in the (global) variable moves 
    moves = [rock, paper, scissors, lizard, spock]

#Calls the moves list function, so the moves are instantiated and stored in a list
moves_list()

"""COMMENt HERE DOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
class Player (object):
    #an instance variable to store the name of each Player
    _name = ""

    """Comment this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
    def __init__(self, _name):
         self._name = _name

    #getter method to return the instance variable _name for the particular Player (inherited in subclasses)
    def name(self):
         return self._name

    """Comment this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Is self right param?"""
    def play(self):
         raise NotImplementedError("Not yet implemented")


class StupidBot (Player):
    _name = "Stupid Bot"

    def __init__(self,name):
        super(StupidBot,self).__init__("Stupid Bot")
    
    def play(self):
        return moves[0]

p1 = StupidBot('Stupid Bot')
p1move = p1.play()
p2 = StupidBot('Stupid Bot')
p2move = p2.play()

print(p1.name())
print(moves[0].name())
print (p1move.compareTo(p2move))
 






