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
def playernames():
  playerName1 = trtl.textinput("Name", "What is player 1s name?")
  while "," in playerName1 or len(playerName1) == 0 or "1" in playerName1 or "2" in playerName1 or "3" in playerName1 or "4" in playerName1 or "5" in playerName1 or "6" in playerName1 or "7" in playerName1 or "8" in playerName1 or "9" in playerName1:
    playerName1 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
    break

  playerName2 = trtl.textinput("Name", "What is player 2s name?")
  while "," in playerName2 or len(playerName2) == 0 or "1" in playerName2 or "2" in playerName2 or "3" in playerName2 or "4" in playerName2 or "5" in playerName2 or "6" in playerName2 or "7" in playerName2 or "8" in playerName2 or "9" in playerName2:
    playerName2 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
    break
playernames()
def PlayerDifficulty():
  playerDif = trtl.textinput("Difficulty", "What do you want the difficulty to be? Easy/Med/Hard")
  if playerDif == "Easy" or playerDif == "EASY" or playerDif == "easy":
    PlayerQuestionEasy()
  elif playerDif == "Medium" or playerDif == "medium" or playerDif == "MEDIUM" or playerDif == "Med" or playerDif == "med" or playerDif == "MED":
    PlayerQuestionMed()
  elif playerDif == "Hard" or playerDif == "HARD" or playerDif == "hard":
    PlayerQuestionHard()
  else:
    PlayerDifficulty()

#Player Turn
playermove = 1
turn = trtl.Turtle()
turn.color("red")
turn.shape('circle')
turn.shapesize(3.5)
def playerturn():
  global playermove
  if playermove % 2 == 0:
    turn.color("red")
  else:
    turn.color("yellow")
  turn.penup()
  turn.goto(400,0)
  playermove = playermove + 1


#Question correct If then
randindex = rand.randint(1,9)
index = randindex
def PlayerQuestionEasy():
  global index
  num1 = rand.randint(1,100)
  num2 = rand.randint(1,50)
  if index % 2 == 0:
    PlayerQuestionEven = trtl.textinput("Easy", "What is "+str(num1)+" + "+str(num2)+" equal to?")
    if PlayerQuestionEven == (str(num1 + num2)):
      print("Good job you got it right!")
    else:
      print("Sorry that's incorect")
  else:
    PlayerQuestionOdd = trtl.textinput("Question", "What is "+str(num1)+" - "+str(num2)+" equal to?")
    if PlayerQuestionOdd == (str(num1 - num2)):
      print("Good job you got it right!")
    else:
      print("Sorry that's incorect")
  randindex = rand.randint(1,9)
  index = index + randindex

def PlayerQuestionMed():
  num1 = rand.randrange(1,10)
  num2 = rand.randint(1,10)
  global index
  if index % 2 == 0:
    PlayerQuestionEven = trtl.textinput("Medium", "What is " + str(num1) + " x " + str(num2) + " equal to?")
    if PlayerQuestionEven == (str(num1*num2)):
      print("Thats correct")
      print(PlayerQuestionEven)
    else:
      print("Thats incorect")
      print(str(num1*num2))
      print(PlayerQuestionEven)
  else:
    if num1 % num2 == 0:
      PlayerQuestionOdd = trtl.textinput("Medium", "What is " + str(num1) + " / " + str(num2) + " equal to?")
      if (num1 / num2) % 1 == 0:
        PlayerQuestionOdd = PlayerQuestionOdd + ".0"
      if PlayerQuestionOdd == (str(num1/num2)):
        print("thats correct")
        print(PlayerQuestionOdd)
      else:
        print("thats incorrect")
        print(str(num1/num2))
        print(PlayerQuestionOdd)
    else:
      num2 = 2
      PlayerQuestionOdd = trtl.textinput("Medium", "What is " + str(num1) + " / " + str(num2) + " equal to?")
      if (num1 / num2) % 1 == 0:
        PlayerQuestionOdd = PlayerQuestionOdd + ".0"
        print(PlayerQuestionOdd)
      if PlayerQuestionOdd == (str(num1/num2)):
        print("thats correct")
        print(PlayerQuestionOdd)
      else:
        print("thats incorrect")
        print(str(num1/num2))
        print(PlayerQuestionOdd)
  randindex = rand.randint(1,9)
  index = index + randindex
  
def PlayerQuestionHard():
  num1 = rand.randint(1,5)
  num2 = rand.randint(1,5)
  num3 = rand.randint(1,5)
  global index
  if index % 2 == 0:
    PlayerQuestionEven = trtl.textinput("Hard", "Solve for x (rounded to nearest whole number): " + str(num1) + "x + " + str(num2) + " = " + str(num3))
    PlayerQuestionEven = int(PlayerQuestionEven)
    PlayerQuestionEven = round(PlayerQuestionEven)
    print(PlayerQuestionEven)
    if PlayerQuestionEven == round((num3 - num2)/num1):
      print("Thats correct")
    else:
      print("That's Incorrect")
      print(str((num3-num2)/num1))
  else:
    PlayerQuestionOdd = trtl.textinput("Hard", "Solve for x (rounded to nearest whole number):" + str(num1) + "x - " + str(num2) + " = " + str(num3))
    PlayerQuestionOdd = int(PlayerQuestionOdd)
    PlayerQuestionOdd = round(PlayerQuestionOdd)
    print(PlayerQuestionOdd)
    if PlayerQuestionOdd == round((num3 + num2)/num1):
      print("Thats correct")
    else:
      print("That's Incorrect")
      print(str((num3+num2)/num1))
  randindex = rand.randint(1,9)
  index = index + randindex  

#----Grey Chip Hover

#Chips drop

#Game logic for if someone wins

#Print Winner

#Ask for replay
def playagain():
  playernames()
  PlayerDifficulty()

#Play Game
playagain()

#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()