# 1.2.5 Shall We Play a Game Summitive
# Blackjack/Slots Game

import turtle as trtl
import random as rand
import tkinter as tk
from PIL import Image

#Image resizing and card shapes
def resize_card(name, size):
    img = Image.open(f"{name}.gif")
    img = img.resize(size)
    img.save(f"{name}_small.gif")

for suit in ["hearts", "diamonds", "clubs", "spades"]:
    resize_card(suit, (30, 30))
wn = trtl.Screen()
hearts = "hearts_small.gif"
diamonds = "diamonds_small.gif"
clubs = "clubs_small.gif"
spades = "spades_small.gif"
wn.addshape(hearts)
wn.addshape(diamonds)
wn.addshape(clubs)
wn.addshape(spades)

#Turtles Setup
#Initilizing
t = trtl.Turtle()  #Named this to save some time
screen = trtl.Screen()
hearts = trtl.Turtle(shape=hearts)
diamonds = trtl.Turtle(shape=diamonds)
clubs = trtl.Turtle(shape=clubs)
spades = trtl.Turtle(shape=spades)
card_turtle = trtl.Turtle()
score_turtle = trtl.Turtle()
pen = trtl.Turtle()
ChipsT = trtl.Turtle()

#Hide Turtles/Speed Setup
hearts.hideturtle()
diamonds.hideturtle()
clubs.hideturtle()
spades.hideturtle()
card_turtle.hideturtle()
score_turtle.hideturtle()
ChipsT.hideturtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
card_turtle.penup()
card_turtle.speed(0)
t.speed(0)

#Lists
SuitsList = ["Hearts", "Diamonds", "Spades", "Clubs"]
NumList = [1,2,3,4,5,6,7,8,9,10,11,12,13]
CardX = [20,160,-220,20,160,-220,20,160,-220,0]
OutlineX = [0,140,-240,0,140,-240,0,0]

#Variables
CardValue = 0
CardName = ""
TempPlayerValue = 0
TempDealerValue = 0
PlayerScore = 0
DealerScore = 0
Chips = 100
max_chars = 8

#Functions
def FaceCardValue():
    global CardValue, CardSuit, CardName
    if CardValue == 13:
        CardValue = 10
        CardName = "King"
    if CardValue == 12:
        CardValue = 10
        CardName = "Queen"
    if CardValue == 11:
        CardValue = 10
        CardName = "Jack"
    if CardValue == 1:
        CardValue = 11
        CardName = "Ace"
    else:
        CardName = str(CardValue)
    print(CardName, "of", CardSuit)

#Core game display
def MainGameCreate():
    global PlayerScore, DealerScore, pen
    t.hideturtle()
    t.penup()
    t.goto(-200,200)
    t.write("Dealer", font=("Arial", 14, "bold"))

    t.goto(160,200)
    t.write(str(player_name), font=("Arial", 14, "bold"))

    t.goto(-200,-160)
    t.write("Dealer Score:" + str(DealerScore), font=("Arial", 14, "bold"))

    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.goto(160,-160)
    score_turtle.write(player_name + " Score: " + str(PlayerScore), font=("Arial", 14, "bold"))

    pen.fillcolor("grey")
    pen.penup()
    pen.goto(-85,-200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-55,-190)
    pen.write("Hit", align="center", font=("Arial", 14, "bold"))

    pen.fillcolor("grey")
    pen.penup()
    pen.goto(5,-200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(35,-190)
    pen.write("Stand", align="center", font=("Arial", 14, "bold"))

#Prints players total chips after finishing
def Cashout():
    ChipsT = trtl.Turtle()
    ChipsT.hideturtle()
    ChipsT.penup()
    ChipsT.speed(0)
    ChipsT.goto(0,160)
    ChipsT.write(f"You got {Chips} Chips.", font=("Arial", 14, "bold"))

#Blackjack logic
def Blackjack():
    global CardValue, TempPlayerValue, PlayerScore, CardSuit, CardName, Chips, bet
    #Generate a new random card
    CardValue = rand.choice(NumList)
    CardSuit = rand.choice(SuitsList)
    FaceCardValue()
    #Add value to player score
    TempPlayerValue = CardValue
    PlayerScore += TempPlayerValue
    #Adjust for Ace if over 21
    if PlayerScore > 21 and CardName == "Ace":
        PlayerScore -= 10
    print(f"{player_name} score is {PlayerScore}")
    #Redraw display with new score
    #Lose condition
    if PlayerScore > 21:
        Chips -= int(bet)
        print("Busted! Chips:", Chips)
        t.penup()
        t.goto(-20, 100)
        ClearScreen()
        t.write("Busted! You lost!", align="center", font=("Arial", 20, "bold"))
        ReplayGame()

#Getting the cards the player starts with
def StartingCards():
    global CardValue, PlayerScore, CardSuit, CardName, DealerScore, TempDealerValue
    ClearScreen()
    PlayerScore = 0
    DealerScore = 0

    # Deal two cards to player
    for i in range(2):
        CardValue = rand.choice(NumList)
        CardSuit = rand.choice(SuitsList)
        FaceCardValue()
        PlayerScore += CardValue
        x = CardX[0]
        DrawCards(x, 160, CardName, CardSuit)
        CardX.pop(0)

    # Deal one card to dealer
    CardValue = rand.choice(NumList)
    CardSuit = rand.choice(SuitsList)
    FaceCardValue()
    TempDealerValue = CardValue
    DealerScore += TempDealerValue
    x = CardX[0]
    DrawCards(x, 160, CardName, CardSuit)
    CardX.pop(0)

    # Update visible info (but NOT the dealer’s hidden logic)
    MainGameCreate()

#Dealer hits and runs logic for chips
def Dealer():
    global CardValue, PlayerScore, CardSuit, Chips, bet, DealerScore, TempDealerValue, pen
    while DealerScore < 17:
        CardValue = rand.choice(NumList)
        CardSuit = rand.choice(SuitsList)
        FaceCardValue()
        TempDealerValue = CardValue
        DealerScore = DealerScore + TempDealerValue
        pen.clear()
        t.clear()
        score_turtle.clear()

    if DealerScore < PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips + int(bet)
    if DealerScore == PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips
    if DealerScore > PlayerScore and DealerScore <= 21 and PlayerScore <= 21:
        Chips = Chips - int(bet)
    print("Dealer score is", DealerScore)
    ClearScreen()
    ReplayGame()

#Clearing everything on the screen
def ClearScreen():
    t.clear()
    pen.clear()
    hearts.clear()
    diamonds.clear()
    spades.clear()
    clubs.clear()
    # also clear display turtles if you have them
    try:
        score_turtle.clear()
    except NameError:
        pass
    wn.update()

#Drawing a new card
def DrawCards(x, y, card_name, card_suit):
    y = 160
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw outline
    for i in range(2):
        t.forward(125)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.penup()
    
    # Write card name/number
    t.goto(x + 80, 135)
    t.write(card_name, font=("Arial", 20, "bold"))
    t.goto(x + 30, 10)
    t.write(card_name, font=("Arial", 20, "bold"))
    
    # Stamp suit
    suit_turtle = {'Hearts': hearts, 'Diamonds': diamonds, 'Spades': spades, 'Clubs': clubs}[card_suit]
    suit_turtle.hideturtle()
    suit_turtle.penup()
    suit_turtle.goto(x + 30, 135)
    suit_turtle.stamp()
    suit_turtle.goto(x + 80, 30)
    suit_turtle.stamp()

#Setting things up to replay
def ReplayGame():
    global PlayerScore, DealerScore
    pen.fillcolor("grey")
    pen.penup()
    pen.goto(-200,200)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-165,210)
    pen.write("Continue", align="center", font=("Arial", 14, "bold"))

    pen.begin_fill()
    pen.penup()
    pen.goto(200,200)
    pen.pendown()
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(235,210)
    pen.write("Cash Out", align="center", font=("Arial", 14, "bold"))
    PlayerScore = 0
    DealerScore = 0

#Asking for how much the player wants to bet
def BetValue():
    global Chips, bet
    while True:
        bet = trtl.textinput("Bet", "How much do you want to bet 1-" + str(Chips) + "?")
        if bet and bet.isnumeric():
            bet = int(bet)
            if 1 <= bet <= Chips:
                ClearScreen()
                StartingCards()
                break
            else:
                bet = trtl.textinput("Bet", "Please enter a valid number between 1 and " + str(Chips))
        else:
            bet = trtl.textinput("Bet", "Please enter only numbers")

#Checking for clicks
def OnClick(x, y):
    global CardValue, TempPlayerValue, PlayerScore, CardSuit, CardName, Chips, TempDealerValue, OutX
    #Continue
    if -200 < x < -120 and 200 < y < 240:
        ClearScreen()
        BetValue()
        CardX = [20,100,160,240,-220,-140,20,100,160,240,-220,-140,0]
        OutlineX = [0,140,-240,0,140,-240,0,0]
        x = CardX[0]
        OutX = OutlineX[0]

    #Cashout
    elif 200 < x < 280 and 200 < y < 240:
        ClearScreen()
        Cashout()

    #Hit
    elif -85 < x < -5 and -200 < y < -160:
        score_turtle.clear()
        CardValue = rand.choice(NumList)
        CardSuit = rand.choice(SuitsList)
        FaceCardValue()
        TempPlayerValue = CardValue
        PlayerScore += TempDealerValue
        score_turtle.penup()
        score_turtle.goto(160,-160)
        score_turtle.write(player_name + " Score: " + str(PlayerScore), font=("Arial", 14, "bold"))
        score_turtle.goto(160,-120)
        score_turtle.write(str(CardName) + " of " + str(CardSuit), font=("Arial", 14, "bold"))
        if (PlayerScore > 21):
            Dealer()
            t.penup()
            t.goto(-20,0)
            t.write("Busted! You lost!", align="center", font=("Arial", 20, "bold"))
            t.goto(-50,-50)
            t.write(f"You Have {Chips} Chips.", font=("Arial", 14, "bold"))

    #Stand
    elif 5 < x < 85 and -200 < y < -160:
        #Player stands then dealer reveals cards
        Dealer()
        t.penup()
        t.goto(0,-50)
        t.write(f"You Have {Chips} Chips.", font=("Arial", 14, "bold"))

#Asking for players name
t.penup()
t.goto(-160,250)
t.pendown()
t.write("Black Jack Simplified", font=("Arial", 35, "bold"))

player_name = trtl.textinput("Name", "Enter your name, with max char "+str(max_chars))
player_name = player_name[:max_chars]

while "," in player_name or len(player_name) == 0 or "1" in player_name or "2" in player_name or "3" in player_name or "4" in player_name or "5" in player_name or "6" in player_name or "7" in player_name or "8" in player_name or "9" in player_name:
  player_name = trtl.textinput("Name", "Please do not use a comma, nothing, or number Enter your name")
  break

#Begin Playing
screen.onclick(OnClick)
ClearScreen()
BetValue()

#Keeping whats on the screen there
wn = trtl.Screen()
wn.mainloop()