import ConnectFour
from ConnectFour import *

"""
PLAYERS:
+--HumanPlayer('human')
+--RandomPlayer('random')
+--MinimaxPlayer('minimax')
+--QLearningPlayer('q-agent')

TRAINING Q-AGENT:
+--Initialize two QLearningPlayer('player-1')
+--Initialize a game object from ConnectFourBoard(p1, p2)
   +--Pass the Player-1 and Player-2 objects
+--Use the game objects train function and pass the number of rounds to be trained for
+--Save the Policy for the QLearningPlayer from the object created

EXAMPLE:
p1 = QLearningPlayer('Q1')
p2 = QLearningPlayer('Q2')

game = ConnectFourBoard(p1, p2)
game.train(500000)

p1.savePolicy()
p2.savePolicy()

LOADING AGENT:
+--Initialize the QLearningPlayer('player-1')
+--Use the object to load the policy with the name of the pickle file
   +--p1.loadPolicy('policy_QLearning-1') 
+--Initialize a game object from ConnectFourBoard(p1, p2)
   +--Pass the Player-1 and Player-2 objects
+--Use the game.play() function to play the game

EXAMPLE:
p1 = QLearningPlayer('Q1')
p1.loadPolicy('policy_QLearning-1')

game = ConnectFourBoard(p1, p2)
game.play()    
"""


ConnectFour.ROWS = 6
ConnectFour.COLS = 7

p1 = QLearningPlayer('Q1-6x7')
p2 = QLearningPlayer('Q2-6x7')

game = ConnectFourBoard(p1, p2)
game.train(500000)

p1.savePolicy()
p2.savePolicy()


# p1 = RandomPlayer('random')
# p2 = MinimaxPlayer('minimax')
# game = ConnectFourBoard(p1, p2)
# game.play()

