#Game setup
import turtle as trtl
import random as rand
wn = trtl.Screen()

#Variables
game_board = "Connect4Board.gif"
num1 = 0
num2 = 0

#Lists
EasyList = ["num1 + num2 = ", "num1 - num2 = "]
MedList = []
HardList = []

#Functions


#Wecome to game

#Ask if they want to play
play_game = trtl.textinput("Play game?", "Do you want to play the game? Yes or No")
if play_game == "yes" or play_game == "YES" or play_game == "Yes" or play_game == "y" or play_game =="Y":
  print("Working")
else: 
  print("Restart if you want to play")

#Game board settup
#Game board
wn.setup(width=1.0,height=1.0)
wn.addshape(game_board)
game_board_turtle = trtl.Turtle()
game_board_turtle.shape(game_board)

#Buttons

#Make chips turtles
RedChip = trtl.Turtle()
RedChip.color("red")
RedChip.shape('circle')
RedChip.shapesize(3.5)
RedChip.back(10)
YellowChip = trtl.Turtle()
YellowChip.color("yellow")
YellowChip.shape('circle')
YellowChip.shapesize(3.5)

#Ask for player1/player2 name
#Ask for what difficulty for both players
playerName1 = trtl.textinput("Name", "What is player 1s name?")
while "," in playerName1 or len(playerName1) == 0 or "1" in playerName1 or "2" in playerName1 or "3" in playerName1 or "4" in playerName1 or "5" in playerName1 or "6" in playerName1 or "7" in playerName1 or "8" in playerName1 or "9" in playerName1:
  playerName1 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
  break

playerName2 = trtl.textinput("Name", "What is player 2s name?")
while "," in playerName2 or len(playerName2) == 0 or "1" in playerName2 or "2" in playerName2 or "3" in playerName2 or "4" in playerName2 or "5" in playerName2 or "6" in playerName2 or "7" in playerName2 or "8" in playerName2 or "9" in playerName2:
  playerName2 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
  break

def PlayerDifficulty():
  playerDif = trtl.textinput("Difficulty", "What do you want the difficulty to be? Easy/Med/Hard")
  if playerDif == "Easy" or playerDif == "EASY" or playerDif == "easy":
    print("Player difficulty is easy")
  elif playerDif == "Medium" or playerDif == "medium" or playerDif == "MEDIUM" or playerDif == "Med" or playerDif == "med" or playerDif == "MED":
    print("Player diff is med")
  elif playerDif == "Hard" or playerDif == "HARD" or playerDif == "hard":
    print("Player difficulty is hard")
  else:
    playerDif
PlayerDifficulty()

#Player Turn

#Question correct If then
randindex = rand.randint(1,9)
index = randindex
def PlayerQuestionEasy():
  if index % 2 == 0:
    Player1QuestionEven = trtl.textinput("Question", "What is "+str(num1)+" + "+str(num2)+" equal to? ")
    if Player1QuestionEven == (str(num1 + num2)):
      print("Good job you got it right!")
    else:
      print("Sorry that's incorect")
  else:
    Player1QuestionOdd = trtl.textinput("Question", "What is "+str(num1)+" - "+str(num2)+" equal to? ")
    if Player1QuestionOdd == (str(num1 - num2)):
      print("Good job you got it right!")
    else:
      print("Sorry that's incorect")
  randindex = rand.randint(1,9)
  index = index + randindex
PlayerQuestionEasy()

  

#----Grey Chip Hover

#Chips drop

#Game logic for if someone wins

#Print Winner

#Ask for replay


#Play Game


#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()