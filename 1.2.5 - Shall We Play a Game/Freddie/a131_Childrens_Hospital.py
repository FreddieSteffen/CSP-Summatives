#Game setup
import turtle as trtl
import random as rand
import time as time
wn = trtl.Screen()

#Variables
game_board = "Connect4Board.gif"
num1 = 0
num2 = 0
randindex = rand.randint(1,9)
index = randindex
ychip = 0
y = ychip
x = 0
InARow = False
ChipBelow = False
ChipBelow1 = -280
ChipBelow2 = -280
ChipBelow3 = -280
ChipBelow4 = -280
ChipBelow5 = -280
ChipBelow6 = -280
ChipBelow7 = -280
difficulty = 1

#Lists
Board = [(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0)]
Rows = [0,1,2,3,4,5]
Columns = [0,1,2,3,4,5,6]
row1 = Rows[0]
column1 = Columns[0]
playerNameList = []
playeranswerslist = []

#Turtles
#Game board settup
#Game board
wn.setup(width=1.0,height=1.0)
wn.addshape(game_board)
game_board_turtle = trtl.Turtle()
game_board_turtle.shape(game_board)
screen = trtl.Screen()
#Welcome turtle
WelcomeTurtle = trtl.Turtle()
WelcomeTurtle.hideturtle()
WelcomeTurtle.penup()
WelcomeTurtle.goto(-150,300)
WelcomeTurtle.write("Welcome to Connect 4", font=("Arial", 30, "bold"))
#Make chips turtles
RedChip = trtl.Turtle()
RedChip.color("red")
RedChip.shape('circle')
RedChip.shapesize(3.5)
RedChip.penup()
RedChip.goto(400, 100)
YellowChip = trtl.Turtle()
YellowChip.color("yellow")
YellowChip.shape('circle')
YellowChip.shapesize(3.5)
YellowChip.penup()
YellowChip.goto(400, 200)
#Player Turn
playermove = 1
turn = trtl.Turtle()
turn.color("yellow")
turn.shape('circle')
turn.shapesize(3.5)
#Grey Chip
GreyChip = trtl.Turtle()
GreyChip.hideturtle()
GreyChip.color("grey")
GreyChip.shape('circle')
GreyChip.shapesize(3.5)
#New game
pen = trtl.Turtle()
pen.hideturtle()
pen.speed(0)
pen.fillcolor("grey")
pen.penup()
pen.goto(365,-100)
pen.pendown()
pen.begin_fill()
for i in range(2):
  pen.forward(80)
  pen.left(90)
  pen.forward(40)
  pen.left(90)
pen.end_fill()
pen.penup()
pen.goto(410,-80)
pen.write("New Game", align="center", font=("Arial", 14, "bold"))
playernameTurtle = trtl.Turtle()
playernameTurtle.penup()
playernameTurtle.hideturtle()

#Functions

#Players Turn
def playerturn():
  global playermove
  if playermove % 2 == 0:
    turn.color("red")
  else:
    turn.color("yellow")
  turn.penup()
  turn.goto(400,0)
#Question Diffucultys
def PlayerQuestionEasy():
  global index
  num1 = rand.randint(1,100)
  num2 = rand.randint(1,50)
  if index % 2 == 0:
    PlayerQuestionEven = trtl.textinput("Easy", "What is "+str(num1)+" + "+str(num2)+" equal to?")
    if PlayerQuestionEven == (str(num1 + num2)):
      print("Good job you got it right!")
      playeranswerslist.append(PlayerQuestionEven)
      print(playeranswerslist)
    else:
      print("Sorry that's incorect")
  else:
    PlayerQuestionOdd = trtl.textinput("Question", "What is "+str(num1)+" - "+str(num2)+" equal to?")
    if PlayerQuestionOdd == (str(num1 - num2)):
      print("Good job you got it right!")
      playeranswerslist.append(PlayerQuestionOdd)
      print(playeranswerslist)
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
      playeranswerslist.append(PlayerQuestionEven)
      print(playeranswerslist)
    else:
      print("Thats incorect")
      print(str(num1*num2))
      playeranswerslist.append(PlayerQuestionOdd)
      print(playeranswerslist)
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
    playeranswerslist.append(PlayerQuestionEven)
    print(playeranswerslist)
    if PlayerQuestionEven == round((num3 - num2)/num1):
      print("Thats correct")
    else:
      print("That's Incorrect")
      print(str((num3-num2)/num1))
  else:
    PlayerQuestionOdd = trtl.textinput("Hard", "Solve for x (rounded to nearest whole number):" + str(num1) + "x - " + str(num2) + " = " + str(num3))
    PlayerQuestionOdd = int(PlayerQuestionOdd)
    PlayerQuestionOdd = round(PlayerQuestionOdd)
    playeranswerslist.append(PlayerQuestionOdd)
    print(playeranswerslist)
    if PlayerQuestionOdd == round((num3 + num2)/num1):
      print("Thats correct")
    else:
      print("That's Incorrect")
      print(str((num3+num2)/num1))
  randindex = rand.randint(1,9)
  index = index + randindex  
def PlayerDifficulty():
  if playerDif == "Easy" or playerDif == "EASY" or playerDif == "easy":
    PlayerQuestionEasy()
  elif playerDif == "Medium" or playerDif == "medium" or playerDif == "MEDIUM" or playerDif == "Med" or playerDif == "med" or playerDif == "MED":
    PlayerQuestionMed()
  elif playerDif == "Hard" or playerDif == "HARD" or playerDif == "hard":
    PlayerQuestionHard()
  GreyChip.showturtle()
#Grey Chip Hover
def OnClick(x, y):
  global CurrentX, CurrentY, ChipBelow1, ChipBelow2, ChipBelow3, ChipBelow4, ChipBelow5, ChipBelow6, ChipBelow7
  #640x480
  #Column 1
  if -320 < x < -230 and -240 < y < 240:
    GreyChip.penup()
    x = -270
    GreyChip.goto(x, ChipBelow1+80)
  #Column 2
  elif -230 < x < -140 and -240 < y < 240: 
    GreyChip.penup()
    x = -180
    GreyChip.goto(x, ChipBelow2+80)
  #Column 3
  elif -140 < x < -50 and -240 < y < 240:
    GreyChip.penup()
    x = -90
    GreyChip.goto(x, ChipBelow3+80)
  #Column 4
  elif -50 < x <40 and -240 < y < 240:
    GreyChip.penup()
    x = 0
    GreyChip.goto(x, ChipBelow4+80)
  #Column 5
  elif 40 < x < 130 and -240 < y < 240:
    GreyChip.penup()
    x = 90
    GreyChip.goto(x, ChipBelow5+80)
  #Column 6
  elif 130 < x < 220 and -240 < y < 240:
    GreyChip.penup()
    x = 180
    GreyChip.goto(x, ChipBelow6+80)
  #Column 7
  elif 220 < x < 320 and -240 < y < 240:
    GreyChip.penup()
    x = 270
    GreyChip.goto(x, ChipBelow7+80)
  #New Game
  elif 365 < x < 445 and -100 < y < -60:
    RedChip.clear()
    RedChip.penup()
    RedChip.goto(400, 100)
    YellowChip.clear()
    YellowChip.penup()
    YellowChip.goto(400, 200)
    GameLogic()
def countdown(seconds):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
#Chips drop
def ChipsDrop(x, y):
  global CurrentX, CurrentY, playermove, ChipBelow1, ChipBelow2, ChipBelow3, ChipBelow4, ChipBelow5, ChipBelow6, ChipBelow7
  CurrentX = GreyChip.xcor()
  CurrentY = 270
  if -320 < x < 320:
    if playermove % 2 == 0:
      RedChip.penup()
      RedChip.goto(CurrentX,CurrentY)
      RedChip.setheading(90)
      while RedChip.ycor() > ChipBelow:
        RedChip.back(80)
      else: 
        if -320 < x < -230 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow1+80)
          ChipBelow1 = ChipBelow1 + 80
        #Column 2
        elif -230 < x < -140 and -240 < y < 240: 
          RedChip.goto(CurrentX,ChipBelow2+80)
          ChipBelow2 = ChipBelow2 + 80
        #Column 3
        elif -140 < x < -50 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow3+80)
          ChipBelow3 = ChipBelow3 + 80
        #Column 4
        elif -50 < x <40 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow4+80)
          ChipBelow4 = ChipBelow4 + 80
        #Column 5
        elif 40 < x < 130 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow5+80)
          ChipBelow5 = ChipBelow5 + 80
        #Column 6
        elif 130 < x < 220 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow6+80)
          ChipBelow6 = ChipBelow6 + 80
        #Column 7
        elif 220 < x < 320 and -240 < y < 240:
          RedChip.goto(CurrentX,ChipBelow7+80)
          ChipBelow7 = ChipBelow7 + 80
        RedChip.stamp()
        playermove = playermove + 1
        playerturn()
        countdown(1.5)
        GameLogic()

    else:
      YellowChip.penup()
      YellowChip.goto(CurrentX,CurrentY)
      YellowChip.setheading(90)
      while YellowChip.ycor() > ChipBelow:
        YellowChip.back(80)
      else: 
        if -320 < x < -230 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow1+80)
          ChipBelow1 = ChipBelow1 + 80
          print(ChipBelow1)
        #Column 2
        elif -230 < x < -140 and -240 < y < 240: 
          YellowChip.goto(CurrentX,ChipBelow2+80)
          ChipBelow2 = ChipBelow2 + 80
          print(ChipBelow2)
        #Column 3
        elif -140 < x < -50 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow3+80)
          ChipBelow3 = ChipBelow3 + 80
          print(ChipBelow3)
        #Column 4
        elif -50 < x <40 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow4+80)
          ChipBelow4 = ChipBelow4 + 80
          print(ChipBelow4)
        #Column 5
        elif 40 < x < 130 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow5+80)
          ChipBelow5 = ChipBelow5 + 80
          print(ChipBelow5)
        #Column 6
        elif 130 < x < 220 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow6+80)
          ChipBelow6 = ChipBelow6 + 80
          print(ChipBelow6)
        #Column 7
        elif 220 < x < 320 and -240 < y < 240:
          YellowChip.goto(CurrentX,ChipBelow7+80)
          ChipBelow7 = ChipBelow7 + 80
          print(ChipBelow7)

        YellowChip.stamp()
        playermove = playermove + 1
        playerturn()
        countdown(1.5)
        GameLogic()
#Game logic for if someone wins
def GameLogic():
  global difficulty, playerDif
  playerturn()
  while difficulty == 1:
    playerDif = trtl.textinput("Difficulty", "What do you want the difficulty to be? Easy/Med/Hard")
    difficulty = 0
  PlayerDifficulty()
  screen.onclick(OnClick)
  GreyChip.onclick(ChipsDrop)

#Play Game
#Ask if they want to play
play_game = trtl.textinput("Play game?", "Do you want to play the game? Yes or No")
if play_game == "yes" or play_game == "YES" or play_game == "Yes" or play_game == "y" or play_game =="Y":
  playerName1 = trtl.textinput("Name", "What is player 1s name?")
  playerNameList.append(playerName1)
  while "," in playerName1 or len(playerName1) == 0 or "1" in playerName1 or "2" in playerName1 or "3" in playerName1 or "4" in playerName1 or "5" in playerName1 or "6" in playerName1 or "7" in playerName1 or "8" in playerName1 or "9" in playerName1:
    playerName1 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
    break
  playerName2 = trtl.textinput("Name", "What is player 2s name?")
  playerNameList.append(playerName2)
  while "," in playerName2 or len(playerName2) == 0 or "1" in playerName2 or "2" in playerName2 or "3" in playerName2 or "4" in playerName2 or "5" in playerName2 or "6" in playerName2 or "7" in playerName2 or "8" in playerName2 or "9" in playerName2:
    playerName2 = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
    break
  if playermove % 2 == 0:
    playernameTurtle.goto(410,-150)
    playerName = playerNameList[0]
    playernameTurtle.write("It's " + playerName + " Turn", align="center", font=("Arial", 14, "bold"))
  else:
    playernameTurtle.goto(410,-150)
    playerName = playerNameList[1]
    playernameTurtle.write("It's " + playerName + " Turn", align="center", font=("Arial", 14, "bold"))
  GameLogic()
else: 
  WelcomeTurtle.clear()
  GreyChip.clear()
  RedChip.clear()
  YellowChip.clear()
  pen.clear()
  turn.clear()
  WelcomeTurtle.goto(-150,300)
  WelcomeTurtle.write("Welcome to Connect 4", font=("Arial", 30, "bold"))

#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()