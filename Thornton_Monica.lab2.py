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

import random

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
    so we throw an exception if someone tries to compare two Element objects directly."""
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

    #Overrides the compareTo method inherited from Element, with all the particular win/loss info for this Element     
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

    #Overrides the compareTo method inherited from Element, with all the particular win/loss info for this Element              
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

    #Overrides the compareTo method inherited from Element, with all the particular win/loss info for this Element            
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

    #Overrides the compareTo method inherited from Element, with all the particular win/loss info for this Element           
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
        
    #Overrides the compareTo method inherited from Element, with all the particular win/loss info for this Element            
    def compareTo(self, Element):
        #A winning case, represents the case when Spock (the self parameter) is played against Scissors (the Element parameter)
        if (Element.name() == "Scissors"):
            return (self.name() + " smashes " + Element.name(), "Win")

        #A winning case, represents the case when Spock (the self parameter) is played against Rock (the Element parameter)
        if (Element.name() == "Rock"):
            return (self.name() + " vaporizes " + Element.name(), "Win")

        #Tie case, where both players throw Spock 
        if (self.name() == Element.name()):
            return (self.name() + " equals " + Element.name() + " - MIND MELD!", "Tie")  

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

"""A superclass that the six subclasses StupidBot, RandomBot, IterativeBot, LastPlayBot, HumanBot and MyBot all inherit from"""
class Player (object):
    #an instance variable to store the name of each Player
    _name = ""

    """A constructor for the Player class, which not only builds a Player, but will be used to specify a name
     in the subclasses(i.e. StupidBot, RandomBot, IterativeBot, et al). Because we are not instantiating any Element objects directly,
     name is an empty string in this class, and is overridden in the subclasses"""
    def __init__(self, _name):
         self._name = _name

    #getter method to return the instance variable _name for the particular Player (inherited in subclasses)
    def name(self):
         return self._name

    """An abstract method to specify the different move strategies for each of the Player subclasses. Each subclass will override this method in
    different ways, and we will not be playing with Player objects directly, so we throw an exception if someone tries to
    play with the Player object directly."""
    def play(self):
         raise NotImplementedError("Not yet implemented")

"""A subclass to represent the StupidBot player, which plays the same move every time. In the spirit of the Big Bang Theory,
   StupidBot plays Spock every time."""
class StupidBot (Player):
    #The name instance variable from Player is overriden, and its value set to StupidBot
    _name = "Stupid Bot"

    #Constructor to build StupidBot players
    def __init__(self,name):
        super(StupidBot,self).__init__("Stupid Bot")
        
    #Overrides the play method inherited from Player, with the play the same move every time strategy implemented    
    def play(self):
        #plays Spock for every move 
        return moves[4]

"""A subclass to represent the RandomBot player, which plays a random move every time."""
class RandomBot (Player):
    #The name instance variable from Player is overriden, and its value set to RandomBot
    _name = "Random Bot"

    #Constructor to build RandomBot players
    def __init__(self,name):
        super(RandomBot,self).__init__("Random Bot")
        
    """Overrides the play method inherited from Player, with the Random move strategy implemented. In this strategy, a move is picked at random from
    our moves list and played."""    
    def play(self):

        #Generate a random number between 0 and 4, save it in the variable randomMove
        randomMove = random.randint(0, 4)
        
        #Use randomMove variable to get a move from the moves list
        return moves[randomMove]

"""A subclass to represent the IterativeBot player, which iterates through the move list to choose its move. Once it has gone through
the entire move list, it starts again."""
class IterativeBot (Player):
    #The name instance variable from Player is overriden, and its value set to IterativeBot
    _name = "Iterative Bot"

    #Constructor to build IterativeBot players
    def __init__(self,name):
        super(IterativeBot,self).__init__("Iterative Bot")
        
    """Overrides the play method inherited from Player, with the Iterative move strategy implemented. In this strategy, a move is picked from
    the moves list and played, and the move immediately preceding it is picked for our next move."""    
    def play(self):
        #Specifies that the below variables are global, used to keep track of where we are iteratively for p1 and p2
        global p1IterativeCounter
        global p2IterativeCounter

        #Specifies that the below variables are global, used to specify/differentiate between p1 and p2
        global p1
        global p2

        #Checks if self is p1 or p2 - to update the correct global variables
        if self == p1:
            
            #location is a local variable to keep track of where we are in the moves list, we set it equal to the value in p1IterativeCounter
            location = p1IterativeCounter

            #If location is greater than 4 (because we have 5 moves total and moves is 0 indexed), we start back at the beginning of the list
            if location > 4:
                location = 0
                #increments p1IterativeCounter, so the next time we loop through it - p1IterativeCounter is in the right place
                p1IterativeCounter = location + 1
            else:
                #If location is not greater than 4, update to the next move in the moves list
                p1IterativeCounter = p1IterativeCounter + 1
                  
        elif self == p2:
            #location is a local variable to keep track of where we are in the moves list, we set it equal to the value in p2IterativeCounter
            location = p2IterativeCounter

            #If location is greater than 4 (because we have 5 moves total and moves is 0 indexed), we start back at the beginning of the list
            if location > 4:
                location = p2IterativeCounter
                location = 0
                #increments p2IterativeCounter, so the next time we loop through it - p2IterativeCounter is in the right place
                p2IterativeCounter = location + 1
            else:
                #If location is not greater than 4, update to the next move in the moves list
                p2IterativeCounter = p2IterativeCounter + 1
                            
        #Return the appropriate member of the moves list to the calling function
        return moves[location]            
               
"""A subclass to represent the LastPlayBot player, which chooses its move based on the last move the opponent played."""
class LastPlayBot (Player):
    #The name instance variable from Player is overriden, and its value set to LastPlayBot
    _name = "Last Play Bot"

    #Constructor to build LastPlayBot players
    def __init__(self,name):
        super(LastPlayBot,self).__init__("Last Play Bot")
        
    """Overrides the play method inherited from Player, with the Last Play move strategy implemented. In this strategy, the initial move is chosen randomly,
    and after that moves are picked based on the last move played by the opponent."""
    def play(self):
        #Specifies that the below variables are global, used to specify/differentiate between p1 and p2        
        global p1
        global p2

        #A global variable to store the opponent's last move, used to specify/differentiate between p1 and p2
        global p1sOpponentsMove
        global p2sOpponentsMove

        #Checks if self is p1 or p2 - to update the correct global variables
        if p1 == self:
            #opponentMove is a local variable to keep track of what your opponent played
            opponentMove = p1sOpponentsMove

            #If first move of round (ergo, opponent has not moved yet), play random move
            if opponentMove is None:

                #Generate a random number between 0 and 4, save it in the variable randomMove
                randomMove = random.randint(0, 4)
            
                #Use randomMove variable to get a move from the moves list
                return moves[randomMove]
        
            else:
                #If your opponent has already moved, play their move from last turn for this turn
                return opponentMove

        elif p2 == self:
            #opponentMove is a local variable to keep track of what your opponent played
            opponentMove = p2sOpponentsMove

            #If first move of round (ergo, opponent has not moved yet), play random move
            if opponentMove is None:

                #Generate a random number between 0 and 4, save it in the variable randomMove
                randomMove = random.randint(0, 4)
            
                #Use randomMove variable to get a move from the moves list
                return moves[randomMove]
        
            else:
                #If your opponent has already moved, play their move from last turn for this turn
                return opponentMove

"""A subclass to represent the Human player, in which the series of moves are determined by the Human player."""
class Human (Player):
    #The name instance variable from Player is overriden, and its value set to Human
    _name = "Human"

    #Constructor to build IterativeBot players
    def __init__(self,name):
        super(Human,self).__init__("Human")

    
    """Overrides the play method inherited from Player, with the Human player picking the moves."""    
    def play(self):
        #Prints the menu of options for the human player
        print("(1) : Rock")
        print("(2) : Paper")
        print("(3) : Scissors")        
        print("(4) : Lizard")
        print("(5) : Spock")

        #Sets up a list with all of the valid choices, so we can make sure the user picks one  
        validChoices = [1, 2, 3, 4, 5]

        #Loop to make sure that the input is one of the valid choices
        while True:
            #Casts the user choice as an integer value
            userChoice = int(input("Enter your move: "))
            #Checks if the user choice is valid
            if userChoice in validChoices:
                #If userChoice is a valid entry, subtract one from the value (because moves is 0 indexed)
                userChoice = userChoice - 1
                #We have adjusted our valid user choice, so break out of the loop
                break
            else:
                #If user choice is invalid, print a message to a user and continue to loop
                print("Invalid move. Please try again.")                

        #Return the Human choice to the calling function    
        return moves[userChoice]  

"""DONE TO HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
class MyBot (Player):
    #The name instance variable from Player is overriden, and its value set to Human
    _name = "MyBot"

    #Constructor to build IterativeBot players
    def __init__(self,name):
        super(MyBot,self).__init__("MyBot")

    
    """Overrides the play method inherited from Player, with the Human player picking the moves."""    
    def play(self):            
        return moves[0]  









"""This stuff will eventually go in main!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""                  
#Calls the moves list function, so the moves are instantiated and stored in a list
moves_list()

#A global variable to keep track of the location in the moves list, for use with the Iterative Bot
global p1IterativeCounter
global p2IterativeCounter

#Sets iterativeCounter to 0, which is the start of the moves list
p1IterativeCounter = 0
p2IterativeCounter = 0

global p1
global p2

global p1sOpponentsMove
global p2sOpponentsMove

p1 = None
p2 = None
p1sOpponentsMove = None
p2sOpponentsMove = None

p1 = IterativeBot('Iterative Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")

p1 = LastPlayBot('Last Play Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")

p1 = LastPlayBot('Last Play Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")

p1 = LastPlayBot('Last Play Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")

p1 = LastPlayBot('Last Play Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")

p1 = LastPlayBot('Last Play Bot')
p2 = LastPlayBot('Last Play Bot')
p1Move = p1.play()
p2Move = p2.play()
p1sOpponentsMove = p2Move
p2sOpponentsMove = p1Move
print ("p1 played " + p1Move.name())
print ("p2 played " + p2Move.name())
print (p1Move.compareTo(p2Move))
print("______________________________")
