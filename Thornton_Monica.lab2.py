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

#For use in generating random numbers
import random

class MainClass:

    def main(self):
        global p1
        global p2
    
        global rounds

        #Keeps track of p1OldMove (because it gets overwritten right away), and p2Move as global variables for use in the LastPlayBot and MyBot
        global p1OldMove
        global p2Move

        #A global variable to keep track of the location in the moves list, for use with the Iterative Bot
        global p1IterativeCounter
        global p2IterativeCounter

        #Sets iterativeCounter to 0, which is the start of the moves list
        p1IterativeCounter = 0
        p2IterativeCounter = 0

        p1 = None
        p2 = None

        p1Move = None
        p2Move = None

        p1Wins = 0
        p2Wins = 0

        #String variable indicating my name.
        #I did not work with a partner on this lab
        myName = "Monica Thornton"
        
        rounds = 1

        #move all this to a print menu func??????????????????????????????????????????????????????????????
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by " + myName + "\n")
        print("Please choose two players: ")        
        print("   (1) Human")
        print("   (2) Stupid Bot")
        print("   (3) Random Bot")
        print("   (4) Iterative Bot")
        print("   (5) Last Play Bot")
        print("   (6) My Bot\n")

        #Sets up a list with all of the valid choices, so we can make sure the user picks one  
        validChoices = [1, 2, 3, 4, 5, 6]

        #Loop to make sure that the input for Player 1 is one of the valid choices
        while True:
            #Gets the first selection from the user
            userChoice1 = input("Select Player 1: ")

            #tests that the user inputs are digits, and also that they are one of the valid choices in the list above
            if str.isdigit(userChoice1) == True and int(userChoice1) in validChoices:
                userChoice1 = int(userChoice1)
                #Checks if the user choice is valid
                if userChoice1 in validChoices:
                    if userChoice1 == 1:
                        p1 = Human('Human')
                        
                    elif userChoice1 == 2:
                        p1 = StupidBot('Stupid Bot')

                    elif userChoice1 == 3:
                        p1 = RandomBot('Random Bot')

                    elif userChoice1 == 4:
                        p1 = IterativeBot('Iterative Bot')

                    elif userChoice1 == 5:
                        p1 = LastPlayBot('Last Play Bot')

                    elif userChoice1 == 6:
                        p1 = MyBot('MyBot')
                    break
            else:
                #If user choice is invalid, print a message to a user and continue to loop
                print("Invalid bot choice. Please try again.")

        #Loop to make sure that the input for Player 2 is one of the valid choices
        while True:
            #Gets the first selection from the user
            userChoice2 = input("Select Player 2: ")

            #tests that the user inputs are digits, and also that they are one of the valid choices in the list above
            if str.isdigit(userChoice2) == True and int(userChoice2) in validChoices:
                userChoice2 = int(userChoice2)
                #Checks if the user choice is valid
                if userChoice2 in validChoices:
                    if userChoice2 == 1:
                        p2 = Human('Human')
                        
                    elif userChoice2 == 2:
                        p2 = StupidBot('Stupid Bot')

                    elif userChoice2 == 3:
                        p2 = RandomBot('Random Bot')

                    elif userChoice2 == 4:
                        p2 = IterativeBot('Iterative Bot')

                    elif userChoice2 == 5:
                        p2 = LastPlayBot('Last Play Bot')

                    elif userChoice2 == 6:
                        p2 = MyBot('MyBot')
                    break
            else:
                #If user choice is invalid, print a message to a user and continue to loop
                print("Invalid bot choice. Please try again.")

        print("\n" + p1.name() + " vs " + p2.name() +". Go!\n")

        for x in range (0, 5):
            print ("Round " + str(rounds) +":")
            p1OldMove = p1Move
            p1Move = p1.play()
            p2Move = p2.play()
            
            print("Player 1 chose " + p1Move.name())
            print("Player 2 chose " + p2Move.name())
            outcome = p1Move.compareTo(p2Move)

            print(outcome[0])
                        
            if outcome[1] == "Win":
                p1Wins = p1Wins + 1
                print("Player 1 won the round\n")
            elif outcome[1] == "Lose":
                p2Wins = p2Wins + 1
                print("Player 2 won the round\n")
            else:
                print("Round was a tie\n")
                
            rounds = rounds + 1

        print ("The score is " + str(p1Wins) + " to " + str(p2Wins) + ".")

        if p1Wins == p2Wins:
            print("Game was a draw.")
        elif p1Wins > p2Wins:
            print("Player 1 wins the game.")
        else:
            print("Player 2 wins the game.")    


     
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
    the moves list and played, and the move immediately following it is picked for our next move. We start over once we have gone through the entire
    moves list."""    
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
        global p1oldMove
        global p2Move

        #Checks if we are in the first round
        global rounds
       
        #Checks if self is p1 or p2 - to update the correct global variables
        if p1 == self:
            #opponentMove is a local variable to keep track of what your opponent played
            opponentMove = p2Move
            
            #If first move of round (ergo, opponent has not moved yet), play random move
            if opponentMove is None or rounds == 1:

                #Generate a random number between 0 and 4, save it in the variable randomMove
                randomMove = random.randint(0, 4)
            
                #Use randomMove variable to get a move from the moves list
                return moves[randomMove]
        
            else:
                
                #If your opponent has already moved, play their move from last turn for this turn
                return opponentMove

        elif p2 == self:
            #opponentMove is a local variable to keep track of what your opponent played
            opponentMove = p1OldMove

            #If first move of round (ergo, opponent has not moved yet), play random move
            if opponentMove is None or rounds == 1:
                
                print("You are in the first part of p2 (the random part)")
                #Generate a random number between 0 and 4, save it in the variable randomMove
                randomMove = random.randint(0, 4)
            
                #Use randomMove variable to get a move from the moves list
                return moves[randomMove]
        
            else:
                #If your opponent has already moved, play their move from last turn for this turn
                print("You are in the second part of p2 (the play last move part)")
                print("Opponent's last move was " + opponentMove.name())
                return opponentMove

"""A subclass to represent the Human player, in which the series of moves are determined by the Human player."""
class Human (Player):
    #The name instance variable from Player is overriden, and its value set to Human
    _name = "Human"

    #Constructor to build Human players
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
            #Gets the selection from the user
            userChoice = input("Enter your move: ")
            #inserts an empty line, because if you have 2 Human players, output can look a bit cluttered
            print("")
            #tests that the user input is a digit, and also that it is one of the valid choices in the list above
            if str.isdigit(userChoice) == True and int(userChoice) in validChoices:
                userChoice = int(userChoice)
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

"""MyBot uses the fact that while a random player is going to have the highest percentage of wins, a Human player is
rarely truly random. This bot exploits some of the well known fallacies of the human player, and depending on the number
of rounds played so far, the opponent's last move, and the win/loss ratio, employs different strategies."""
class MyBot (Player):
    #The name instance variable from Player is overriden, and its value set to MyBot
    _name = "MyBot"

    #Constructor to build MyBot players
    def __init__(self,name):
        super(MyBot,self).__init__("MyBot")

    """Overrides the play method inherited from Player, with the MyBot strategy implemented. Details of the strategy are found in the
    comments for the conditional statements below"""    
    def play(self):
        #Specifies that the below variables are global, used to specify/differentiate between p1 and p2        
        global p1
        global p2

        #global variable to keep track of the number of rounds        
        global rounds

        #global variable to keep track of the number of wins
        global p1Wins
        global p2Wins

        #global variable to keep track of the last moves for p1 and p2
        global p1OldMove
        global p2Move

        #saves the last move made by p1 into a local variable
        p1LastMove = p1OldMove
        
        #saves the last move made by p2 into a local variable        
        p2LastMove = p2Move
        
        """Inexperienced players tend to lead with rock (for males) and paper (for females) - paper will beat rock and tie paper, so this is the most likely first
        move. Based on that information, we make paper the most likely first move. However, if the first for the MyBot player is always Paper, it will be very easy
        to beat, so knowing that the other player is anticipating a paper play - choose either Spock (who will smash scissors, but still vaporize rock) or Rock
        (which will crush Lizard, yet still tie if they play rock)."""
        if rounds == 1:

            #generates a random integer, so we can choose from Paper, Spock and Lizard
            randomInteger = random.randint(1, 4)

            if randomInteger < 2:
                return moves[4]
            elif randomInteger == 2:
                return moves[0]
            else:
                return moves[1]

        """When they are losing, people are more likely to (subconciously)play the move that would have beaten their last move. Therefore, if the other player
        is losing, make a move to counter that strategy (again, don't rely on throwing one move exclusively - but make it the most likely move)."""
        if self == p1:
            #if p1 (self, the MyBot player) is winning, we anticipate the other player will get desperate and go for the strategy described above 
            if p1Wins > p2Wins:

                randomInteger = random.randint(1, 4)
                                 
                if p2LastMove.name() == "Rock":
                    #p2 is likely to play what would have beaten Rock (Spock or Paper)
                    #Based on that assumption, p1 chooses their move to beat Spock or Paper - and Lizard beats both, so that is the most likely move.
                    
                    if randomInteger >= 2:
                        #Make Lizard the move most often thrown in this situation
                        calculatedMove = moves[3]
                    elif randomInteger == 2:
                        #Throw Scissors about 25% of the time
                        calculatedMove = moves[2]
                    else:
                        #Throw Paper about 25% of the time
                        calculatedMove = moves[1]
                        
                elif p2LastMove.name() == "Paper":
                    #p2 is likely to play what would have beaten Paper (Scissors or Lizard)
                    #Based on that assumption, p1 chooses their move to beat Scissors or Lizard - and Rock beats both, so that is the most likely move.
                    if randomInteger >= 2:
                        #Make Rock the move most often thrown in this situation
                        calculatedMove = moves[0]
                    elif randomInteger == 2:
                        #Throw Scissors about 25% of the time
                        calculatedMove = moves[2]
                    else:
                        #Throw Spock about 25% of the time
                        calculatedMove = moves[4]
           
                elif p2LastMove.name() == "Scissors":
                    #p2 is likely to play what would have beaten Scissors (Spock or Rock)
                    #Based on that assumption, p1 chooses their move to beat Spock or Rock - and Paper beats both, so that is the most likely move.

                    if randomInteger >= 2:
                        #Make Paper the move most often thrown in this situation
                        calculatedMove = moves[1]
                    elif randomInteger == 2:
                        #Throw Lizard about 25% of the time
                        calculatedMove = moves[3]
                    else:
                        #Throw Spock about 25% of the time
                        calculatedMove = moves[4]

                elif p2LastMove.name() == "Lizard":
                    #p2 is likely to play what would have beaten Lizard (Rock or Scissors)
                    #Based on that assumption, p1 chooses their move to beat Rock or Scissors - and  Spock beats both, so that is the most likely move.

                    if randomInteger >= 2:
                        #Make Spock the move most often thrown in this situation
                        calculatedMove = moves[4]
                    elif randomInteger == 2:
                        #Throw Paper about 25% of the time
                        calculatedMove = moves[1]
                    else:
                        #Throw Rock about 25% of the time
                        calculatedMove = moves[0]
            
                elif p2LastMove.name() == "Spock":
                    #p2 is likely to play what would have beaten Spock (Paper or Lizard)
                    #Based on that assumption, p1 chooses their move to beat Paper or Lizard - and Scissors beats both, so that is the most likely move.

                    if randomInteger >= 2:
                        #Make Scissors the move most often thrown in this situation
                        calculatedMove = moves[2]
                    elif randomInteger == 2:
                        #Throw Lizard about 25% of the time
                        calculatedMove = moves[3]
                    else:
                        #Throw Rock about 25% of the time
                        calculatedMove = moves[0]


        #if p2 (self, the MyBot player) is winning, we anticipate the other player will get desperate and go for the strategy described above   
        elif self == p2:
                randomInteger = random.randint(1, 4)
                if p1Wins < p2Wins:  
                    if p1LastMove.name() == "Rock":
                        #p1 is likely to play what would have beaten Rock (Spock or Paper)
                        #Based on that assumption, p2 chooses their move to beat Spock or Paper - and Lizard beats both, so that is the most likely move.
                    
                        if randomInteger >= 2:
                            #Make Lizard the move most often thrown in this situation
                            calculatedMove = moves[3]
                        elif randomInteger == 2:
                            #Throw Scissors about 25% of the time
                            calculatedMove = moves[2]
                    else:
                        #Throw Paper about 25% of the time
                        calculatedMove = moves[1]

                elif p1LastMove.name() == "Paper":
                    #p1 is likely to play what would have beaten Paper (Scissors or Lizard)
                    #Based on that assumption, p2 chooses their move to beat Scissors or Lizard - and Rock beats both, so that is the most likely move.
                    if randomInteger >= 2:
                        #Make Rock the move most often thrown in this situation
                        calculatedMove = moves[0]
                    elif randomInteger == 2:
                        #Throw Scissors about 25% of the time
                        calculatedMove = moves[2]
                    else:
                        #Throw Spock about 25% of the time
                        calculatedMove = moves[4]

                elif p1LastMove.name() == "Scissors":
                    #p1 is likely to play what would have beaten Scissors (Spock or Rock)
                    #Based on that assumption, p2 chooses their move to beat Spock or Rock - and Paper beats both, so that is the most likely move.
                    
                    if randomInteger >= 2:
                        #Make Paper the move most often thrown in this situation
                        calculatedMove = moves[1]
                    elif randomInteger == 2:
                        #Throw Lizard about 25% of the time
                        calculatedMove = moves[3]
                    else:
                        #Throw Spock about 25% of the time
                        calculatedMove = moves[4]
                        
                elif p2LastMove.name() == "Lizard":
                    #p1 is likely to play what would have beaten Lizard (Rock or Scissors)
                    #Based on that assumption, p2 chooses their move to beat Rock or Scissors - and  Spock beats both, so that is the most likely move.
                    
                    if randomInteger >= 2:
                        #Make Spock the move most often thrown in this situation
                        calculatedMove = moves[4]
                    elif randomInteger == 2:
                        #Throw Paper about 25% of the time
                        calculatedMove = moves[1]
                    else:
                        #Throw Rock about 25% of the time
                        calculatedMove = moves[0]
            
                elif p2LastMove.name() == "Spock":
                    #p1 is likely to play what would have beaten Spock (Paper or Lizard)
                    #Based on that assumption, p2 chooses their move to beat Paper or Lizard - and Scissors beats both, so that is the most likely move.

                    if randomInteger >= 2:
                        #Make Scissors the move most often thrown in this situation
                        calculatedMove = moves[2]
                    elif randomInteger == 2:
                        #Throw Lizard about 25% of the time
                        calculatedMove = moves[3]
                    else:
                        #Throw Rock about 25% of the time
                        calculatedMove = moves[0]

                    #based on the decisions you have made above (given the opponents throw), throw the move that makes the most sense   
                    return calculatedMove

        #If self player is losing, falls back on a random strategy (as that is the most effective strategy)

        #selects a move at random from the move list
        randomMove = random.randint(0, 4)
        return moves[randomMove]

"""This stuff will eventually go in main!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""                  
#Calls the moves list function, so the moves are instantiated and stored in a list
moves_list()







p1Wins = 0
p2Wins = 0
rounds = 0




mc = MainClass
mc.main('Main Class')










