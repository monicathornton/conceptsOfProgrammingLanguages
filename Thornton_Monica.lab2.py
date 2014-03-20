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

    #getter method to return the instance variable _name for the particular element (inherited in subclasses)
    def name(self):
         return self._name

    """An abstract method to compare Elements, to determine the winner when pitted against eachother. Each subclass
    will override this method, and we will not be comparing Element objects to eachother directly, so we throw an exception
    if someone tries to compare two Element objects directly. """
    def compareTo(self, element):
         raise NotImplementedError("Not yet implemented")

"""A subclass to represent the Rock element, which triumphs when pitted against Lizard or Rock,
but perishes against Paper or Spock. If Rock is played against itself in a match, it results in a tied game."""
class Rock (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Rock"

    #Constructor to build Rocks
    def __init__(self,name):
        super(Rock,self).__init__("Rock")
         
    def compareTo(self, element):
        #A winning case, Rock crushes Lizard
        if (element.name() == "Lizard"):
            return ("Rock crushes Lizard", "Win")

        #A winning case, Rock crushes Scissors
        if (element.name() == "Scissors"):
            return ("Rock crushes Scissors", "Win")

        #Tie case, where both players throw Rock (Rock equals Rock)
        if (self == element):
            return ("Rock equals Rock", "Tie")  

        #A losing case, Paper covers Rock
        if (element.name() == "Paper"):
            return ("Paper covers Rock", "Lose")        

        #A losing case, Spock vaporizes Rock
        if (element.name() == "Spock"):
            return ("Spock vaporizes Rock", "Lose")         

class Paper (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Paper"

    #Constructor to build Rocks
    def __init__(self,name):
        super(Paper,self).__init__("Paper")
         
    def compareTo(self, element):
        #A winning case, Paper covers Rock
        if (element.name() == "Rock"):
            return ("Paper covers Rock", "Win")

        #A winning case, Paper disproves Spock
        if (element.name() == "Spock"):
            return ("Paper disproves Spock", "Win")

        #Tie case, where both players throw Paper (Paper equals Paper)
        if (self == element):
            return ("Paper equals Paper", "Tie")  

        #A losing case, Scissors cut Paper
        if (element.name() == "Scissors"):
            return ("Scissors cut Paper", "Lose")        

        #A losing case, Lizard eats Paper
        if (element.name() == "Lizard"):
            return ("Lizard eats Paper", "Lose")      

class Scissors (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Scissors"

    #Constructor to build Scissors
    def __init__(self,name):
        super(Scissors,self).__init__("Scissors")
         
    def compareTo(self, element):
        #A winning case, Scissors cut Paper
        if (element.name() == "Paper"):
            return ("Scissors cut Paper", "Win")

        #A winning case, Scissors decapitate Lizard
        if (element.name() == "Lizard"):
            return ("Scissors decapitate Lizard", "Win")

        #Tie case, where both players throw Scissors (Scissors equals Scissors)
        if (self == element):
            return ("Scissors equals Scissors", "Tie")  

        #A losing case, Spock smashes Scissors
        if (element.name() == "Spock"):
            return ("Spock smashes Scissors", "Lose")        

        #A losing case, Rock crushes Scissors
        if (element.name() == "Rock"):
            return ("Rock crushes Scissors", "Lose")    

class Lizard (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Lizard"

    #Constructor to build Scissors
    def __init__(self,name):
        super(Lizard,self).__init__("Lizard")
         
    def compareTo(self, element):
        #A winning case, Lizard poisons Spock
        if (element.name() == "Spock"):
            return ("Lizard poisons Spock", "Win")

        #A winning case, Lizard eats Paper
        if (element.name() == "Paper"):
            return ("Lizard eats Paper", "Win")

        #Tie case, where both players throw Lizard (Lizard equals Lizard)
        if (self == element):
            return ("Lizard equals Lizard", "Tie")  

        #A losing case, Rock crushes Lizard
        if (element.name() == "Rock"):
            return ("Rock crushes Lizard", "Lose")        

        #A losing case, Scissors decapitate Lizard
        if (element.name() == "Scissors"):
            return ("Scissors decapitate Lizard", "Lose")    

class Spock (Element):
    #the name instance variable from Element is overriden, and its value set to Rock
    _name = "Spock"

    #Constructor to build Scissors
    def __init__(self,name):
        super(Spock,self).__init__("Spock")
         
    def compareTo(self, element):
        #A winning case, Spock smashes Scissors
        if (element.name() == "Scissors"):
            return ("Spock smashes Scissors", "Win")

        #A winning case, Spock vaporizes Rock
        if (element.name() == "Rock"):
            return ("Spock vaporizes Rock", "Win")

        #Tie case, where both players throw Spock (Spock equals Spock)
        if (self == element):
            return ("Spock equals Spock", "Tie")  

        #A losing case, Paper disproves Spock
        if (element.name() == "Paper"):
            return ("Paper disproves Spock", "Lose")        

        #A losing case, Lizard poisons Spock
        if (element.name() == "Lizard"):
            return ("Lizard poisons Spock", "Lose")    

#rock = Rock()
#paper = Paper(`Paper')
#print rock.compareTo(paper)
#print paper.compareTo(rock)
#print rock.compareTo(rock)
#result1 = Element('Rock') 
#result1.compareTo('Rock')

rock = Rock("Rock")
paper = Paper("Paper")
scissors = Scissors("Scissors")
lizard = Lizard("Lizard")
spock = Spock("Spock")

print("Testing Rock")
print(rock.compareTo(lizard))
print(rock.compareTo(scissors))
print(rock.compareTo(rock))
print(rock.compareTo(paper))
print(rock.compareTo(spock))
print("_____________")
print("Testing Paper")
print(paper.compareTo(rock))
print(paper.compareTo(spock))
print(paper.compareTo(paper))
print(paper.compareTo(scissors))
print(paper.compareTo(lizard))
print("_____________")
print("Testing Scissors")
print(scissors.compareTo(paper))
print(scissors.compareTo(lizard))
print(scissors.compareTo(scissors))
print(scissors.compareTo(spock))
print(scissors.compareTo(rock))
print("_____________")
print("Testing Lizard")
print(lizard.compareTo(spock))
print(lizard.compareTo(paper))
print(lizard.compareTo(lizard))
print(lizard.compareTo(rock))
print(lizard.compareTo(scissors))
print("_____________")
print("Testing Spock")
print(spock.compareTo(scissors))
print(spock.compareTo(rock))
print(spock.compareTo(spock))
print(spock.compareTo(paper))
print(spock.compareTo(lizard))
print("_____________")

def init_list():
    # global variable, can be used anywhere within the file after
    # init_list gets called, since it's declared with "global" keyword
    rock = Rock("Rock")
    paper = Paper("Paper")
    scissors = Scissors("Scissors")
    lizard = Lizard("Lizard")
    spock = Spock("Spock")
    
    global moves
    moves = [rock, paper, scissors, lizard, spock]

    for i in range(len(moves)):
        print(moves[i])


init_list()
print("Does this work?")
print(moves[0].compareTo(moves[1]))
